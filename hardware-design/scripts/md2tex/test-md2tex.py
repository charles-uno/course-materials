#!/usr/bin/env python3

import argparse
import os
import subprocess as sp
import sys

import helpers


def main():
    path = get_path()
    test_case_name = path.split("/")[-1].split(".md")[0]

    print(f"testing", helpers.blue(test_case_name), "... ", end="")
    returncode = run_md2tex(path)
    if returncode != 0:
        print(helpers.red("build failed"))
        return
    result = check_output(path)
    if result == "ok":
        print(helpers.green("ok"))
    else:
        print(helpers.red(result))


def run_md2tex(path):
    return sp.run(["./md2tex.py", path], capture_output=True).returncode


def check_output(input_path):
    output_path = input_path.replace(".md", ".gen.tex")
    if not os.path.isfile(output_path):
        return "build failed"
    expected_path = input_path.replace(".md", ".tex")
    if not os.path.isfile(expected_path):
        return "missing " + expected_path
    actual_output = read_file(output_path)
    expected_output = read_file(expected_path)
    if not expected_output:
        return "empty " + expected_path
    if is_consistent(expected_output, actual_output):
        return "ok"
    else:
        return "output does not match"


def is_consistent(expected: str, actual: str) -> bool:
    actual_leftovers = actual
    for i, expected_line in enumerate(expected.splitlines()):
        expected_line_nospace = expected_line.replace(" ", "")
        actual_line, actual_leftovers = split_at_n_real_chars(actual_leftovers, len(expected_line_nospace))
        actual_line_nospace = actual_line.replace(" ", "").replace("\n", "")

        if actual_line_nospace != expected_line_nospace:

            print("mismatch on line", i)
            print("expected:", expected_line.replace("\n", ""))
            print("actual:  ", actual_line)


            return False
    return True

def split_at_n_real_chars(text, n):
    chunk_chars = []
    leftover_chars = list(text)
    while leftover_chars and real_char_count(chunk_chars) < n:
        chunk_chars.append(leftover_chars.pop(0))
    return "".join(chunk_chars), "".join(leftover_chars)

def real_char_count(chars: list[str]):
    return len("".join(chars).replace(" ", "").replace("\n", ""))





                  
def squish(text: str) -> str:
    return text.replace(" ", "").replace("\n", "")


def read_file(path):
    with open(path, "r") as handle:
        return handle.read()


def get_path():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "md_path", help="path to the input markdown file"
    )
    return parser.parse_args().md_path


if __name__ == "__main__":
    sys.exit(main())