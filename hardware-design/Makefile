.PHONY: all clean tidy syllabus project slides homework final exams

MD2PDF := build/md2pdf.sh
BUILD_TOOLS := $(wildcard build/**/*.*)

TARGET_MDS := $(shell find * -mindepth 1 -not -path "build/*" -not -path "imports/*" -not -path "*/imports/*" -name "*.md" | sort)
TARGET_PDFS := $(foreach f,$(TARGET_MDS),$(shell $(MD2PDF) $(f) --get-pdf-path))

all: exams syllabus project homework slides

exams:
	cd exams && $(MAKE)

slides:
	cd slides && $(MAKE)

homework:
	cd homework && $(MAKE)

syllabus: 
	cd syllabus && $(MAKE)

project:
	cd project && $(MAKE)

final:
	cd final && make

# remove junk per the .gitignore
clean: tidy
	@ git clean -fdX

# remove junk per .gitignore but leave the PDFs
tidy: 
	@ git clean -fdX -e "*.pdf"
