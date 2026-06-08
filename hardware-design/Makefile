.PHONY: all clean tidy syllabus project slides quiz homework final placeholder

MD2PDF := build/md2pdf.sh
BUILD_TOOLS := $(wildcard build/**/*.*)

TARGET_MDS := $(shell find * -mindepth 1 -not -path "build/*" -name "*.md" | sort)
TARGET_PDFS := $(foreach f,$(TARGET_MDS),$(shell $(MD2PDF) $(f) --get-pdf-path))

all: $(TARGET_PDFS)

slides: $(filter %-slides.pdf,$(TARGET_PDFS))
homework: $(filter %-homework.pdf,$(TARGET_PDFS))
quiz: $(filter %-quiz.pdf,$(TARGET_PDFS))

chapters/%: placeholder
	$(eval CH_DIR := $(patsubst %/,%,$*))
	$(eval MATCHING_PDFS := $(filter artifacts/$(CH_DIR)-%,$(TARGET_PDFS)))
	@if [ -n "$(MATCHING_PDFS)" ]; then $(MAKE) $(MATCHING_PDFS); else echo "No targets for chapter: $(CH_DIR)"; fi

placeholder: # avoid confusion since the chapter target is a directory

syllabus: artifacts/syllabus.pdf
project: artifacts/project.pdf

final:
	cd final && make

$(TARGET_PDFS): $(BUILD_TOOLS)
	@ $(MD2PDF) $(shell $(MD2PDF) $@ --get-md-path)

# remove junk per the .gitignore
clean: tidy
	@ git clean -fdX

# remove junk per .gitignore but leave the PDFs
tidy: 
	@ git clean -fdX -e "*.pdf"
