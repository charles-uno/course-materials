MD2TEX = ../build/md2tex/md2tex.py
TEX2PDF = ../build/tex2pdf.sh
IMPORT_DIR = ../imports/syllabus

all: syllabus.pdf

syllabus.pdf: syllabus.tex $(IMPORT_DIR)/syllabus.gen.tex
	@ $(TEX2PDF) syllabus.tex

$(IMPORT_DIR)/syllabus.gen.tex: $(IMPORT_DIR)/syllabus.md
	@ $(MD2TEX) $(IMPORT_DIR)//syllabus.md

clean:
	cd .. && $(MAKE) clean