#!/bin/bash

set -e

DIR=$(dirname "$1")
INPUT_NAME=$(basename "$1")
JOB_NAME=$(echo "$INPUT_NAME" | cut -d '.' -f 1)
PDF_NAME="$DIR/$JOB_NAME.pdf"

printf "building \033[35m$DIR/$INPUT_NAME\033[0m -> \033[35m$PDF_NAME\033[0m ... "

HOME=$(pwd)
cd "$DIR"

latexmk -silent -pdf -jobname="$JOB_NAME" -interaction=nonstopmode -shell-escape "$INPUT_NAME" >/dev/null 2>&1

if [ -f "$JOB_NAME.pdf" ]; then
	printf "\033[92mdone\033[0m\n"
	latexmk -c -jobname="$JOB_NAME" -e '$$clean_ext = "nav snm vrb"' "$INPUT_NAME" >/dev/null 2>&1
else
	printf "\033[31mfailed\033[0m (see $DIR/$JOB_NAME.log)\n"
	[ -f "$JOB_NAME.log" ] && cat "$JOB_NAME.log"; exit 1
fi

# consolidate artifacts into one directory for convenience
# projects, syllabus, etc: foo/foo.pdf -> artifacts/foo.pdf
# slides, homework, etc: chapters/foo/bar.pdf -> artifaacts/foo-bar.pdf
cd "$HOME"

if [[ "$DIR" == chapters/* ]]; then
	# chapters/foo/bar.pdf -> artifacts/foo-bar.pdf (slides, homework, etc)
	CHAPTERNAME=$(basename "$DIR")
	FILENAME=$(basename "$X")
	ARTIFACT_NAME="artifacts/$CHAPTERNAME-$FILENAME.pdf"
else
	# foo/foo.pdf -> artifacts/foo.pdf (syllabus, project, etc)
	ARTIFACT_NAME="artifacts/$JOB_NAME.pdf"
fi

mkdir -p artifacts
printf "moving \033[35m$PDF_NAME\033[0m -> \033[35martifacts/$ARTIFACT_NAME\033[0m\n"
cp "$PDF_NAME" "$ARTIFACT_NAME"
