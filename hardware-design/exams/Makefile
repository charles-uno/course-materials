
all: final.pdf test1.pdf test2.pdf test3.pdf test4.pdf

%.pdf: %.tex helpers.sty
	pdflatex -interaction=nonstopmode -shell-escape $<
	pdflatex -interaction=nonstopmode -shell-escape $<

clean:
	rm -rf *.log *.aux *.toc *.log *.nav *.out *.snm *.fdb_latex *.fls *.vrb _minted* *.data.minted *.fdb_latexmk ||:
