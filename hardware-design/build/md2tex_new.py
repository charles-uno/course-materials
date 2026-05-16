#!/usr/bin/env python3

import argparse
import json
import os
import sys
import yaml


def main() -> int:
    md_path = get_md_path()
    tex_path = md_path.replace(".md", ".gen.tex")
    print(f"building \033[96m{md_path}\033[0m -> \033[96m{tex_path}\033[0m ... ", end="")
    sys.stdout.flush()

    doc = Document(md_path)

    print(doc.to_html())

    with open(tex_path, "w") as handle:
        handle.write(doc.to_tex())

    print("\033[92mdone\033[0m")

    return 0


class DocElement:

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        instance._params = {}
        instance._children = []
        return instance

    def _children_to_tex(self) -> str:
        return "\n".join(c.to_tex() for c in self._children)

    def to_tex(self) -> str:
        return self._children_to_tex()

    def to_html(self) -> str:
        children = "\n".join(c.to_html() for c in self._children)
        tag_close = f"</{self.__class__.__name__}>"
        return "\n".join([self._html_open(), indent(children), self._html_close()])

    def _html_open(self, include_params=True) -> str:
        if include_params and self._params:
            params_pretty = json.dumps(self._params)
            return f"<{self.__class__.__name__} {params_pretty}>"
        return f"<{self.__class__.__name__}>"

    def _html_close(self) -> str:
        return f"</{self.__class__.__name__}>"

    def _html_solo(self) -> str:
        return f"<{self.__class__.__name__} \>"


def indent(text, depth=2) -> str:
    return "\n".join(" "*depth + l for l in text.splitlines())




class Section(DocElement):

    def __init__(self, raw, head):
        title, contents = get_title_and_contents(raw)
        self._params = {"title": title}
        self._children = get_children(contents, head)

    @classmethod
    def matches(cls, raw: str) -> bool:
        return raw.startswith("# ")

    def to_tex(self) -> str:
        return "\n" + r"\section{" + self._params["title"] + "}\n" + self._children_to_tex()

    @classmethod
    def get_with_leftovers(cls, body: str, head: dict) -> tuple[Section, str]:
        # Section goes until the next section or the end of the doc
        current, leftovers = break_at_line_starting_with(body, ["# "])
        return Section(current, head), leftovers


class Subsection(DocElement):

    def __init__(self, raw, head):
        title, contents = get_title_and_contents(raw)
        self._params = {"title": title}
        self._children = get_children(contents, head)

    @classmethod
    def matches(cls, raw: str) -> bool:
        return raw.startswith("## ")

    def to_tex(self) -> str:
        return "\n" + r"\subsection{" + self._params["title"] + "}\n" + self._children_to_tex()

    @classmethod
    def get_with_leftovers(cls, body: str, head: dict) -> tuple[Subsection, str]:
        # Section goes until the next section, next subsection, or the end of the doc
        current, leftovers = break_at_line_starting_with(body, ["## ", "# "])
        return cls(current, head), leftovers



class UnorderedList(DocElement):

    MARKERS = ("- ", "* ")

    def __init__(self, raw, head):
        self._children = self._get_items(raw, head)

    def to_tex(self) -> str:
        return r"\begin{itemize}" + "\n" + self._children_to_tex() + "\n" + r"\end{itemize}"

    @classmethod
    def matches(cls, raw: str) -> bool:
        return any(raw.startswith(m) for m in cls.MARKERS)

    @classmethod
    def get_with_leftovers(cls, body: str, head: dict) -> tuple[Subsection, str]:
        # list continues as long as we see indented lines and lines starting with list markers
        # TODO: smarter indentation handling for nested lists
        current, leftovers = break_at_line_starting_without(body, [" ", "- ", "* "])
        return cls(current, head), leftovers

    def _get_items(self, raw: str, head: dict) -> list[DocElement]:
        delims = ["- ", "* "]
        raw_items = []
        for line in raw.splitlines():
            if any(line.startswith(d) for d in delims):
                raw_items.append(line)
            else:
                raw_items[-1] += "\n" + line
        return [UnorderedListItem(ri, head) for ri in raw_items]


class UnorderedListItem(DocElement):

    def __init__(self, raw, head):
        # chop off the list item delimiter
        raw = raw.split(None, 1)[-1]
        # if this is a multi-line item, following lines are indented. chop
        # that off so we can identify nested stuff
        if "\n" in raw:
            lines = raw.splitlines()
            indent = len(lines[1]) - len(lines[1].lstrip())
            
            print(lines[1], "indented by:", indent)

            lines = lines[:1] + [l[indent:] for l in lines[1:]]
            raw = "\n".join(lines)

        # list items are usually just a line of text. but in principle one list
        # item can have multiple lines of text, code blocks, etc.
        self._children = get_children(raw, head)

    def to_tex(self):
        return r"\item " + self._children_to_tex() + "\n"


def break_at_line_starting_with(body: str, delim: list[str]) -> tuple[str, str]:
    leftover_lines = body.splitlines()
    # don't break on the first line. we are in a section and looking for the start of the next section
    lines = [leftover_lines.pop(0)]
    while leftover_lines:
        if any(leftover_lines[0].startswith(d) for d in delim):
            break
        lines.append(leftover_lines.pop(0))
    return "\n".join(lines), "\n".join(leftover_lines)



