#!/usr/bin/env python3

import argparse
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

    _HTML_TAG = None

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        instance._params = {}
        instance._children = []
        return instance

    def to_tex(self) -> str:
        return self._children_to_tex()

    def _children_to_tex(self) -> str:
        return "\n".join(c.to_tex() for c in self._children)

    def to_html(self) -> str:
        return "\n".join([self._html_open(), indent(self._children_to_html()), self._html_close()])

    def _children_to_html(self) -> str:
        return "\n".join(c.to_html() for c in self._children)

    def _html_tag_name(self) -> str:
        return self._HTML_TAG or self.__class__.__name__

    def _html_open(self, include_params=True) -> str:
        if include_params and self._params:
            return f"<{self._html_tag_name()} {pretty_html_params(self._params)}>"
        return f"<{self._html_tag_name()}>"

    def _html_close(self) -> str:
        return f"</{self._html_tag_name()}>"

    def _html_solo(self) -> str:
        return f"<{self._html_tag_name()} \\>"


def pretty_html_params(params: dict) -> str:
    pretty = []
    for key, val in params.items():
        assert isinstance(key, str)
        if val is None:
            continue
        elif isinstance(val, str):
            pretty.append(f'{key}="{val}"')
        elif isinstance(val, int) or isinstance(val, float):
            pretty.append(f'{key}={val}')
        else:
            raise ValueError(f"Unsupported HTML params: {params}")
    return " ".join(pretty)


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




class Subsubsection(DocElement):

    def __init__(self, raw, head):
        title, contents = get_title_and_contents(raw)
        self._params = {"title": title}
        self._children = get_children(contents, head)

    @classmethod
    def matches(cls, raw: str) -> bool:
        return raw.startswith("### ")

    def to_tex(self) -> str:
        return "\n" + r"\subsubsection{" + self._params["title"] + "}\n" + self._children_to_tex()

    @classmethod
    def get_with_leftovers(cls, body: str, head: dict) -> tuple[Subsection, str]:
        # Section goes until the next section, next subsection, or the end of the doc
        current, leftovers = break_at_line_starting_with(body, ["### ", "## ", "# "])
        return cls(current, head), leftovers


class UnorderedList(DocElement):

    _HTML_TAG = "ul"

    _MARKERS = ("- ", "* ")

    def __init__(self, raw, head):
        self._children = self._get_items(raw, head)

    def to_tex(self) -> str:
        return r"\begin{itemize}" + "\n" + self._children_to_tex() + "\n" + r"\end{itemize}"

    @classmethod
    def matches(cls, raw: str) -> bool:
        return any(raw.startswith(m) for m in cls._MARKERS)

    @classmethod
    def get_with_leftovers(cls, body: str, head: dict) -> tuple[DocElement, str]:
        # list continues as long as we see indented lines and lines starting with list markers
        # TODO: smarter indentation handling for nested lists
        current, leftovers = break_at_line_starting_without(body, [" ", "- ", "* "])
        return cls(current, head), leftovers

    def _get_items(self, raw: str, head: dict) -> list[DocElement]:
        delims = ["- ", "* "]
        raw_items = []
        for line in raw.splitlines():
            if self.matches(line):
                raw_items.append(line)
            else:
                raw_items[-1] += "\n" + line
        return [ListItem(ri, head) for ri in raw_items]


