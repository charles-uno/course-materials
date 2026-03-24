.PHONY: all clean tidy

REPO_ROOT := $(shell git rev-parse --show-toplevel)
MD2TEX := $(REPO_ROOT)/hardware-design/build/md2tex/md2tex.py

HOMEWORK_TEX := $(wildcard chapters/*/homework.md)
HOMEWORK_TEX := $(HOMEWORK_TEX:.md=.gen.tex)

SLIDES_TEX := $(wildcard chapters/*/slides.md)
SLIDES_TEX := $(SLIDES_TEX:.md=.gen.tex)

BUILD = latexmk -pdf -interaction=nonstopmode -shell-escape -cd $(NAME)*.tex >/dev/null
REPORT = if [[ -f $(NAME)*.pdf ]]; then echo "\033[92mdone\033[0m"; else \
         echo "\033[91mfailed\033[0m (see $(NAME).log)"; cat $(NAME)*.log; exit 1; fi

define build_latex
	@# 1. Determine the source: .gen.tex if it exists, else .tex
	$(eval SRC := $(shell [ -f $(1).gen.tex ] && echo $(1).gen.tex || echo $(1).tex))
	@# 2. Extract just the filename (e.g., 'bar' from 'foo/bar')
	$(eval BASE := $(notdir $(1)))
	@# 3. Extract the directory (e.g., 'foo' from 'foo/bar')
	$(eval DIR := $(or $(dir $(1)), .))
	@printf "\033[35mbuilding $(1).pdf from $(SRC)... \033[0m"
	@# -cd changes to the directory of the file
	@# -jobname=$(BASE) ensures it's 'bar.pdf' even if input is 'bar.gen.tex'
	@latexmk -pdf -silent -jobname=$(BASE) -interaction=nonstopmode -shell-escape -cd $(SRC) >/dev/null ; \
	if [ -f $(1).pdf ]; then \
		echo "\033[32mdone\033[0m"; \
		latexmk -c -jobname=$(BASE) -cd -e '$$clean_ext = "nav snm vrb"' $(SRC) >/dev/null; \
	else \
		echo "\033[31mfailed\033[0m (see $(1).log)"; \
		cat $(1).log; exit 1; \
	fi
endef


# all: syllabus/syllabus.pdf homework.pdf slides.pdf 
all: homework.pdf slides.pdf 

# target to build just the tex input
chapters: $(HOMEWORK_TEX) $(SLIDES_TEX)

homework.pdf: homework.tex $(HOMEWORK_TEX)
	@ $(call build_latex,homework)

slides.pdf: slides.tex $(SLIDES_TEX)
	@ $(call build_latex,slides)

syllabus/syllabus.pdf: syllabus/syllabus.gen.tex
	@ $(call build_latex,syllabus/syllabus)

%.gen.tex: %.md $(MD2TEX)
	@ $(MD2TEX) $<

# remove junk per the .gitignore
clean: tidy
	@ git clean -fdX

# remove junk per .gitignore but leave the PDFs
tidy: 
	@ git clean -fdX -e "*.pdf"




