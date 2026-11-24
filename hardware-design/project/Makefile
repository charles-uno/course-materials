include ../build/common.mk

IMPORT_DIR = ../imports/project

all: project.pdf

project.pdf: project.tex $(VARS_TEX) $(IMPORT_DIR)/project.gen.tex
	@ $(TEX2PDF) project.tex
