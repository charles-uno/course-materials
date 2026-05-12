#!/usr/bin/env python3

import argparse
import json
import mistletoe
from mistletoe.latex_renderer import LaTeXRenderer
import os
import re
import sys
import yaml


def main() -> int:
    md_path = get_md_path()
    tex_path = md_path.replace(".md", ".gen.tex")
    print(f"building \033[96m{md_path}\033[0m -> \033[96m{tex_path}\033[0m ... ", end="")
    sys.stdout.flush()

    doc = Document(md_path)

    print(repr(doc))

    with open(tex_path, "w") as handle:
        handle.write(str(doc))

    print("\033[92mdone\033[0m")

    return 0






class DocElement:

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        instance._params = {}
        instance._children = []
        return instance

    def _children_to_str(self) -> str:
        return "\n".join(str(c) for c in self._children)

    def to_dict(self) -> dict:
        return {
            "class": self.__class__.__name__,
            "params": self._params,
            "children": [c.to_dict() for c in self._children],
        }

    def __repr__(self) -> str:
        return json.dumps(self.to_dict(), indent=2)



class Section(DocElement):

    def __init__(self, raw, head):
        title, contents = get_title_and_contents(raw)
        self._params = {"title": title}
        self._children = get_children(contents, head)

    def __str__(self) -> str:
        return "\n" + r"\section{" + self._params["title"] + "}\n" + self._children_to_str()

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

    def __str__(self) -> str:
        return "\n" + r"\subsection{" + self._params["title"] + "}\n" + self._children_to_str()

    @classmethod
    def get_with_leftovers(cls, body: str, head: dict) -> tuple[Subsection, str]:
        # Section goes until the next section, next subsection, or the end of the doc
        current, leftovers = break_at_line_starting_with(body, ["## ", "# "])
        return cls(current, head), leftovers



class UnorderedList(DocElement):

    def __init__(self, raw, head):
        self._children = self._get_items(raw, head)

    def __str__(self) -> str:
        return r"\begin{itemize}" + "\n" + self._children_to_str() + "\n" + r"\end{itemize}"

    @classmethod
    def get_with_leftovers(cls, body: str, head: dict) -> tuple[Subsection, str]:
        # list continues as long as we see indented lines and lines starting with list markers
        # TODO: smarter indentation handling for nested lists
        current, leftovers = break_at_line_starting_without(body, [" ", "- ", "* "])
        return cls(current, head), leftovers

    def _get_items(self, body: str, head: dict) -> list[DocElement]:

        print("parsing list contents:", body)

        delims = ["- ", "* "]
        raw_bodies = []
        for line in body.splitlines():
            if any(line.startswith(d) for d in delims):
                print("new item", line)
                raw_bodies.append(line)
            else:
                print("continuing item", line)
                raw_bodies[-1] += "\n" + line
        return [UnorderedListItem(b, head) for b in raw_bodies]



class UnorderedListItem(DocElement):

    def __init__(self, raw, head):
        text = raw.split(None, 1)[-1]
        self._children = [Paragraph(text, head)]

    def __str__(self):
        return r"\item " + self._children_to_str() + "\n"



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


def get_next_and_leftovers(body: str, head: dict) -> tuple[DocElement, str]:
    while body.startswith("\n"):
        body = body[1:]
    if body.startswith("# "):
        return Section.get_with_leftovers(body, head)
    elif body.startswith("## "):
        return Subsection.get_with_leftovers(body, head)
    elif body.startswith("- ") or body.startswith("* "):
        return UnorderedList.get_with_leftovers(body, head)
    else:
        return Paragraph(body, head).get_with_leftovers(body, head)



class Paragraph(DocElement):

    def __init__(self, body, head):
        self._params = {"text": body}

    def __str__(self):
        return self._params["text"]

    @classmethod
    def get_with_leftovers(cls, body: str, head: dict) -> tuple[Subsection, str]:
        # empty line is a paragraph break
        leftover_lines = body.splitlines()
        lines = [leftover_lines.pop(0)]
        while leftover_lines:
            if not leftover_lines[0]:
                break
            lines.append(leftover_lines.pop(0))
        return cls("\n".join(lines), head), "\n".join(leftover_lines)



class Document(DocElement):

    def __init__(self, md_path: str):
        head, body = self._get_head_and_body(md_path)
        while body:
            next_elt, body = get_next_and_leftovers(body, head)
            self._children.append(next_elt)

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

    def __str__(self) -> str:
        return self._children_to_str()



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
    sys.exit(main())
