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

    chunks = [get_head()]
    paths = get_paths()
    for p in paths:
        chunks += get_chunks(p)
    chunks.append(get_tail())

    for chunk in chunks:
        if not chunk.strip():
            continue
        print("% --------------------")
        print(to_tex(chunk))


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




def get_chunks(filename: str) -> list[str]:
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
    if chunk.startswith("# "):
        return get_section(chunk)
    elif chunk.startswith("## "):
        return get_subsection(chunk)
    elif chunk.startswith("### "):
        return get_begin_frame(chunk)
    elif chunk.startswith("```"):
        # mistletoe doesn't handle code blocks nicely
        return get_code_block(chunk)
    elif chunk.lstrip().startswith(r"\begin"):
        # Tolerate LaTeX blocks within the Markdown 
        return chunk

    else:
        return md_to_tex(chunk)


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










def write_tex_from_md():
    md_paths = get_paths()
    for p in md_paths:
        write_tex(get_tex_from_md_file(p))


def get_tex_from_md_file(filename: str) -> str:
    chunks = get_chunks(filename)


    tex_chunks = []
    for md_chunk in chunks:
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


def get_tex_from_md_within_frame(md_text: str) -> str:
    with LaTeXRenderer() as renderer:
        tex_document = renderer.render(mistletoe.Document(md_text))
    # these are chunks in an existing document. remove packages, doc boundaries
    to_skip = [
        r"\documentclass",
        r"\begin{document}", 
        r"\end{document}", 
        r"\usepackage",
        r"lstlisting"
    ]
    tex_lines = []
    for line in tex_document.splitlines():
        if not any(x in line for x in to_skip):
            tex_lines.append(line)
    return "\n".join(tex_lines)


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


def write_tex(text: str) -> None:

    print(text)

    os.makedirs(BUILD_DIR, exist_ok=True)
    with open(BUILD_FILENAME, "a") as handle:
        handle.write(text)


def build() -> None:
    subprocess.run(["pdflatex", "-interaction=nonstopmode", "-shell-escape", BUILD_FILENAME]) 


def read_file(path: str) -> str:
    with open(path, "r") as handle:
        return "".join(handle.readlines())


class ParseFailure(Exception):
    pass


if __name__ == "__main__":
    main()
