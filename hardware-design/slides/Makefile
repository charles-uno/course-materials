REPO_ROOT := $(shell git rev-parse --show-toplevel)
MD2TEX := $(REPO_ROOT)/hardware-design//md2tex/md2tex.py
BUILD_SLIDES := pdflatex -interaction=nonstopmode -shell-escape slides.tex

# call pdflatex twice to make sure the TOC is populated correctly
slides:
	@ $(MD2TEX) sections/*.md
	@ $(BUILD_SLIDES); $(BUILD_SLIDES); if [[ "$$?" == "0" ]]; then echo "\033[92mpdf build complete\033[0m"; else echo "\033[91mpdf build failed\033[0m"; fi
	
clean:
	rm -rf *.log *.aux *.toc *.log *.nav *.out *.snm *.pdf *.fdb_latex *.fls *.vrb _minted* *.data.minted *.fdb_latexmk *.cpt *.gen.tex sections/*.log sections/*.gen.tex ||:
