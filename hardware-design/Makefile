.DEFAULT_GOAL := all
.PHONY: all clean tidy syllabus project slides exams homework final
.SECONDARY:

MD2TEX   := scripts/md2tex/md2tex.py
TEX2PDF  := scripts/tex2pdf.sh
VARS2TEX := scripts/vars2tex.py

VARS_TEX := templates/vars.gen.tex
DOC_STY  := templates/course-doc.sty

SLIDES_IMPORTS := $(patsubst %.md,%.gen.tex,$(sort $(wildcard content/*/slides.md)))

HW_SOURCES  := $(sort $(wildcard content/*/homework.md))
HW_CHAPTERS := $(notdir $(patsubst %/,%,$(dir $(HW_SOURCES))))
HW_PDFS     := $(addprefix artifacts/,$(addsuffix -homework.pdf,$(HW_CHAPTERS)))

EXAM1_IMPORTS := \
	content/01-data-representation/exam.gen.tex \
	content/02-logic-representation/exam.gen.tex \
	content/03-computer-architecture/exam.gen.tex

EXAM2_IMPORTS := \
	content/04-linux-shell/exam.gen.tex \
	content/05-assembly-programming/exam.gen.tex \
	content/06-control-flow/exam.gen.tex

EXAM3_IMPORTS := \
	content/07-os-concepts/exam.gen.tex \
	content/08-breadboards/exam.gen.tex \
	content/09-networking/exam.gen.tex

EXAM_PDFS := artifacts/exam1.pdf artifacts/exam2.pdf artifacts/exam3.pdf

all: syllabus project slides exams homework

syllabus: artifacts/syllabus.pdf
project: artifacts/project.pdf
slides: artifacts/slides.pdf
exams: $(EXAM_PDFS)
homework: $(HW_PDFS)

final:
	cd final && $(MAKE)

$(VARS_TEX): vars.yaml $(VARS2TEX)
	@ python3 $(VARS2TEX) vars.yaml $(VARS_TEX)

content/%.gen.tex: content/%.md
	@ $(MD2TEX) $<

artifacts/syllabus.pdf: templates/syllabus.tex $(DOC_STY) $(VARS_TEX) content/syllabus/syllabus.gen.tex
	@ $(TEX2PDF) $< && mkdir -p artifacts && mv templates/syllabus.pdf $@

artifacts/project.pdf: templates/project.tex $(DOC_STY) $(VARS_TEX) content/project/project.gen.tex
	@ $(TEX2PDF) $< && mkdir -p artifacts && mv templates/project.pdf $@

artifacts/slides.pdf: templates/slides.tex templates/beamerthemegrape.sty $(SLIDES_IMPORTS)
	@ $(TEX2PDF) $< && mkdir -p artifacts && mv templates/slides.pdf $@

artifacts/exam1.pdf: templates/exam1.tex templates/exam-preamble.tex $(DOC_STY) $(VARS_TEX) $(EXAM1_IMPORTS)
	@ $(TEX2PDF) $< && mkdir -p artifacts && mv templates/exam1.pdf $@

artifacts/exam2.pdf: templates/exam2.tex templates/exam-preamble.tex $(DOC_STY) $(VARS_TEX) $(EXAM2_IMPORTS)
	@ $(TEX2PDF) $< && mkdir -p artifacts && mv templates/exam2.pdf $@

artifacts/exam3.pdf: templates/exam3.tex templates/exam-preamble.tex $(DOC_STY) $(VARS_TEX) $(EXAM3_IMPORTS)
	@ $(TEX2PDF) $< && mkdir -p artifacts && mv templates/exam3.pdf $@

artifacts/%-homework.pdf: templates/%-homework.gen.tex $(DOC_STY) $(VARS_TEX) content/%/homework.gen.tex
	@ $(TEX2PDF) $< && mkdir -p artifacts && mv templates/$*-homework.pdf $@

templates/%-homework.gen.tex: templates/homework.tex
	@ sed 's|@@import_dir@@|../content/$*/|g' $< > $@

# remove junk per the .gitignore
clean: tidy
	@ git clean -fdX

# remove junk per the .gitignore but leave the PDFs
tidy:
	@ git clean -fdX -e "*.pdf"
