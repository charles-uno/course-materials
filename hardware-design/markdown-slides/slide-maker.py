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

    raw_chunks = [get_head()]
    paths = get_paths()
    for p in paths:
        raw_chunks += get_raw_chunks(p)
    raw_chunks.append(get_tail())

    tex_chunks = []
    for raw_chunk in raw_chunks:
        if not raw_chunk.strip():
            continue
        tex_chunk = to_tex(raw_chunk)
        if should_end_frame_before_chunk(tex_chunks, tex_chunk):
            tex_chunks.append(get_end_frame())
        tex_chunks.append(tex_chunk)

    for tex_chunk in tex_chunks:
        print("% --------------------")
        print(tex_chunk)


    write_tex("\n\n".join(tex_chunks))


        # section header
        # subsection header
        # begin frame
        # markdown content (need to process)
        # LaTeX content (pass through)
        # close existing frame before starting a new section/subsection/frame


    return


    write_tex(get_head())
    write_tex_from_md()
    write_tex(get_tail())




def get_raw_chunks(filename: str) -> list[str]:
    lines = read_file(filename).splitlines()
    chunks = [""]
    tex_depth = 0
    code_block = False
    while lines:
        line = lines.pop(0) + "\n"
        if chunks[-1] == "" and not line.strip():
            continue

        elif line.strip().startswith(r"\begin{"):
            if tex_depth > 0:
                chunks[-1] += line
            else:
                chunks.append(line)
            tex_depth += 1
        elif line.strip().startswith(r"\end{"):
            chunks[-1] += line
            tex_depth -= 1
            if tex_depth == 0:
                chunks.append("")
        elif line.strip().startswith("```"):
            if code_block:
                chunks[-1] += line
                chunks.append("")
            else:
                chunks.append(line)                
            code_block = not code_block
        elif line.startswith("#") and line.lstrip("#").startswith(" "):
            chunks += [line, ""]
        else:
            chunks[-1] += line
    return [c.rstrip() for c in chunks]


def to_tex(chunk: str) -> str:
    tex_markers = [r"\begin{", r"\end{", r"\documentclass{"]
    if chunk.startswith("# "):
        return get_section(chunk)
    elif chunk.startswith("## "):
        return get_subsection(chunk)
    elif chunk.startswith("### "):
        return get_begin_frame(chunk)
    elif chunk.startswith("```"):
        # mistletoe doesn't handle code blocks nicely
        return get_code_block(chunk)
    elif any(chunk.lstrip().startswith(m) for m in tex_markers):
        # LaTeX just gets passed along
        return chunk
    else:
        return md_to_tex(chunk)


def should_end_frame_before_chunk(tex_chunks: list[str], tex_chunk: str) -> bool:
    tex = "\n\n".join(tex_chunks)
    n_begin_frames = tex.count(r"\begin{frame}")
    n_end_frames = tex.count(r"\end{frame}")
    if n_begin_frames == n_end_frames:
        return False
    need_frame_closed = [r"\section{", r"\Section", r"\subsection", r"\Subsection", r"\begin{frame}", r"\end{document}"]
    return any(tex_chunk.startswith(x) for x in need_frame_closed)


def get_section(chunk: str) -> str:
    assert chunk.startswith("# ")
    section_title = chunk[2:].splitlines()[0]
    return "\n" + r"\Section{" + section_title + "}"


def get_subsection(chunk: str) -> str:
    assert chunk.startswith("## ")
    section_title = chunk[3:].splitlines()[0]
    return "\n" + r"\Subsection{" + section_title + "}"


def get_code_block(chunk: str) -> str:
    lines = chunk.splitlines()[:-1]
    language = lines.pop(0)[3:]
    content = "\n".join(lines)
    return r"\begin{minted}{" + language + "}\n" + content + "\n" + r"\end{minted}"


def get_begin_frame(chunk: str) -> str:
    assert chunk.startswith("### ")
    frame_title = chunk[4:].splitlines()[0]
    return r"\begin{frame}{" + frame_title + "}"


def get_end_frame() -> str:
    return r"\end{frame}"


def md_to_tex(md_text: str) -> str:
    with LaTeXRenderer() as renderer:
        tex_document = renderer.render(mistletoe.Document(md_text))
    # these are chunks in an existing document. remove packages, doc boundaries
    to_skip = [
        r"\documentclass",
        r"\begin{document}", 
        r"\end{document}", 
        r"\usepackage",
        "lstlisting"
    ]
    tex_lines = []
    for line in tex_document.splitlines():
        if not any(x in line for x in to_skip):
            tex_lines.append(line)
    return "\n".join(tex_lines)    


def write_tex(text: str) -> None:
    os.makedirs(BUILD_DIR, exist_ok=True)
    with open(BUILD_FILENAME, "a") as handle:
        handle.write(text)


def get_head() -> str:
    with open(f"{SOURCE_DIR}/head.tex", "r") as handle:
        return "".join(handle.readlines())


def get_tail() -> str:
    with open(f"{SOURCE_DIR}/tail.tex", "r") as handle:
        return "".join(handle.readlines())


def get_paths() -> list[str]:
    paths = []
    for filename in os.listdir(SOURCE_DIR):
        if filename.endswith(".md"):
            paths.append(f"{SOURCE_DIR}/{filename}")
    return paths


def read_file(path: str) -> str:
    with open(path, "r") as handle:
        return "".join(handle.readlines())


class ParseFailure(Exception):
    pass


if __name__ == "__main__":
    main()
