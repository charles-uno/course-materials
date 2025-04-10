#!/usr/bin/env python3

"""
Student names and standards are loaded from the Moodle grades CSV. Then the
exam source is personalized according to inline annotation:

1. The student's name is swapped in for %NAME.
2. If the student has completed standard FOO, omit from %BEGIN_STANDARD_FOO to %END_STANDARD_FOO.

Finally, the personalized source files are compiled to PDFs.
"""

from argparse import ArgumentParser, Namespace
import csv
from dataclasses import dataclass
import os
import random
import subprocess
import sys
from typing import Any, Optional

CSV_KEY_STANDARD_PREFIX = "Standard "
CSV_KEY_FIRST_NAME = "First name"
CSV_KEY_LAST_NAME = "Last name"
CSV_KEY_EMAIL = "Email address"
CSV_KEY_SECTION = "Section"

TEX_NAME = "%NAME"
TEX_STANDARD_BEGIN = "%BEGIN_STANDARD_"
TEX_STANDARD_END = "%END_STANDARD_"
TEX_STANDARDS = "%STANDARDS"

OUTPUT_DIR = "output"


@dataclass(frozen=True)
class Student:
    name: str
    username: str
    standards_completed: frozenset[str]
    section: Optional[str]


def main() -> int:
    args = parse_args()
    raw_exam = get_raw_exam(args.exam_path)
    students = get_students(args.grades_path, args.completion_threshold)

    if args.debug:
        students = [random.choice(students)]

    for student in students:
        create_exam(raw_exam, student)

    return 0


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

    remaining_standards = [
        x.split("_")[-1]
        for x in exam_source.split()
        if x.startswith(TEX_STANDARD_BEGIN)
    ]
    remaining_standards_pretty = ", ".join(remaining_standards)
    exam_source = exam_source.replace(TEX_STANDARDS, remaining_standards_pretty)

    if not remaining_standards:
        print(
            student.name,
            "(all standards complete)",
        )
        return
    print(
        student.name,
        ":",
        remaining_standards_pretty,
    )
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # usernames should be safe from collisions and special characters
    tex_path = os.path.join(OUTPUT_DIR, student.username + ".tex")
    with open(tex_path, "w") as handle:
        handle.write(exam_source)
    subprocess.run(
        [
            "pdflatex",
            f"-output-directory={OUTPUT_DIR}",
            tex_path,
        ],
        capture_output=True,
    )
    return


def get_students(grades_path: str, completion_threshold: int) -> list[Student]:
    students = []
    with open(grades_path, "r") as handle:
        csv_lines = list(csv.reader(handle))
    column_names = csv_lines.pop(0)
    for line in csv_lines:
        student_map = dict(zip(column_names, line))
        name = student_map[CSV_KEY_FIRST_NAME] + " " + student_map[CSV_KEY_LAST_NAME]
        username = student_map[CSV_KEY_EMAIL].split("@")[0]
        section = student_map.get(CSV_KEY_SECTION, "").upper()
        standards_completed = get_standards_completed(student_map, completion_threshold)
        students.append(
            Student(
                name=name,
                username=username,
                standards_completed=standards_completed,
                section=section,
            )
        )
    return students


def get_standards_completed(
    student_map: dict[str, Any], completion_threshold: int
) -> frozenset[str]:
    standards_completed = []
    for key, val in student_map.items():
        if not key.startswith(CSV_KEY_STANDARD_PREFIX):
            continue
        standard_short_name = key.split(CSV_KEY_STANDARD_PREFIX)[-1].split()[0]
        try:
            v = float(val)
        except ValueError:
            continue
        if v >= completion_threshold:
            standards_completed.append(standard_short_name)
    return frozenset(standards_completed)


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
        "-d",
        "--debug",
        action="store_true",
        help="do one student at random instead of them all",
    )
    parser.add_argument(
        "-c",
        "--completion_threshold",
        default=100,
        help="score that indicates completion of a standard",
    )
    return parser.parse_args()


class AmbiguousAnnotation(Exception):
    pass


if __name__ == "__main__":
    sys.exit(main())
