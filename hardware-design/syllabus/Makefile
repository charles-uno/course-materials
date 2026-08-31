MD2TEX = ../build/md2tex/md2tex.py
TEX2PDF = ../build/tex2pdf.sh

all: syllabus.pdf

syllabus.pdf: syllabus.tex syllabus.gen.tex
	@ $(TEX2PDF) syllabus.tex

syllabus.gen.tex: syllabus.md
	@ $(MD2TEX) syllabus.md
