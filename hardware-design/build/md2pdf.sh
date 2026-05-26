#!/bin/bash

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

echogreen() {
	printf "\033[0;32m%b\033[0m" "$*"
}

echored() {
	printf "\033[0;31m%b\033[0m" "$*"
}

echopurp() {
	printf "\033[0;35m%b\033[0m" "$*"
}

printf "building $(echopurp $MD_PATH) -> $(echopurp $ARTIFACT_PATH) ... "

./build/md2tex/md2tex.py "$MD_PATH" > "$DIR/$JOB_NAME.md2tex" 2>&1
if [[ "$?" != "0" ]]; then
	echored "md parse failed\n"
	cat "$DIR/$JOB_NAME.md2tex"
	exit 1
fi

./build/tex2pdf.sh "$TEX_PATH" > /dev/null 2>&1
if [[ ! -f "$PDF_PATH" ]]; then
	echored "tex build failed\n"
	cat "$DIR/$JOB_NAME.log" | grep -E -A 5 "^\!.*|^l\.[0-9]+"
	exit 1
fi

mkdir -p artifacts
mv "$PDF_PATH" "$ARTIFACT_PATH"

echogreen "done\n"
