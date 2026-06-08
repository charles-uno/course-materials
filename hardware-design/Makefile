.PHONY: all clean tidy syllabus project slides quiz homework final

MD2PDF := build/md2pdf.sh
BUILD_TOOLS := $(wildcard build/**/*.*)

TARGET_MDS := $(shell find * -mindepth 1 -not -path "build/*" -name "*.md" | sort)
TARGET_PDFS := $(foreach f,$(TARGET_MDS),$(shell $(MD2PDF) $(f) --get-pdf-path))

all: $(TARGET_PDFS)

slides: $(filter %-slides.pdf,$(TARGET_PDFS))
homework: $(filter %-homework.pdf,$(TARGET_PDFS))
quiz: $(filter %-quiz.pdf,$(TARGET_PDFS))

syllabus: artifacts/syllabus.pdf
project: artifacts/project.pdf

# final is special. personalized build for each student based on CSV
final:
	cd final && make

# reverse dry run to get the input path from the destination path
$(TARGET_PDFS):
	@ $(MD2PDF) $(shell $(MD2PDF) $@ --get-md-path)

# remove junk per the .gitignore
clean: tidy
	@ git clean -fdX

# remove junk per .gitignore but leave the PDFs
tidy: 
	@ git clean -fdX -e "*.pdf"
