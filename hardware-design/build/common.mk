.DEFAULT_GOAL := all
.PHONY: all clean tidy
.SECONDARY:

BUILD_DIR := $(dir $(lastword $(MAKEFILE_LIST)))
MD2TEX    := $(BUILD_DIR)md2tex/md2tex.py
TEX2PDF   := $(BUILD_DIR)tex2pdf.sh

# Single source of truth for compiling any imported markdown fragment
../imports/%.gen.tex: ../imports/%.md
	@ $(MD2TEX) $<

# remove junk per the .gitignore
clean: tidy
	@ git clean -fdX

# remove junk per the .gitignore but leave the PDFs
tidy:
	@ git clean -fdX -e "*.pdf"
