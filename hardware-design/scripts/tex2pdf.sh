#!/bin/bash

set -e

INPUT_PATH="$1"
DIR=$(dirname "$INPUT_PATH")
JOB_NAME=$(basename "$INPUT_PATH" | cut -d '.' -f 1)
PDF_PATH="$DIR/$JOB_NAME.pdf"

printf "building \033[35m$INPUT_PATH\033[0m -> \033[35m$PDF_PATH\033[0m ... "

# so we can import from the templates directory
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
export TEXINPUTS=".:$ROOT_DIR/templates/:"

# NOTE: it's important that we run from a parent directory with -cd rather than
# move to the working directory. The minted lexer will try to import temporary
# generated files and get confused
if texfot latexmk -silent -halt-on-error -pdf -jobname="$JOB_NAME" -cd -interaction=nonstopmode -shell-escape "$INPUT_PATH" > /dev/null 2>&1; then
	# if the build was successful, clean up temporary files
	printf "\033[92mdone\033[0m\n"
	latexmk -c -cd -jobname="$JOB_NAME" -e '$clean_ext = "nav snm vrb"' "$INPUT_PATH" >/dev/null 2>&1
	rm -rf "$DIR/_minted-$JOB_NAME"
else
	# if the build failed, leave temporary files in place for debugging
	printf "\033[31mfailed\033[0m\n"
	if [ -f "$DIR/$JOB_NAME.log" ]; then
		cat "$DIR/$JOB_NAME.log" | texfot
	fi
	exit 1
fi
