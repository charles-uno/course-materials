#!/usr/bin/env python3

import argparse
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

    with open(tex_path, "w") as handle:
        handle.write(str(doc))

    print("\033[92mdone\033[0m")

    return 0






class DocElement:
    _params: dict = {}
    _children: list[DocElement] = []

    def _children_to_str(self) -> str: 
        return "\n" + "".join(str(c) for c in self._children)



def get_next_and_leftovers(body: str, head: dict) -> tuple[DocElement, str]:
    if body.startswith("# "):
        return Section.get_with_leftovers(body, head)



    else:
        return Text(body, head), ""


class Section(DocElement):

    def __init__(self, raw_body, head):
        title, body = raw_body.split("\n", 1)
        title = title[2:]
        self._params = {"title": title}
        self._children = []
        while body:
            next_elt, body = get_next_and_leftovers(body, head)
            self._children.append(next_elt)

    def __str__(self):
        parts = r"\section{" + self._params["title"] + "}" + self._children_to_str()

    @classmethod
    def get_with_leftovers(cls, body: str, head: dict) -> tuple[Section, str]:
        # Section goes until the next section or the end of the doc
        section, leftovers = body.split("\n# ", 1)
        return Section(section, head), leftovers



class Text(DocElement):

    def __init__(self, body, head):
        self._params = {"text": body}

    def __str__(self):
        return self._params["text"]


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
