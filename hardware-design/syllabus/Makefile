MD2TEX = ../build/md2tex/md2tex.py
TEX2PDF = ../build/tex2pdf.sh

all: syllabus.pdf

syllabus.pdf: syllabus.tex imports/syllabus.gen.tex
	@ $(TEX2PDF) syllabus.tex

imports/syllabus.gen.tex: imports/syllabus.md
	@ $(MD2TEX) imports/syllabus.md

clean:
	cd .. && $(MAKE) clean