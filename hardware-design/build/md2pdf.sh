#!/bin/bash

set -e

MD_PATH="$1"
DIR=$(dirname "$MD_PATH")
JOB_NAME=$(basename "$MD_PATH" | cut -d '.' -f 1)
TEX_PATH="$DIR/$JOB_NAME.gen.tex"
PDF_PATH="$DIR/$JOB_NAME.pdf"

if [[ "$DIR" == chapters/* ]]; then
	# chapters/foo/bar.pdf -> artifacts/foo-bar.pdf (slides, homework, etc)
	CHAPTER_NAME=$(basename "$DIR")
	ARTIFACT_PATH="artifacts/$CHAPTER_NAME-$JOB_NAME.pdf"
else
	# foo/foo.pdf -> artifacts/foo.pdf (syllabus, project, etc)
	ARTIFACT_PATH="artifacts/$JOB_NAME.pdf"
fi

printf "building \033[35m$MD_PATH\033[0m -> \033[35m$ARTIFACT_PATH\033[0m ... "

REPO_ROOT=$(git rev-parse --show-toplevel)
cd "$REPO_ROOT/hardware-design"

FAILURE=""

./build/md2tex/md2tex.py "$MD_PATH" > /dev/null 2>&1
if [[ "$?" != "0" ]]; then FAILURE="md parse failed: ./build/md2tex/md2tex.py $MD_PATH"; fi

./build/tex2pdf.sh "$TEX_PATH" > /dev/null
if [[ ! -f "$PDF_PATH" ]]; then FAILURE="tex build failed: ./build/tex2pdf.sh $TEX_PATH"; fi

if [[ "$FAILURE" != "" ]]; then
	printf "\033[31m$FAILURE\033[0m\n"
	exit 1
else
	printf "\033[92mdone\033[0m\n"
fi

mkdir -p artifacts
mv "$PDF_PATH" "$ARTIFACT_PATH"

