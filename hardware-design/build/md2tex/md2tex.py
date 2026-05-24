#!/usr/bin/env python3

import argparse
import os
import sys
import yaml

import docparser
import helpers


def main() -> int:
    md_path = get_md_path()
    tex_path = md_path.replace(".md", ".gen.tex")
    print(f"building", helpers.blue(md_path), "->", helpers.blue(tex_path), "... ", end="")
    sys.stdout.flush()

    try:
        doc = docparser.Document(md_path)
    except docparser.ParseFailure as exc:
        print(helpers.red(exc))
        return 1

#    print(doc.to_html())

    with open(tex_path, "w") as handle:
        handle.write(doc.to_tex())

    print(helpers.green("done"))

    return 0



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