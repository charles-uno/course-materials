.PHONY: all clean tidy

REPO_ROOT := $(shell git rev-parse --show-toplevel)
MD2TEX := $(REPO_ROOT)/hardware-design/build/md2tex/md2tex.py

# 1. Define separate lists of generated tex files
HOMEWORK_TEX := $(wildcard chapters/*/homework.md)
HOMEWORK_TEX := $(HOMEWORK_TEX:.md=.gen.tex)

SLIDES_TEX := $(wildcard chapters/*/slides.md)
SLIDES_TEX := $(SLIDES_TEX:.md=.gen.tex)

# 2. Shared build/report logic using variables (NAME is target-specific)
BUILD = pdflatex -interaction=nonstopmode -shell-escape $(NAME).tex >/dev/null
REPORT = if [[ -f $(NAME).pdf ]]; then echo "\033[92mdone\033[0m"; else \
         echo "\033[91mfailed\033[0m (see $(NAME).log)"; cat $(NAME).log; exit 1; fi

all: homework.pdf slides.pdf

# 3. Explicitly link each PDF to its specific sub-dependencies
homework.pdf: NAME := homework
homework.pdf: homework.tex $(HOMEWORK_TEX)
	@ printf "\033[95mbuilding $@... \033[0m"
	@ $(BUILD) ; $(BUILD) ; $(REPORT)

slides.pdf: NAME := slides
slides.pdf: slides.tex $(SLIDES_TEX)
	@ printf "\033[95mbuilding $@... \033[0m"
	@ $(BUILD) ; $(BUILD) ; $(REPORT)

# 4. Keep the generic rule for generating .tex from .md
%.gen.tex: %.md $(MD2TEX)
	@ $(MD2TEX) $<

clean: tidy
	@ rm -rf homework.pdf slides.pdf ||:

tidy: 
	@ rm -rf *.log *.aux *.toc *.nav *.out *.snm *.fdb_latex *.fls *.vrb _minted* *.data.minted *.fdb_latexmk *.cpt *.gen.tex */*.log */*.gen.tex */*/*.gen.tex ||:
