.PHONY: all chapters clean tidy

# Now handles both targets
TARGETS := homework slides

MD_CHAPTERS := $(wildcard chapters/*/*.md)
# This generates .gen.tex for every .md file found
TEX_CHAPTERS := $(MD_CHAPTERS:.md=.gen.tex)

REPO_ROOT := $(shell git rev-parse --show-toplevel)
MD2TEX := $(REPO_ROOT)/hardware-design/build/md2tex/md2tex.py

# Build all targets by default
all: $(foreach t,$(TARGETS),$(t).pdf)

# Pattern rule for the PDFs
%.pdf: %.tex chapters
	@ printf "\033[95mbuilding $@... \033[0m"
	@ pdflatex -interaction=nonstopmode -shell-escape $*.tex >/dev/null ; \
	  pdflatex -interaction=nonstopmode -shell-escape $*.tex >/dev/null ; \
	  if [[ -f $@ ]]; then echo "\033[92mdone\033[0m"; else \
	  echo "\033[91mfailed\033[0m (see $*.log)"; cat $*.log; exit 1; fi

chapters: $(TEX_CHAPTERS)

# Static pattern rule: handles homework.gen.tex, slides.gen.tex, etc.
$(TEX_CHAPTERS): %.gen.tex: %.md $(MD2TEX)
	@ $(MD2TEX) $<

clean: tidy
	@ rm -rf $(foreach t,$(TARGETS),$(t).pdf) ||:

tidy: 
	@ rm -rf *.log *.aux *.toc *.nav *.out *.snm *.fdb_latex *.fls *.vrb _minted* *.data.minted *.fdb_latexmk *.cpt *.gen.tex */*.log */*.gen.tex */*/*.gen.tex ||:
