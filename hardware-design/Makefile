
.PHONY: all clean tidy syllabus project slides quiz homework final

SLIDES_MD := $(wildcard chapters/*/slides.md)
HOMEWORK_MD := $(wildcard chapters/*/homework.md)
QUIZ_MD := $(wildcard chapters/*/quiz.md)
CHAPTERS_MD := $(wildcard chapters/*/*.md)

MD2PDF := build/md2pdf.sh
BUILD_TOOLS := $(wildcard build/**/*.*)

MAIN_MD := $(shell find * -mindepth 1 -not -path "build/*" -name "*.md" | sort)
MAIN_PDF := $(MAIN_MD:.md=.pdf)

all: syllabus project chapters # final

syllabus: syllabus/syllabus.pdf
project: project/project.pdf
slides: $(SLIDES_MD:.md=.pdf)
quiz: $(QUIZ_MD:.md=.pdf)
homework: $(HOMEWORK_MD:.md=.pdf)
chapters: $(CHAPTERS_MD:.md=.pdf)

final:
	cd final && make

$(MAIN_MD:.md=.pdf): %.pdf: %.md $(BUILD_TOOLS)
	@$(MD2PDF) $<

# remove junk per the .gitignore
clean: tidy
	@ git clean -fdX

# remove junk per .gitignore but leave the PDFs
tidy: 
	@ git clean -fdX -e "*.pdf"
