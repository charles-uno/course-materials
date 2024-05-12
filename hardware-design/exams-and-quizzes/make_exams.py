#!/usr/bin/env python3

"""
Accepts the path to a LaTeX file, the source for an exam. Creates a
directory of new LaTeX files, one for each student. Student exams are
personalized by omitting any standard where that student has already
demonstrated proficiency. 

Proficiency is judged according to grades.csv, the grades exported from Moodle.

Content is then omitted according to inline annotation in the LaTeX source. For
example, if a student has shown proficiency in the "MD" standard, it'll chop
out anything between the following two lines:
% BEGIN_MD
% END_MD
"""

from argparse import ArgumentParser, Namespace
import csv
from dataclasses import dataclass
import sys
from typing import Any, TypedDict

CSV_KEY_STANDARD_PREFIX = "Standard "
CSV_KEY_FIRST_NAME = "First name"
CSV_KEY_LAST_NAME = "Last name"


def main() -> int:
    args = parse_args()
    students = get_students(args.grades_path, args.proficiency_score)
    for student in students:
        print(student)


@dataclass(frozen=True)
class Student:
    name: str
    proficiencies: frozenset[str]


def get_students(grades_path: str, proficiency_score: int) -> list[Student]:
    students = []
    with open(grades_path, "r") as handle:
        csv_lines = list(csv.reader(handle))
    column_names = csv_lines.pop(0)
    for line in csv_lines:
        student_map = dict(zip(column_names, line))
        name = student_map[CSV_KEY_FIRST_NAME] + " " + student_map[CSV_KEY_LAST_NAME]
        proficiencies = get_student_proficiencies(student_map, proficiency_score)
        students.append(Student(name=name, proficiencies=proficiencies))
    return students


def get_student_proficiencies(
    student_map: dict[str, Any], proficiency_score: int
) -> frozenset[str]:
    proficiencies = []
    for key, val in student_map.items():
        if not key.startswith(CSV_KEY_STANDARD_PREFIX):
            continue
        standard_short_name = key.split(CSV_KEY_STANDARD_PREFIX)[-1].split()[0]
        try:
            v = float(val)
        except ValueError:
            continue
        if v >= proficiency_score:
            proficiencies.append(standard_short_name)
    return frozenset(proficiencies)


def parse_args() -> Namespace:
    parser = ArgumentParser(
        prog="make_exams",
        description="generate personalized exams, skipping standards where a student has already demonstrated proficiency",
    )
    parser.add_argument("exam_path", help="path to the annotated TEX exam file")
    parser.add_argument(
        "-g", "--grades_path", default="grades.csv", help="path to the CSV grades file"
    )
    parser.add_argument(
        "-p", "--proficiency_score", default=50, help="score that indicates proficiency"
    )
    return parser.parse_args()


if __name__ == "__main__":
    sys.exit(main())
