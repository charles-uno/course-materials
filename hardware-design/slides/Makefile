.PHONY: slides sections clean tidy

REPO_ROOT := $(shell git rev-parse --show-toplevel)
MD2TEX := $(REPO_ROOT)/hardware-design//md2tex/md2tex.py
BUILD_SLIDES := pdflatex -interaction=nonstopmode -shell-escape slides.tex >/dev/null
REPORT_SLIDES := if [[ -f slides.pdf ]]; then echo "\033[92mdone\033[0m"; else echo "\033[91mfailed\033[0m (see slides.log)"; exit 1; fi

# call pdflatex twice to make sure the TOC is populated correctly
slides: sections
	@ printf "\033[95mpreliminary build for toc ... \033[0m"
	@ $(BUILD_SLIDES) ; $(REPORT_SLIDES)
	@ printf "\033[95mfinal build ... \033[0m"
	@ $(BUILD_SLIDES) ; $(REPORT_SLIDES)

sections: clean
	@ $(MD2TEX) sections/*.md

# remove output and generated/intermediate files
clean: tidy
	@ rm -rf *.pdf ||:

# remove generated/intermediate files
tidy: 
	@ rm -rf *.log *.aux *.toc *.log *.nav *.out *.snm *.fdb_latex *.fls *.vrb _minted* *.data.minted *.fdb_latexmk *.cpt *.gen.tex sections/*.log sections/*.gen.tex ||:

