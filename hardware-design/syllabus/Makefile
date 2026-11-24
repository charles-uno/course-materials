include ../build/common.mk

IMPORT_DIR = ../imports/syllabus

all: syllabus.pdf

syllabus.pdf: syllabus.tex $(VARS_TEX) $(IMPORT_DIR)/syllabus.gen.tex
	@ $(TEX2PDF) syllabus.tex
