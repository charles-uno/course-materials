#!/usr/bin/env python3

"""
Accepts the path to a LaTeX file, the source for an exam. Creates a
directory of new LaTeX files, one personalized to each student. 

Student names and standards are loaded from grades.csv, the exported grades
from Moodle. LaTeX files are then modified according to inline annotation:

1. The student's name is swapped in for %NAME. 
2. If the student has already demonstrated proficiency in the standard FOO,
   omit all content between %BEGIN_FOO and %END_FOO. 
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

OUTPUT_DIR = "make_exams_output"


@dataclass(frozen=True)
class Student:
    name: str
    proficiencies: frozenset[str]


def main() -> int:
    args = parse_args()
    students = get_students(args.grades_path, args.proficiency_score)
    for student in students:
        create_exam(args.exam_path, student)
    return 0


def create_exam(exam_path: str, student: Student) -> None:
    with open(exam_path, "r") as handle:
        exam_source = "".join(handle.readlines())
    exam_source = exam_source.replace(TEX_NAME, student.name)
    for p in student.proficiencies:
        begin_macro = TEX_STANDARD_BEGIN + p
        end_macro = TEX_STANDARD_END + p
        if exam_source.count(begin_macro) != 1 or exam_source.count(end_macro) != 1:
            raise AmbiguousAnnotation(f"ambiguous annotation for standard {p}")
        before = exam_source.split(begin_macro)[0]
        after = exam_source.split(end_macro)[-1]
        exam_source = before + after
    # If the student is already proficient in all standards, don't bother
    # creating an exam
    if TEX_STANDARD_BEGIN not in exam_source:
        print("SKIP", student.name)
        return
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    output_path = os.path.join(OUTPUT_DIR, slug(student.name) + ".tex")
    with open(output_path, "w") as handle:
        handle.write(exam_source)
        print("OK", student.name)
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


class MissingSubstitution(Exception):
    pass


class AmbiguousAnnotation(Exception):
    pass


if __name__ == "__main__":
    sys.exit(main())
