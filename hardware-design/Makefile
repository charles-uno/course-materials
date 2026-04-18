.PHONY: all clean tidy

MD2TEX := build/md2tex.py

# some markdown files turn into standalone tex docs
MD_MAIN := $(shell find * -mindepth 1 -name "*.main.md")
TEX_MAIN := $(MD_MAIN:.md=.gen.tex)

# some markdown files generate content to be imported
MD_INCL := $(wildcard chapters/*/*.incl.md)
MD_INCL := $(MD_INCL:.md=.gen.tex)

# some manual tex docs to import the above
MANUAL_TEX := $(shell find . -name "*.tex" ! -name "*.gen.*")

PDFS := $(MANUAL_TEX:.tex=.pdf) $(MD_MAIN:.main.md=.pdf)


define build_latex
	$(eval BASE := $(notdir $(1)))
	@printf "\033[35mbuilding $(1).pdf from $(2)... \033[0m"
	@latexmk -silent -pdf -jobname=$(BASE) -interaction=nonstopmode -shell-escape -cd $(2) >/dev/null 2>&1; \
	if [ -f $(1).pdf ]; then \
		printf "\033[92mdone\033[0m\n"; \
		latexmk -c -jobname=$(BASE) -cd -e '$$clean_ext = "nav snm vrb"' $(2) >/dev/null 2>&1; \
	else \
		printf "\033[31mfailed\033[0m (see $(1).log)\n"; \
		[ -f $(1).log ] && cat $(1).log; exit 1; \
	fi
endef


all: $(PDFS)

%.pdf: %.tex $(INCL_TEX)
	@$(call build_latex,$*,$<)

%.pdf: %.main.gen.tex
	@$(call build_latex,$*,$<)

%.gen.tex: %.md $(MD2TEX)
	@$(MD2TEX) $<

# remove junk per the .gitignore
clean: tidy
	@ git clean -fdX

# remove junk per .gitignore but leave the PDFs
tidy: 
	@ git clean -fdX -e "*.pdf"




