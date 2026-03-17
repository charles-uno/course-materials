#!/usr/bin/env python3

import argparse
import mistletoe
from mistletoe.latex_renderer import LaTeXRenderer
import os
import re
import sys
import yaml


def main():
    args = parse_args()
    max_path_length = max(len(p) for p in args.md_paths)
    for md_path in args.md_paths:
        output_path = md_path.replace(".md", ".gen.tex")

        print(f"\033[96m{md_path.ljust(max_path_length)}\033[0m -> \033[96m{output_path.ljust(max_path_length+5)}\033[0m ... ", end="")
        sys.stdout.flush()

        with open(output_path, "w") as handle:
            handle.write(get_tex(md_path))

        print("\033[92mdone\033[0m")
    return


def get_tex(filename: str) -> list[str]:
    header, lines = get_header_and_lines(filename)

    chunks = get_chunks(lines, **header)

    # fix formatting for beamer builds
    frames = chunks_to_frames(chunks)
    return join_pretty(frames)


def chunks_to_frames(chunks: list[str]) -> list[str]:
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
    return [fix_frame(f) for f in frames]


def join_pretty(chunks: list[str]) -> str:
    ret = "\n\n".join(chunks).lstrip().replace("\\item \n", "\\item ").replace("\n\n\\item", "\n\\item").replace("\n\n\\end", "\n\\end")
    while "\n\n\n" in ret:
        ret = ret.replace("\n\n\n", "\n\n")

    # find urls starting with http(s), avoid those already in brackets or parens
    url_pattern = r'(?<![\{\[\(])(https?:\/\/[^\s<>]+)(?![\}\]\)])'
    # wrap in \url for nicer formatting
    ret = re.sub(url_pattern, r'\\url{\1}', ret)
    return ret


def get_chunks(lines: list[str], **kwargs) -> list[str]:

    chunks = []
    while lines:
        chunk, lines = get_next_chunk(lines)
        if chunk:
            chunks.append(chunk)
    return [to_tex(c.rstrip(), **kwargs) for c in chunks]


def get_next_chunk(lines: list[str]) -> tuple[str, list[str]]:
    standalone_markers = [
        "# ",
        "## ",
        "### ",
        "%",
        "|||"
    ]
    fence_markers = [
        "```",
        "$$$",
    ]
    # always process at least one line per call
    line = lines.pop(0)
    # empty lines
    if not line.strip():
        return "", lines
    # section headers, comments
    if any(line.startswith(m) for m in standalone_markers):
        return line, lines
    # fenced code blocks or tex blocks
    for m in fence_markers:
        if line.startswith(m):
            chunk = line
            while lines:
                next_line = lines.pop(0)
                chunk += "\n" + next_line
                if next_line.startswith(m):
                    return chunk, lines
    # Everything else just gets clumped and sent to the md parser
    chunk = line
    markers = standalone_markers + fence_markers
    while lines:
        if any(lines[0].startswith(m) for m in markers):
            break
        chunk += "\n" + lines.pop(0)
    return chunk, lines


def to_tex(chunk: str, **kwargs) -> str:
    is_beamer = kwargs.get("beamer", False)
    if chunk.startswith("# "):
        return get_h1(chunk, is_beamer)
    elif chunk.startswith("## "):
        return get_h2(chunk, is_beamer)
    elif chunk.startswith("### "):
        # for beamer builds, h3 is new frame
        return get_h3(chunk, is_beamer)
    elif chunk.startswith("```"):
        # mistletoe doesn't handle code blocks nicely
        return get_code_block(chunk, is_beamer=is_beamer)
    elif chunk.startswith("$$$"):
        # pass along fenced tex block
        return get_tex_block(chunk)
    elif chunk.startswith("%"):
        # pass along comment
        return chunk
    else:
        return md_to_tex(chunk)


def fix_frame(frame: str) -> str:
    if not frame.strip().startswith(r"\begin{frame}"):
        return frame
    if r"\begin{minted}" in frame or r"\verb" in frame:
        frame = frame.replace(r"\begin{frame}", r"\begin{frame}[fragile]")
    frame += "\n\n" + r"\end{frame}"
    # pipe fencing is for multicolumn. can explicitly specify columns or just
    # make a multicolumn environment
    if frame.count("|||") == 3:
        frame = frame.replace("|||", r"\bigskip\begin{columns}\begin{column}{0.5\textwidth}", 1)
        frame = frame.replace("|||", r"\end{column}\begin{column}{0.5\textwidth}", 1)
        frame = frame.replace("|||", r"\end{column}\end{columns}\bigskip", 1)
    elif frame.count("|||") == 2:
        frame = frame.replace("|||", r"\bigskip\begin{multicols}{2}", 1)
        frame = frame.replace("|||", r"\end{multicols}\bigskip", 1)
    elif frame.count("|||") != 0:
        frame_title = frame.splitlines()[0].split("### ")[-1]
        raise ParseFailure(f"ambiguous multicolumn setup after '{frame_title}'")
    return frame

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


def get_h1(chunk: str, is_beamer: bool) -> str:
    assert chunk.startswith("# ")
    title = chunk[2:].splitlines()[0]
    if is_beamer:
        return r"\Section{" + title + "}"
    else:
        return r"\section{" + title + "}"


def get_h2(chunk: str, is_beamer: bool) -> str:
    assert chunk.startswith("## ")
    title = chunk[3:].splitlines()[0]
    if is_beamer:
        return r"\Subsection{" + title + "}"
    else:
        return r"\subsection{" + title + "}"


def get_h3(chunk: str, is_beamer: bool) -> str:
    assert chunk.startswith("### ")
    title = chunk[4:].splitlines()[0]
    if is_beamer:
        return r"\begin{frame}{" + title + "}"
    else:
        return r"\subsubsection{" + title + "}"


def get_code_block(chunk: str, is_beamer: bool) -> str:
    lines = chunk.splitlines()[:-1]
    language = lines.pop(0)[3:]
    if "," in language:
        language, flags = language.split(",", 1)
    else:
        flags = ""
    content = "\n".join(lines)
    if not language:
        language = "text"
    if flags:
        ret = r"\begin{minted}[" + flags + "]{" + language + "}\n" + content + "\n" + r"\end{minted}"
    else:
        ret = r"\begin{minted}{" + language + "}\n" + content + "\n" + r"\end{minted}"
    # for more than a handful of lines, use two columns
    if is_beamer and content.count("\n") > 13:
        ret = r"\begin{multicols}{2}" + "\n" + r"{\small" + "\n" + ret + "\n}\n" + r"\end{multicols}"
    if is_beamer and content.count("\n") > 50:
        ret = ret.replace(r"\small", r"\tiny")
    return ret

def get_tex_block(chunk: str) -> str:
    return "\n".join(chunk.splitlines()[1:-1])


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
        "md_paths", nargs="+", type=md_path, help="path(s) to the input markdown file(s)"
    )
    return parser.parse_args()


class ParseFailure(Exception):
    pass


if __name__ == "__main__":
    main()
