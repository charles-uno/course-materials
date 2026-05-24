#!/bin/bash

set -e

mkdir -p artifacts
rm -r artifacts/*

for X in $(ls */*.pdf); do
    FILENAME=$(basename $X)
    printf "moving \033[35m$X\033[0m -> \033[35martifacts/$FILENAME\033[0m\n"
    cp "$X" artifacts/
done    

for X in $(ls chapters/*/*.pdf); do
    FILENAME_WITHOUT_EXT=$(basename "$X" | cut -d '.' -f 1)
    CHAPTERNAME=$(dirname $X | xargs basename)
    printf "moving \033[35m$X\033[0m -> \033[35martifacts/$FILENAME_WITHOUT_EXT-$CHAPTERNAME.pdf\033[0m\n"
    cp "$X" "artifacts/$FILENAME_WITHOUT_EXT-$CHAPTERNAME.pdf"
done


