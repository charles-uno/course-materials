#!/usr/bin/env python3

import argparse
import os
import subprocess as sp
import sys
from typing import Optional
from dataclasses import dataclass


@dataclass
class TestArgs:
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
    if not os.path.isfile(args.src):
        raise TestFailure(f"input file not found: {args.src}")
    if os.path.isfile("a.out"):
        os.remove("a.out")
    sp.getoutput(f"gcc {args.src} -o a.out")
    if not os.path.isfile("a.out"):
        raise TestFailure("build failed")
    # Note: no input is potentially different from empty string input
    if input is None:
        stdout = sp.getoutput("./a.out")
    else:
        proc = sp.Popen(
            ["./a.out"], stdout=sp.PIPE, stdin=sp.PIPE, stderr=sp.PIPE, text=True
        )
        proc_reply = proc.communicate(input=args.input)
        stdout = proc_reply[0]
        return_code = proc_reply[2]
    if args.output and stdout != args.output:
        raise TestFailure(f"expected output '{args.output}' but got '{stdout}'")
    if return_code != 0:
        raise TestFailure(f"expected return code 0 but got '{return_code}'")


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
