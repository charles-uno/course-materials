#!/usr/bin/env python3

import argparse
import mistletoe
from mistletoe.latex_renderer import LaTeXRenderer
import os
import re
import sys
import yaml


def main() -> int:
    args = parse_args()
    header, lines = get_header_and_lines(args.md_path)
    # .main.md turns into a standalone tex doc
    # .incl.md turns into content to be imported
    is_marked_main = args.md_path.endswith(".main.md")
    has_template = header.get("template", False)
    if is_marked_main and not has_template:
        print(f"\033[91mmissing template in {args.md_path}\033[0m")
        return 1
    if has_template and not is_marked_main:
        print(f"\033[91munexpected template in {args.md_path}\033[0m")
        return 1
    output_path = args.md_path.replace(".md", ".gen.tex")
    print(f"building \033[96m{args.md_path}\033[0m -> \033[96m{output_path}\033[0m ... ", end="")
    sys.stdout.flush()



    tex = md_to_tex(header, lines)
    print(tex)

    print("\033[92mdone\033[0m")



    return 0


def get_frames(header: dict, lines: list[str]) -> list[str]:
    frames = []
    while lines:
        frame, lines = get_next_frame(header, lines)
        frames.append(frame)
    return frames


def get_next_frame(header: dict, lines: list[str]) -> tuple[str, list[str]]:
    # always at least one line
    frame = lines.pop(0)
    while lines and not lines[0].startswith("#"):
        frame += "\n" + lines.pop(0)
    return frame, lines



FRAME_MARKERS = [
    r"\begin{frame}",
    r"\end{document}",
    r"\section{", 
    r"\Section{",
    r"\subsection{",
    r"\Subsection{",
    # just in case we split into frames before translating
    "#",
]





def md_to_tex(lines: list[str], **kwargs) -> str:
    if md.startswith("# "):
        return get_h1(md, **kwargs)
    elif md.startswith("## "):
        return get_h2(md, **kwargs)





    return md





def get_h1(md: str, **kwargs) -> str:
    is_beamer = kwargs.get("beamer", False)
    assert md.startswith("# ")
    title = md[2:].splitlines()[0]
    if is_beamer:
        head = r"\Section{" + title + "}"
    else:
        head = r"\section{" + title + "}"
    body = "\n".join(md.splitlines()[1:])
    return head + "\n\n" + md_to_tex(body)


def get_h2(md: str, **kwargs) -> str:
    is_beamer = kwargs.get("beamer", False)
    assert md.startswith("## ")
    title = md[3:].splitlines()[0]
    if is_beamer:
        head = r"\Subsection{" + title + "}"
    else:
        head = r"\subsection{" + title + "}"
    body = "\n".join(md.splitlines()[1:])
    return head + "\n\n" + md_to_tex(body)









def get_header_and_lines(filename: str) -> tuple[dict, list[str]]:
    with open(filename, "r") as handle:
        lines = [x.rstrip() for x in handle.readlines()]
    header_lines = []
    while lines:
        line = lines.pop(0)
        if line.startswith("---"):
            break
        header_lines.append(line)
    if not lines:
        raise ParseFailure("expected yaml header")
    header = yaml.safe_load("\n".join(header_lines)) or {}
    return header, lines


def md_path(path):
    if not os.path.exists(path):
        raise argparse.ArgumentTypeError(f"input path '{path}' does not exist")
    if not path.endswith('.md'):
        raise argparse.ArgumentTypeError(f"input path '{path}' must end in .md")
    return path


def parse_args():
    parser = argparse.ArgumentParser(
        prog="md2tex",
        description="convert markdown to latex",
    )
    parser.add_argument(
        "md_path", type=md_path, help="path to the input markdown file"
    )
    return parser.parse_args()


class ParseFailure(Exception):
    pass


if __name__ == "__main__":
    sys.exit(main())
