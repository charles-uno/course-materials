
all: final


final: grades.csv make_exams.py final.main.gen.tex
	./make_exams.py -g grades.csv final.main.gen.tex
	cd output && latexmk -pdf -interaction=nonstopmode -shell-escape *.tex
	cd output && rm -rf _minted* && latexmk -c *.tex
