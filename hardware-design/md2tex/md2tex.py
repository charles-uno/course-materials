#!/usr/bin/env python3

import argparse
import mistletoe
from mistletoe.latex_renderer import LaTeXRenderer
import os
import sys
import yaml


def main():
    args = parse_args()
    output_filename = os.path.splitext(args.markdown_file)[0] + ".tex"

    print(f"converting \033[96m{args.markdown_file}\033[0m -> \033[96m{output_filename}\033[0m ... ", end="")
    sys.stdout.flush()

    with open(output_filename, "w") as handle:
        handle.write(get_tex(args.markdown_file))

    print("\033[92mdone\033[0m")
    return


def get_tex(filename: str) -> list[str]:


    header, lines = get_header_and_lines(filename)



    chunks = get_chunks(lines)
    frame_markers = [
        r"\begin{frame}",
        r"\end{document}",
        r"\section{", 
        r"\Section{",
        r"\subsection{",
        r"\Subsection{",
    ]
    frames = [""]
    for c in chunks:
        if any(c.startswith(m) for m in frame_markers):
            frames.append(c)
        else:
            frames[-1] += "\n\n" + c

    # Add \end{frame} and [fragile] as appropriate
    frames = [fix_frame(f) for f in frames]
    return join_frames(frames)



def join_frames(frames: list[str]) -> str:
    ret = "\n\n".join(frames).lstrip().replace("\\item \n", "\\item ").replace("\n\n\\item", "\n\\item").replace("\n\n\\end", "\n\\end")
    while "\n\n\n" in ret:
        ret = ret.replace("\n\n\n", "\n\n")
    return ret


def get_chunks(lines: list[str]) -> list[str]:
    chunks = [""]
    tex_depth = 0
    code_block = False

    standalone_line_markers = [
        "# ",
        "## ",
        "### ",
        r"\includegraphics",
        "%",
    ]
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
        elif code_block:
            chunks[-1] += line
        elif any(line.startswith(m) for m in standalone_line_markers):
            chunks += [line, ""]
        else:
            chunks[-1] += line
    return [to_tex(c.rstrip()) for c in chunks]


def to_tex(chunk: str) -> str:
    tex_markers = [
        "%",
        r"\begin{",
        r"\end{",
        r"\documentclass{",
        r"\includegraphics"
    ]
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


def fix_frame(frame: str) -> str:
    if not frame.strip().startswith(r"\begin{frame}"):
        return frame
    if r"\begin{minted}" in frame or r"\verb" in frame:
        frame = frame.replace(r"\begin{frame}", r"\begin{frame}[fragile]")
    return frame + "\n\n" + r"\end{frame}"


def should_end_frame_before_chunk(tex_chunks: list[str], tex_chunk: str) -> bool:
    tex = "\n\n".join(tex_chunks)
    n_begin_frames = tex.count(r"\begin{frame}")
    n_end_frames = tex.count(r"\end{frame}")
    if n_begin_frames == n_end_frames:
        return False
    need_frame_closed = [
        r"\section{", 
        r"\Section{",
        r"\subsection{",
        r"\Subsection{",
        r"\begin{frame}",
        r"\end{document}",
    ]
    return any(tex_chunk.startswith(x) for x in need_frame_closed)


def get_section(chunk: str) -> str:
    assert chunk.startswith("# ")
    section_title = chunk[2:].splitlines()[0]
    return r"\Section{" + section_title + "}"


def get_subsection(chunk: str) -> str:
    assert chunk.startswith("## ")
    section_title = chunk[3:].splitlines()[0]
    return r"\Subsection{" + section_title + "}"


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


def get_header_and_lines(filename: str) -> tuple[dict, list[str]]:
    with open(filename, "r") as handle:
        lines = handle.readlines()
    header_lines = []
    while lines:
        line = lines.pop(0)
        if line.startswith("---"):
            break
        header_lines.append(line)
    if not lines:
        raise ParseFailure("expected yaml header")
    header = yaml.safe_load("".join(header_lines))
    return header, lines


def parse_args():
    parser = argparse.ArgumentParser(
        prog="md2tex",
        description="convert markdown to latex",
    )
    parser.add_argument("markdown_file", help="path to the input markdown file")
    return parser.parse_args()


class ParseFailure(Exception):
    pass


if __name__ == "__main__":
    main()
