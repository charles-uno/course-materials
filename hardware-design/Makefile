.PHONY: all clean tidy

REPO_ROOT := $(shell git rev-parse --show-toplevel)
MD2TEX := $(REPO_ROOT)/hardware-design/build/md2tex/md2tex.py

HOMEWORK_TEX := $(wildcard chapters/*/homework.md)
HOMEWORK_TEX := $(HOMEWORK_TEX:.md=.gen.tex)

SLIDES_TEX := $(wildcard chapters/*/slides.md)
SLIDES_TEX := $(SLIDES_TEX:.md=.gen.tex)

BUILD = latexmk -pdf -interaction=nonstopmode -shell-escape -cd $(NAME)/*.tex >/dev/null
REPORT = if [[ -f $(NAME).pdf ]]; then echo "\033[92mdone\033[0m"; else \
         echo "\033[91mfailed\033[0m (see $(NAME).log)"; cat $(NAME).log; exit 1; fi


all: homework.pdf slides.pdf syllabus/syllabus.pdf

# target to build just the tex input
chapters: $(HOMEWORK_TEX) $(SLIDES_TEX)

homework.pdf: NAME := homework
homework.pdf: homework.tex $(HOMEWORK_TEX)
	@ printf "\033[95mbuilding $@... \033[0m"
	@ $(BUILD) ; $(REPORT)

slides.pdf: NAME := slides
slides.pdf: slides.tex $(SLIDES_TEX)
	@ printf "\033[95mbuilding $@... \033[0m"
	@ $(BUILD) ; $(REPORT)

syllabus/syllabus.pdf: NAME := syllabus
syllabus/syllabus.pdf: syllabus/syllabus.gen.tex
	@ printf "\033[95mbuilding $@... \033[0m"
	@ $(BUILD) ; $(REPORT)

%.gen.tex: %.md $(MD2TEX)
	@ $(MD2TEX) $<

clean: tidy
	@ git clean -fdX

tidy: 
	@ git clean -fdX -e "*.pdf"
