#!/bin/bash

set -e

if [[ -d artifacts ]]; then rm -r artifacts; fi
mkdir -p artifacts

for X in $(ls */*.pdf); do
    FILENAME=$(basename $X)
    printf "moving \033[35m$X\033[0m -> \033[35martifacts/$FILENAME\033[0m\n"
    cp "$X" artifacts/
done

for X in $(ls chapters/*/*.pdf); do
    FILENAME=$(basename "$X")
    CHAPTERNAME=$(dirname $X | xargs basename)
#    INITIALS=$(echo "$CHAPTERNAME" | sed -E 's/([a-zA-Z])[a-zA-Z]*-?/\1/g')
    NEW_FILENAME="$CHAPTERNAME-$FILENAME"
    printf "moving \033[35m$X\033[0m -> \033[35martifacts/$NEW_FILENAME\033[0m\n"
    cp "$X" "artifacts/$NEW_FILENAME"
done


