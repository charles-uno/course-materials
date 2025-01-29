#!/usr/bin/env python3

import argparse
import os
import subprocess as sp
import sys
from typing import Optional, TypedDict


class TestArgs(TypedDict):
    src: str
    input: Optional[str]
    output: Optional[str]


def main() -> int:
    args = parse_args()
    try:
        build_run_and_check(args)
        return 0
    except TestFailure as exc:
        print(exc)
        return 1


def build_run_and_check(args: TestArgs):
    src = args["src"]
    input = args["input"]
    output = args["output"]
    if not os.path.isfile(src):
        raise TestFailure(f"input file not found: {src}")
    if os.path.isfile("a.out"):
        os.remove("a.out")
    sp.getoutput(f"gcc {src} -o a.out")
    if not os.path.isfile("a.out"):
        raise TestFailure("build failed")
    # Note: no input is potentially different from empty string input
    if input is None:
        stdout = sp.getoutput("./a.out")
    else:
        proc = sp.Popen(
            ["./a.out"], stdout=sp.PIPE, stdin=sp.PIPE, stderr=sp.PIPE, text=True
        )
        stdout = proc.communicate(input=input)[0]
    if stdout != output:
        raise TestFailure(f"expected output '{output}' but got '{stdout}'")


def parse_args() -> TestArgs:
    parser = argparse.ArgumentParser(description="test tool for arm v7 via gcc")
    parser.add_argument("src", help="name of the assembly file to build and test")
    parser.add_argument("-i", "--input", help="input string to provide to the program")
    parser.add_argument("-o", "--output", help="expected output from the build program")
    return vars(parser.parse_args())


class TestFailure(Exception):
    pass


if __name__ == "__main__":
    sys.exit(main())
