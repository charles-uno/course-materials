#!/bin/bash

# reverse path lookup. Much easier here than in the makefile
if [[ "$1" == artifacts/*.pdf && "$2" == "--get-md-path" ]]; then
	ARTIFACT_PATH="$1"
	NAME=$(basename "$ARTIFACT_PATH" | cut -d '.' -f 1)
	# no dashes: artifacts/syllabus.pdf -> syllabus/syllabus.pdf
	# at least one dash: artifacts/foo-bar-baz.pdf -> chapters/foo-bar/baz.pdf
	NAME_LAST_PART=$(echo "$NAME" | rev | cut -d '-' -f 1 | rev)
	if [[ "$NAME_LAST_PART" == "$NAME" ]]; then
		echo "$NAME/$NAME.md"
	else
		NAME_PREFIX=$(echo "$NAME" | rev | cut -d '-' -f 2- | rev)
		echo "chapters/$NAME_PREFIX/$NAME_LAST_PART.md"
	fi
	exit 0
fi

if [[ "$1" == artifacts/* || "$1" != *.md ]]; then
	echored "expected path to markdown input file"
	exit 1
fi

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

# path lookup for use in the makefile
if [[ "$2" == "--get-pdf-path" ]]; then
	echo "$ARTIFACT_PATH"
	exit 0
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
cp "$PDF_PATH" "$ARTIFACT_PATH"

echogreen "done\n"
