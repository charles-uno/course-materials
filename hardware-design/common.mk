.PHONY: all sections clean tidy

MD_SECTIONS := $(wildcard sections/*.md)
TEX_SECTIONS := $(MD_SECTIONS:.md=.gen.tex)

REPO_ROOT := $(shell git rev-parse --show-toplevel)
MD2TEX := $(REPO_ROOT)/hardware-design//md2tex/md2tex.py

TARGET := $(notdir $(CURDIR))
BUILD := pdflatex -interaction=nonstopmode -shell-escape $(TARGET).tex >/dev/null
REPORT := if [[ -f $(TARGET).pdf ]]; then echo "\033[92mdone\033[0m"; else echo "\033[91mfailed\033[0m (see slides.log)"; cat slides.log; exit 1; fi

all: $(TARGET).pdf

$(TARGET).pdf: $(TARGET).tex sections
	@ printf "\033[95mpreliminary build for toc ... \033[0m"
	@ $(BUILD) ; $(REPORT)
	@ printf "\033[95mfinal build ... \033[0m"
	@ $(BUILD) ; $(REPORT)

# generate tex source then stop. in case the python and latex builds need to happen in different containers
sections: $(TEX_SECTIONS)

sections/%.gen.tex: sections/%.md $(MD2TEX)
	@ $(MD2TEX) $<

# remove output and generated/intermediate files
clean: tidy
	@ rm -rf *.pdf ||:

# remove generated/intermediate files
tidy: 
	@ rm -rf *.log *.aux *.toc *.log *.nav *.out *.snm *.fdb_latex *.fls *.vrb _minted* *.data.minted *.fdb_latexmk *.cpt *.gen.tex sections/*.log sections/*.gen.tex ||:

