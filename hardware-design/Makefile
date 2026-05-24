
.PHONY: all clean tidy syllabus project slides quiz homework final

SLIDES_MD := $(wildcard chapters/*/slides.main.md)
HOMEWORK_MD := $(wildcard chapters/*/homework.main.md)
QUIZ_MD := $(wildcard chapters/*/quiz.main.md)

all: syllabus project slides quiz homework # final
	@ build/consolidate-artifacts.sh

syllabus: syllabus/syllabus.pdf
project: project/project.pdf
slides: $(SLIDES_MD:.main.md=.pdf)
quiz: $(QUIZ_MD:.main.md=.pdf)
homework: $(HOMEWORK_MD:.main.md=.pdf)
final:
	cd final && make

# pretty much everything follows the same pattern:
# foo.main.md -> foo.main.gen.tex -> foo.pdf

MD2TEX := build/md2tex/md2tex.py
TEX2PDF := build/tex2pdf.sh

BUILD_TOOLS := $(MD2TEX) $(TEX2PDF) $(wildcard build/templates/*.tex)

# so we can import from the templates directory as well as the build directory
REPO_ROOT := $(shell git rev-parse --show-toplevel)
export TEXINPUTS := .:$(REPO_ROOT)/hardware-design/build/templates/:

MAIN_MD := $(shell find * -mindepth 1 -not -path "build/*" -name "*.main.md")

$(MAIN_MD:.main.md=.pdf): %.pdf: %.main.gen.tex $(BUILD_TOOLS)
	@$(TEX2PDF) $<

%.gen.tex: %.md $(BUILD_TOOLS)
	@$(MD2TEX) $<

# remove junk per the .gitignore
clean: tidy
	@ git clean -fdX

# remove junk per .gitignore but leave the PDFs
tidy: 
	@ git clean -fdX -e "*.pdf"
