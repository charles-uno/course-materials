
all: final


final: grades.csv make_exams.py final.gen.tex
	./make_exams.py -g grades.csv final.gen.tex
	cd output && latexmk -pdf -interaction=nonstopmode -shell-escape *.tex
	cd output && rm -rf _minted* && latexmk -c *.tex
	cd output && pdfjam output/*.pdf --outfile output/final-joined-printme.pdf