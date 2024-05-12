#!/usr/bin/env python3

"""
Accepts the path to a LaTeX file, the source for an exam. Creates a
directory of new LaTeX files, one personalized to each student. 

Student names and standards are loaded from grades.csv, the exported grades
from Moodle (plain text format). LaTeX files are then modified according to
inline annotation:

1. The student's name is swapped in for %NAME. 
2. If the student has completed standard FOO, omit from %BEGIN_FOO to %END_FOO.
"""

from argparse import ArgumentParser, Namespace
import csv
from dataclasses import dataclass
import os
import sys
from typing import Any

CSV_KEY_STANDARD_PREFIX = "Standard "
CSV_KEY_FIRST_NAME = "First name"
CSV_KEY_LAST_NAME = "Last name"

TEX_NAME = "%NAME"
TEX_STANDARD_BEGIN = "%BEGIN_"
TEX_STANDARD_END = "%END_"

OUTPUT_DIR = "output"


@dataclass(frozen=True)
class Student:
    name: str
    standards_completed: frozenset[str]


def main() -> int:
    args = parse_args()
    raw_exam = get_raw_exam(args.exam_path)
    students = get_students(args.grades_path, args.completion_threshold)
    for student in students:
        create_exam(raw_exam, student)
    show_next_step()
    return 0


def show_next_step() -> None:
    print("\nNow to generate PDFs, run:")
    print(
        blue(
            "    pushd output && for SRC in *.tex; do pdflatex $SRC; done; rm *.aux *.log *.out; popd"
        )
    )


def create_exam(exam_source: str, student: Student) -> None:
    exam_source = exam_source.replace(TEX_NAME, student.name)
    for s in student.standards_completed:
        begin_macro = TEX_STANDARD_BEGIN + s
        end_macro = TEX_STANDARD_END + s
        if exam_source.count(begin_macro) != 1 or exam_source.count(end_macro) != 1:
            raise AmbiguousAnnotation(f"ambiguous annotation for standard {s}")
        before = exam_source.split(begin_macro)[0]
        after = exam_source.split(end_macro)[-1]
        exam_source = before + after
    # sanity check: how many standards does this student have left?
    n_standards_remaining = exam_source.count(TEX_STANDARD_BEGIN)
    if not n_standards_remaining:
        print(
            n_standards_remaining,
            "standards remaining for",
            student.name,
            "(no exam needed)",
        )
        return
    print(n_standards_remaining, "standards remaining for", student.name)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    output_path = os.path.join(OUTPUT_DIR, slug(student.name) + ".tex")
    with open(output_path, "w") as handle:
        handle.write(exam_source)
    return


def slug(name: str) -> str:
    # "normalize" the name so we can use it for a file path
    substitutions = {"é": "e"}
    chars = []
    for c in name.lower():
        if c == " " or c.isalnum:
            chars.append(c)
        elif c in substitutions:
            chars.append(substitutions[c])
        else:
            raise MissingSubstitution(f"please add handling for: {c}")
    return "".join(chars).replace(" ", "-")


def get_students(grades_path: str, completion_threshold: int) -> list[Student]:
    students = []
    with open(grades_path, "r") as handle:
        csv_lines = list(csv.reader(handle))
    column_names = csv_lines.pop(0)
    for line in csv_lines:
        student_map = dict(zip(column_names, line))
        name = student_map[CSV_KEY_FIRST_NAME] + " " + student_map[CSV_KEY_LAST_NAME]
        standards_completed = get_standards_completed(student_map, completion_threshold)
        students.append(Student(name=name, standards_completed=standards_completed))
    return students


def get_standards_completed(
    student_map: dict[str, Any], completion_threshold: int
) -> frozenset[str]:
    get_standards_completed = []
    for key, val in student_map.items():
        if not key.startswith(CSV_KEY_STANDARD_PREFIX):
            continue
        standard_short_name = key.split(CSV_KEY_STANDARD_PREFIX)[-1].split()[0]
        try:
            v = float(val)
        except ValueError:
            continue
        if v >= completion_threshold:
            get_standards_completed.append(standard_short_name)
    return frozenset(get_standards_completed)


def get_raw_exam(exam_path: str) -> str:
    with open(exam_path, "r") as handle:
        return "".join(handle.readlines())


def parse_args() -> Namespace:
    parser = ArgumentParser(
        prog="make_exams",
        description="generate personalized exams, skipping completed standards",
    )
    parser.add_argument("exam_path", help="path to the annotated TEX exam file")
    parser.add_argument(
        "-g", "--grades_path", default="grades.csv", help="path to the CSV grades file"
    )
    parser.add_argument(
        "-c",
        "--completion_threshold",
        default=50,
        help="score that indicates completion of a standard",
    )
    return parser.parse_args()


def blue(text: str) -> str:
    return f"\u001b[34m{text}\u001b[0m"


class MissingSubstitution(Exception):
    pass


class AmbiguousAnnotation(Exception):
    pass


if __name__ == "__main__":
    sys.exit(main())
