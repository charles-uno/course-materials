#!/bin/bash

set -e

DIR=$(dirname "$1")
INPUT_NAME=$(basename "$1")
JOB_NAME=$(echo "$INPUT_NAME" | cut -d '.' -f 1)

printf "building \033[35m$DIR/$INPUT_NAME\033[0m -> \033[35m$DIR/$JOB_NAME.pdf\033[0m ... "

cd "$DIR"

latexmk -silent -pdf -jobname="$JOB_NAME" -interaction=nonstopmode -shell-escape "$INPUT_NAME" >/dev/null 2>&1

if [ -f "$JOB_NAME.pdf" ]; then
	printf "\033[92mdone\033[0m\n"
	latexmk -c -jobname="$JOB_NAME" -e '$$clean_ext = "nav snm vrb"' "$INPUT_NAME" >/dev/null 2>&1
else
	printf "\033[31mfailed\033[0m (see $DIR/$JOB_NAME.log)\n"
	[ -f "$JOB_NAME.log" ] && cat "$JOB_NAME.log"; exit 1
fi