def break_at_line_starting_without(body: str, delim: list[str]) -> tuple[str, str]:
    leftover_lines = body.splitlines()
    # don't break on the first line. we are in a section and looking for the start of the next section
    lines = [leftover_lines.pop(0)]
    while leftover_lines:
        if not any(leftover_lines[0].startswith(d) for d in delim):
            break
        lines.append(leftover_lines.pop(0))
    return "\n".join(lines), "\n".join(leftover_lines)


def get_title_and_contents(body: str) -> tuple[str, str]:
    if "\n" in body:
        title, contents = body.split("\n", 1)
    else:
        title, contents = body, ""
    return title.split(None, 1)[-1], contents


def get_children(raw: str, head: dict) -> list[DocElement]:
    children = []
    while raw:
        next_elt, raw = get_next_and_leftovers(raw, head)
        children.append(next_elt)
    return children


def get_next_and_leftovers(raw: str, head: dict) -> tuple[DocElement, str]:
    while raw.startswith("\n"):
        raw = raw[1:]
    if Section.matches(raw):
        return Section.get_with_leftovers(raw, head)
    elif Subsection.matches(raw):
        return Subsection.get_with_leftovers(raw, head)
    elif CodeBlock.matches(raw):
        return CodeBlock.get_with_leftovers(raw, head)
    elif UnorderedList.matches(raw):
        return UnorderedList.get_with_leftovers(raw, head)
    elif EmptyLine.matches(raw):
        return EmptyLine(raw, head).get_with_leftovers(raw, head)
    else:
        return TextLine(raw, head).get_with_leftovers(raw, head)





class CodeBlock(DocElement):

    def __init__(self, body, head):
        first_line, content = body.split("\n", 1)
        if "," in first_line:
            language, flags = first_line.split(",", 1)
        else:
            language, flags = first_line, ""
        self._params = {"language": language or "text", "flags": flags, "content": content}
        self._children = []

    def to_tex(self) -> str:
        language = self._params["language"]
        content = self._params["content"]
        flags = self._params["flags"]
        if flags:
            return r"\begin{minted}[" + flags + "]{" + language + "}\n" + content + "\n" + r"\end{minted}"
        else:
            return r"\begin{minted}{" + language + "}\n" + content + "\n" + r"\end{minted}"


    def to_html(self) -> str:
        return self._html_open(False) + self._params["content"] + self._html_close()



    @classmethod
    def matches(cls, raw: str) -> bool:
        return raw.startswith("```")

    @classmethod
    def get_with_leftovers(cls, raw: str, head: dict) -> tuple[Subsection, str]:
        assert cls.matches(raw)
        raw = raw.lstrip("```")
        assert "\n```" in raw
        body, leftovers = raw.split("\n```", 1)
        return cls(body, head), leftovers



class Literal(DocElement):

    def __init__(self, raw, head):
        self._params = {"text": raw}

    def to_tex(self):
        return self._params["text"]

    def to_html(self) -> str:
        return self._params["text"]



class EmptyLine(DocElement):

    def __init__(self, body, head):
        pass

    def to_tex(self):
        return "\n"
    
    def to_html(self) -> str:
        return self._html_solo()
    
    @classmethod
    def matches(cls, raw: str) -> bool:
        return raw and not raw.splitlines()[0].strip()

    @classmethod
    def get_with_leftovers(cls, raw: str, head: dict) -> tuple[EmptyLine, str]:
        # if there are multiple empty lines in a row, absorb them all
        lines = raw.splitlines()
        while lines and not lines[0].strip():
            lines.pop(0)
        return cls("", head), "\n".join(lines)


class TextLine(DocElement):

    def __init__(self, body, head):
        self._params = {"text": body}

    def to_tex(self):
        return r"\text{" + self._params["text"] + "}"

    def to_html(self) -> str:
        return self._html_open(False) + self._params["text"] + self._html_close()

    @classmethod
    def get_with_leftovers(cls, raw: str, head: dict) -> tuple[TextLine, str]:
        lines = raw.splitlines()
        return cls(lines[0], head), "\n".join(lines[1:])



class Document(DocElement):

    def __init__(self, md_path: str):
        head, body = self._get_head_and_body(md_path)
        self._children = get_children(body, head)

    def _get_head_and_body(self, md_path: str) -> tuple[dict, str]:
        with open(md_path, "r") as handle:
            lines = [x.rstrip() for x in handle.readlines()]
        header_lines = []
        while lines:
            line = lines.pop(0)
            if line.startswith("---"):
                break
            header_lines.append(line)
        if lines:
            head = yaml.safe_load("\n".join(header_lines)) or {}
            body = "\n".join(lines)
        else:
            # no YAML header
            head = {}
            body = "\n".join(header_lines)
        return head, body

    def to_tex(self) -> str:
        return self._children_to_tex()


def md_path(path):
    if not os.path.exists(path):
        raise argparse.ArgumentTypeError(f"input path '{path}' does not exist")
    if not path.endswith('.md'):
        raise argparse.ArgumentTypeError(f"input path '{path}' must end in .md")
    return path


def get_md_path():
    parser = argparse.ArgumentParser(
        prog="md2tex",
        description="convert markdown to latex",
    )
    parser.add_argument(
        "md_path", type=md_path, help="path to the input markdown file"
    )
    return parser.parse_args().md_path


class ParseFailure(Exception):
    pass


if __name__ == "__main__":

    try:
        sys.exit(main())
    except RecursionError:
        print("RECURSION ERROR")
        sys.exit(1)