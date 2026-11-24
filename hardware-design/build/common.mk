.DEFAULT_GOAL := all
.PHONY: all clean tidy
.SECONDARY:

BUILD_DIR := $(dir $(lastword $(MAKEFILE_LIST)))
MD2TEX    := $(BUILD_DIR)md2tex/md2tex.py
TEX2PDF   := $(BUILD_DIR)tex2pdf.sh
VARS2TEX  := $(BUILD_DIR)vars2tex.py
VARS_YAML := $(BUILD_DIR)../vars.yaml
VARS_TEX  := $(BUILD_DIR)templates/vars.gen.tex

$(VARS_TEX): $(VARS_YAML) $(VARS2TEX)
	@ python3 $(VARS2TEX) $(VARS_YAML) $(VARS_TEX)

# Single source of truth for compiling any imported markdown fragment
../imports/%.gen.tex: ../imports/%.md
	@ $(MD2TEX) $<

# remove junk per the .gitignore
clean: tidy
	@ git clean -fdX

# remove junk per the .gitignore but leave the PDFs
tidy:
	@ git clean -fdX -e "*.pdf"
