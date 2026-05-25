#!/bin/bash

set -e

INPUT_PATH="$1"
DIR=$(dirname "$INPUT_PATH")
JOB_NAME=$(basename "$INPUT_PATH" | cut -d '.' -f 1)
PDF_PATH="$DIR/$JOB_NAME.pdf"

printf "building \033[35m$INPUT_PATH\033[0m -> \033[35m$PDF_PATH\033[0m ... "

# so we can import from the templates directory as well as the build directory
REPO_ROOT=$(git rev-parse --show-toplevel)
export TEXINPUTS=".:$REPO_ROOT/hardware-design/build/templates/:"

# NOTE: -cd is important here. If we cd to that directory explicitly, the
# minted lexer runs into name collisions with temporary generated files
latexmk -silent -pdf -jobname="$JOB_NAME" -cd -interaction=nonstopmode -shell-escape "$INPUT_PATH" >/dev/null 2>&1

if [ -f "$PDF_PATH" ]; then
	printf "\033[92mdone\033[0m\n"
	latexmk -c -jobname="$JOB_NAME" -e '$$clean_ext = "nav snm vrb"' "$INPUT_NAME" >/dev/null 2>&1
else
	printf "\033[31mfailed\033[0m (see $DIR/$JOB_NAME.log)\n"
	[ -f "$DIR/$JOB_NAME.log" ] && cat "$DIR/$JOB_NAME.log"; exit 1
fi

# consolidate artifacts into one directory for convenience
# projects, syllabus, etc: foo/foo.pdf -> artifacts/foo.pdf
# slides, homework, etc: chapters/foo/bar.pdf -> artifaacts/foo-bar.pdf

if [[ "$DIR" == chapters/* ]]; then
	# chapters/foo/bar.pdf -> artifacts/foo-bar.pdf (slides, homework, etc)
	CHAPTER_NAME=$(basename "$DIR")
	ARTIFACT_NAME="artifacts/$CHAPTER_NAME-$JOB_NAME.pdf"
else
	# foo/foo.pdf -> artifacts/foo.pdf (syllabus, project, etc)
	ARTIFACT_NAME="artifacts/$JOB_NAME.pdf"
fi

mkdir -p artifacts
printf "moving \033[35m$PDF_PATH\033[0m -> \033[35m$ARTIFACT_NAME\033[0m\n"
cp "$PDF_PATH" "$ARTIFACT_NAME"
