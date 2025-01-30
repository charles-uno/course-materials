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
    output: str


def main() -> int:
    args = parse_args()
    try:
        build_run_and_check(args)
        print_with_color("ok", color="green")
        return 0
    except TestFailure as exc:
        print_with_color(str(exc), color="red")
        return 1


def print_with_color(*args, color=None):
    text = " ".join(args)
    if color == "green":
        print("\033[92m" + text + "\033[0m")
    elif color == "red":
        print("\033[31m" + text + "\033[0m")
    elif color == "magenta":
        print("\033[35m" + text + "\033[0m")
    elif color == "yellow":
        print("\033[93m" + text + "\033[0m")
    else:
        print(text + "\033[0m")


def build_run_and_check(args: TestArgs):
    if not os.path.isfile(args.src):
        raise TestFailure(f"input file not found: {args.src}")
    if os.path.isfile("a.out"):
        os.remove("a.out")
    sp.getoutput(f"gcc {args.src} -o a.out")
    if not os.path.isfile("a.out"):
        raise TestFailure("build failed")
    proc = sp.Popen(["./a.out"], stdout=sp.PIPE, stdin=sp.PIPE, stderr=sp.PIPE)
    # Watch out - subprocess uses bytes, not unicode strings
    if args.input is None:
        proc_reply = proc.communicate()
    else:
        proc_reply = proc.communicate(input=args.input.encode("ascii"))
    stdout = proc_reply[0].decode("utf-8")
    # Don't worry about trailing whitespace or newlines
    if stdout.rstrip() != args.output.rstrip():
        raise TestFailure(
            f"expected output '{args.output.rstrip()}' but got '{stdout.rstrip()}'"
        )
    if proc.return_code != 0:
        stderr = proc_reply[1].decode("utf-8").strip()
        if "\n" in stderr:
            stderr = stderr.splitlines()[0] + "..."
        raise TestFailure(
            f"got unexpected returncode {proc.return_code}, stderr: '{stderr}'"
        )


def parse_args() -> TestArgs:
    parser = argparse.ArgumentParser(description="test tool for arm v7 via gcc")
    parser.add_argument("src", help="name of the assembly file to build and test")
    # Note: no input is potentially different from empty string input
    parser.add_argument("-i", "--input", help="input string to provide to the program")
    parser.add_argument(
        "-o", "--output", help="expected output from the build program", default=""
    )
    args = parser.parse_args()
    # Use a daraclass for typing
    return TestArgs(
        src=args.src, input=vars(args).get("input"), output=vars(args).get("output")
    )


class TestFailure(Exception):
    pass


if __name__ == "__main__":
    sys.exit(main())
