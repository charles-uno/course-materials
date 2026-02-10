#!/usr/bin/env python3

import mistletoe
from mistletoe.latex_renderer import LaTeXRenderer
import os
import subprocess


SOURCE_DIR = "source"
BUILD_DIR = "build"
BUILD_FILENAME = os.path.join(BUILD_DIR, "slides.tex")


def main():

    if os.path.isfile(BUILD_FILENAME):
        os.remove(BUILD_FILENAME)

    template = get_template()
    before, after = template.split("% BUILD_HERE", 1)
    write_tex(before)

    write_tex_from_md()

    write_tex(after)


def write_tex_from_md():
    md_paths = get_paths()
    for p in md_paths:
        write_tex(get_tex_from_md_file(p))


def get_tex_from_md_file(filename: str) -> str:
    with open(filename, "r") as handle:
        md_lines = handle.readlines()
    md_chunks = [""]
    while md_lines:
        if md_lines[0].startswith("#"):
            md_chunks.append(md_lines.pop(0))
        else:
            md_chunks[-1] += md_lines.pop(0)
    tex_chunks = []
    for md_chunk in md_chunks:
        tex_chunks.append(get_tex_chunk_from_md_chunk(md_chunk))
    return "\n\n".join(tex_chunks)


def get_tex_chunk_from_md_chunk(md_chunk: str) -> str:
    if md_chunk.startswith("# "):
        return get_section(md_chunk)
    elif md_chunk.startswith("## "):
        return get_subsection(md_chunk)
    elif md_chunk.startswith("### "):
        frame_title = md_chunk[4:].splitlines()[0].strip()
        frame_content = md_chunk.split("\n", 1)[-1].strip()
        return (
            r"\begin{frame}{" + frame_title + "}\n" + get_tex_from_md_within_frame(frame_content) + "\n" + r"\end{frame}" + "\n"
        )
    elif not md_chunk.strip():
        return ""
    else:
        raise ParseFailure("not sure how to handle:" + repr(md_chunk))


def get_section(md_h1: str) -> str:
    section_title = md_h1[2:].splitlines()[0]
    return "\n" + r"\Section{" + section_title + "}"


def get_subsection(md_h2: str) -> str:
    section_title = md_h2[3:].splitlines()[0]
    return "\n" + r"\Subsection{" + section_title + "}"


def get_tex_from_md_within_frame(md_text: str) -> str:
    with LaTeXRenderer() as renderer:
        tex_document = renderer.render(mistletoe.Document(md_text))
    # these are chunks in an existing document. remove packages, doc boundaries
    to_skip = [
        r"\documentclass",
        r"\begin{document}", 
        r"\end{document}", 
        r"\usepackage"
    ]
    tex_lines = []
    for line in tex_document.splitlines():
        if not any(x in line for x in to_skip):
            tex_lines.append(line)
    return "\n".join(tex_lines)


def get_template() -> str:
    with open(f"{SOURCE_DIR}/template.tex", "r") as handle:
        return "".join(handle.readlines())


def get_paths() -> list[str]:
    paths = []
    for filename in os.listdir(SOURCE_DIR):
        if filename.endswith(".md"):
            paths.append(f"{SOURCE_DIR}/{filename}")
    return paths


def write_tex(text: str) -> None:

    print(text)

    os.makedirs(BUILD_DIR, exist_ok=True)
    with open(BUILD_FILENAME, "a") as handle:
        handle.write(text)


def build() -> None:
    subprocess.run(["pdflatex", "-interaction=nonstopmode", "-shell-escape", BUILD_FILENAME]) 


class ParseFailure(Exception):
    pass



if __name__ == "__main__":
    main()