class OrderedList(DocElement):

    _HTML_TAG = "ol"

    def __init__(self, raw, head):
        self._children = self._get_items(raw, head)

    def to_tex(self) -> str:
        return r"\begin{enumerate}" + "\n" + self._children_to_tex() + "\n" + r"\end{enumerate}"

    @classmethod
    def matches(cls, raw: str) -> bool:
        if not raw:
            return False
        first_word = raw.split(None, 1)[0]
        if first_word.endswith(".") or first_word.endswith(")"):
            return first_word[:-1].isdigit()
        else:
            return False

    @classmethod
    def get_with_leftovers(cls, raw: str, head: dict) -> tuple[DocElement, str]:
        # list continues as long as we see indented lines and lines starting with list markers
        leftover_lines = raw.splitlines()
        lines = [leftover_lines.pop(0)]
        while leftover_lines:
            line = leftover_lines[0]
            if line.startswith(" ") or cls.matches(line):
                lines.append(leftover_lines.pop(0))
            else:
                break
        return cls("\n".join(lines), head), "\n".join(leftover_lines)
    

    def _get_items(self, raw: str, head: dict) -> list[DocElement]:
        raw_items = []
        for line in raw.splitlines():
            if self.matches(line):
                raw_items.append(line)
            else:
                raw_items[-1] += "\n" + line
        return [ListItem(ri, head) for ri in raw_items]


class ListItem(DocElement):

    _HTML_TAG = "li"

    def __init__(self, raw, head):
        # chop off the list item delimiter
        raw = raw.split(None, 1)[-1]
        # if this is a multi-line item, following lines are indented. chop
        # that off so we can identify nested stuff
        if "\n" in raw:
            lines = raw.splitlines()
            depth = len(lines[1]) - len(lines[1].lstrip())
            lines = lines[:1] + [l[depth:] for l in lines[1:]]
            raw = "\n".join(lines)

        # list items are usually just a line of text. but in principle one list
        # item can have multiple lines of text, code blocks, etc.
        self._children = get_children(raw, head)

    def to_tex(self):
        return r"\item " + self._children_to_tex() + "\n"


class CodeBlock(DocElement):

    def __init__(self, body, head):
        first_line, content = body.split("\n", 1)
        if "," in first_line:
            language, flags = first_line.split(",", 1)
        else:
            language, flags = first_line, None
        self._params = {"language": language or "text", "flags": flags}
        self._children.append(Literal(content, head))

    def to_tex(self) -> str:
        language = self._params["language"]
        content = self._children_to_tex()
        flags = self._params["flags"]
        if flags:
            return r"\begin{minted}[" + flags + "]{" + language + "}\n" + content + "\n" + r"\end{minted}"
        else:
            return r"\begin{minted}{" + language + "}\n" + content + "\n" + r"\end{minted}"

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
        return "<br \\>"
    
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


class TexBlock(DocElement):

    def __init__(self, raw, head):
        self._children.append(Literal(raw, head))

    def to_tex(self) -> str:
        return self._children_to_tex()

    @classmethod
    def matches(cls, raw: str) -> bool:
        return raw.startswith("$$$")

    @classmethod
    def get_with_leftovers(cls, raw: str, head: dict) -> tuple[Subsection, str]:
        assert cls.matches(raw)
        raw = raw.lstrip("$")
        assert "\n$$$" in raw
        body, leftovers = raw.split("\n$$$", 1)
        return cls(body, head), leftovers


class Paragraph(DocElement):

    def __init__(self, body, head):
        self._children.append(Literal(body, head))

    @classmethod
    def matches(cls, raw: str) -> bool:
        # this is the default that catches everything unmatched
        return True

    def to_tex(self):
        return self._children_to_tex()

    def to_html(self) -> str:
        return "<p>" + self._children_to_tex() + "</p>"

    @classmethod
    def get_with_leftovers(cls, raw: str, head: dict) -> tuple[Paragraph, str]:
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
    doc_element_types: list[DocElement] = [
        Section,
        Subsection,
        Subsubsection,
        CodeBlock,
        TexBlock,
        UnorderedList,
        OrderedList,
        EmptyLine,
    ]
    for elt_type in doc_element_types:
        if elt_type.matches(raw):
            return elt_type.get_with_leftovers(raw, head)
    # Paragraph is the catchall for anything that doesn't match elsewhere
    return Paragraph.get_with_leftovers(raw, head)


def indent(text, depth=2) -> str:
    return "\n".join(" "*depth + l for l in text.splitlines())


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