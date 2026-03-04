REPO_ROOT := $(shell git rev-parse --show-toplevel)
MD2TEX := $(REPO_ROOT)/hardware-design//md2tex/md2tex.py


slides:
	$(MD2TEX) sections/00-introduction.md
	$(MD2TEX) sections/01-data-representation.md
	pdflatex -interaction=nonstopmode -shell-escape slides.tex

clean:
	rm -rf *.log *.aux *.toc *.log *.nav *.out *.snm *.pdf *.fdb_latex *.fls *.vrb _minted* *.data.minted *.fdb_latexmk *.cpt *.gen.tex sections/*.log sections/*.gen.tex ||:
