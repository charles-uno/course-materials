.PHONY: all chapters clean tidy

TARGET := homework

MD_CHAPTERS := $(wildcard chapters/*/*.md)
TEX_CHAPTERS := $(MD_CHAPTERS:.md=.gen.tex)

REPO_ROOT := $(shell git rev-parse --show-toplevel)
MD2TEX := $(REPO_ROOT)/hardware-design//md2tex/md2tex.py

BUILD := pdflatex -interaction=nonstopmode -shell-escape $(TARGET).tex >/dev/null
REPORT := if [[ -f $(TARGET).pdf ]]; then echo "\033[92mdone\033[0m"; else echo "\033[91mfailed\033[0m (see $(TARGET).log)"; cat $(TARGET).log; exit 1; fi

$(TARGET).pdf: $(TARGET).tex chapters
	@ printf "\033[95mbuilding $(TARGET)... \033[0m"
	@ $(BUILD) ; $(BUILD) ; $(REPORT)

chapters: $(TEX_CHAPTERS)

chapters/%/homework.gen.tex: chapters/%/homework.md $(MD2TEX)
	@ $(MD2TEX) $<

# remove output and generated/intermediate files
clean: tidy
	@ rm -rf *.pdf ||:

# remove generated/intermediate files
tidy: 
	@ rm -rf *.log *.aux *.toc *.log *.nav *.out *.snm *.fdb_latex *.fls *.vrb _minted* *.data.minted *.fdb_latexmk *.cpt *.gen.tex */*.log */*.gen.tex */*/*.gen.tex ||:

