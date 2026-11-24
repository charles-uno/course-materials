include ../build/common.mk

EXAM1_IMPORTS = \
	../imports/01-data-representation/exam.gen.tex \
	../imports/02-logic-representation/exam.gen.tex \
	../imports/03-computer-architecture/exam.gen.tex

EXAM2_IMPORTS = \
	../imports/04-linux-shell/exam.gen.tex \
	../imports/05-assembly-programming/exam.gen.tex \
	../imports/06-control-flow/exam.gen.tex

EXAM3_IMPORTS = \
	../imports/07-os-concepts/exam.gen.tex \
	../imports/08-breadboards/exam.gen.tex \
	../imports/09-networking/exam.gen.tex

all: exam1.pdf exam2.pdf exam3.pdf

exam1.pdf: exam1.tex exam-preamble.tex $(VARS_TEX) $(EXAM1_IMPORTS)
	@ $(TEX2PDF) exam1.tex

exam2.pdf: exam2.tex exam-preamble.tex $(VARS_TEX) $(EXAM2_IMPORTS)
	@ $(TEX2PDF) exam2.tex

exam3.pdf: exam3.tex exam-preamble.tex $(VARS_TEX) $(EXAM3_IMPORTS)
	@ $(TEX2PDF) exam3.tex
