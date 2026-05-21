#!/usr/bin/env python3

import argparse
import os
import subprocess as sp
import sys


def main():
    path = get_path()
    test_case_name = path.split("/")[-1].split(".md")[0]

    print(f"testing \033[96m{test_case_name}\033[0m ... ", end="")
    run_md2tex(path)
    result = check_output(path)
    if result == "ok":
        print("\033[92mok\033[0m")
    else:
        print(f"\033[91m{result}\033[0m")


def run_md2tex(path):
    sp.run(["./md2tex_new.py", path], capture_output=True)


def check_output(input_path):
    output_path = input_path.replace(".md", ".gen.tex")
    if not os.path.isfile(output_path):
        return "build failed"
    expected_path = output_path.replace(".gen.tex", ".expected.tex")
    if not os.path.isfile(expected_path):
        return "missing expected output"
    actual_output = read_file(output_path)
    expected_output = read_file(expected_path)
    if is_consistent(expected_output, actual_output):
        return "ok"
    else:
        return "fail"


def is_consistent(expected: str, actual: str) -> bool:
    return squish(expected) == squish(actual)
                  
                  
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