#!/usr/bin/env python3

from argparse import ArgumentParser, Namespace
import csv
import os
import sys
from typing import Any

CSV_KEY_STANDARD_PREFIX = "Standard "
CSV_KEY_FIRST_NAME = "First name"
CSV_KEY_LAST_NAME = "Last name"


def main() -> int:
    args = parse_args()
    proficiency_map = get_proficiency_map(args.grades_path, args.proficiency_score)
    print(proficiency_map)


def get_proficiency_map(
    grades_path: str, proficiency_score: int
) -> dict[str, list[str]]:
    proficiency_map = {}
    with open(grades_path, "r") as handle:
        csv_lines = list(csv.reader(handle))
    column_names = csv_lines.pop(0)
    for line in csv_lines:
        student_map = dict(zip(column_names, line))
        student_name = (
            student_map[CSV_KEY_FIRST_NAME] + " " + student_map[CSV_KEY_LAST_NAME]
        )
        proficiency_map[student_name] = get_student_proficiencies(
            student_map, proficiency_score
        )
    return proficiency_map


def get_student_proficiencies(
    student_map: dict[str, Any], proficiency_score: int
) -> list[str]:
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
    return proficiencies


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
