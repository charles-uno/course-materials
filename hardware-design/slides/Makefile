REPO_ROOT := $(shell git rev-parse --show-toplevel)
MD2TEX := $(REPO_ROOT)/hardware-design//md2tex/md2tex.py


slides:
	$(MD2TEX) 00-introduction.md
	pdflatex -interaction=nonstopmode -shell-escape slides.tex

clean:
	rm -rf *.log *.aux *.toc *.log *.nav *.out *.snm *.pdf *.fdb_latex *.fls *.vrb _minted* *.data.minted *.fdb_latexmk *.cpt ||:
