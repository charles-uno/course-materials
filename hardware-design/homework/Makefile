include ../build/common.mk

MD_SOURCES = $(wildcard ../imports/*/homework.md)
CHAPTERS = $(notdir $(patsubst %/,%,$(dir $(MD_SOURCES))))
TARGETS = $(addsuffix -homework.pdf,$(CHAPTERS))

all: $(TARGETS)

%-homework.pdf: %-homework.gen.tex ../imports/%/homework.gen.tex
	@ $(TEX2PDF) $<

%-homework.gen.tex: template.tex
	@ sed 's|@@import_dir@@|../imports/$*/|g' $< > $@
