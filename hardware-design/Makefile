.PHONY: all clean tidy final


BUILD_TOOLS := $(wildcard build/md2tex/*.py)

# MD2TEX := build/md2tex.py
MD2TEX := build/md2tex/md2tex_new.py


# some markdown files turn into standalone tex docs
MAIN_MD := $(shell find * -mindepth 1 -not -path "build/*" -name "*.main.md")
MAIN_TEX := $(MAIN_MD:.md=.gen.tex)
MAIN_PDF := $(MAIN_MD:.main.md=.pdf)

# some markdown files generate content to be imported
INCL_MD := $(wildcard chapters/*/*.incl.md)
INCL_TEX := $(INCL_MD:.md=.gen.tex)

# some manual tex docs to import the above
MANUAL_TEX := $(shell find . -name "*.tex" ! -name "*.gen.*" -not -path "./build/*")
MANUAL_PDF := $(MANUAL_TEX:.tex=.pdf)

all: $(MAIN_PDF) $(MANUAL_PDF)

define build_latex
	$(eval BASE := $(notdir $(1)))
	@printf "building \033[35m$(2)\033[0m -> \033[35m$(1).pdf\033[0m ... "
	@latexmk -silent -pdf -jobname=$(BASE) -interaction=nonstopmode -shell-escape -cd $(2) >/dev/null 2>&1; \
	if [ -f $(1).pdf ]; then \
		printf "\033[92mdone\033[0m\n"; \
		latexmk -c -jobname=$(BASE) -cd -e '$$clean_ext = "nav snm vrb"' $(2) >/dev/null 2>&1; \
	else \
		printf "\033[31mfailed\033[0m (see $(1).log)\n"; \
		[ -f $(1).log ] && cat $(1).log; exit 1; \
	fi
endef

$(MANUAL_PDF): %.pdf: %.tex $(INCL_TEX)
	@$(call build_latex,$*,$<)

$(MAIN_PDF): %.pdf: %.main.gen.tex
	@$(call build_latex,$*,$<)



# foo.md -> foo.gen.tex
# this rule is used by pretty much everything
%.gen.tex: %.md $(MD2TEX)
	@$(MD2TEX) $<









syllabus: syllabus/syllabus.pdf

syllabus/syllabus.main.gen.tex: syllabus/syllabus.main.md build/templates/syllabus.tex $(BUILD_TOOLS)
	./build/md2tex/md2tex_new.py syllabus/syllabus.main.md

project: project/project.pdf

project/project.main.gen.tex: project/project.main.md build/templates/project.tex $(BUILD_TOOLS)
	./build/md2tex/md2tex_new.py project/project.main.md


QUIZ_MD := $(wildcard chapters/*/quiz.main.md)
QUIZ_TEX := $(QUIZ_MD:.md=.gen.tex)
QUIZ_PDF := $(QUIZ_MD:.main.md=.pdf)


quiz: $(QUIZ_PDF)





final: 
	cd exams && make


# remove junk per the .gitignore
clean: tidy
	@ git clean -fdX

# remove junk per .gitignore but leave the PDFs
tidy: 
	@ git clean -fdX -e "*.pdf"
