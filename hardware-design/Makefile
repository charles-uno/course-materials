
.PHONY: all clean tidy syllabus project slides quiz homework final

SLIDES_MD := $(wildcard chapters/*/slides.main.md)
HOMEWORK_MD := $(wildcard chapters/*/homework.main.md)
QUIZ_MD := $(wildcard chapters/*/quiz.main.md)

all: syllabus project slides quiz homework # final

syllabus: syllabus/syllabus.pdf
project: project/project.pdf
slides: $(SLIDES_MD:.main.md=.pdf)
quiz: $(QUIZ_MD:.main.md=.pdf)
homework: $(HOMEWORK_MD:.main.md=.pdf)
final:
	cd final && make

MD2PDF := build/md2pdf.sh

BUILD_TOOLS := $(wildcard build/**/*.*)

MAIN_MD := $(shell find * -mindepth 1 -not -path "build/*" -name "*.main.md" | sort)

$(MAIN_MD:.main.md=.pdf): %.pdf: %.main.md $(BUILD_TOOLS)
	@$(MD2PDF) $<

# remove junk per the .gitignore
clean: tidy
	@ git clean -fdX

# remove junk per .gitignore but leave the PDFs
tidy: 
	@ git clean -fdX -e "*.pdf"
