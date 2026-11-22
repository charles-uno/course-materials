MD2TEX = ../build/md2tex/md2tex.py
TEX2PDF = ../build/tex2pdf.sh

MD_SOURCES = $(wildcard ../imports/*/homework.md)
CHAPTERS = $(notdir $(patsubst %/,%,$(dir $(MD_SOURCES))))
TARGETS = $(addsuffix -homework.pdf,$(CHAPTERS))

.PHONY: all clean tidy
.SECONDARY:

all: $(TARGETS)

%-homework.pdf: %-homework.gen.tex ../imports/%/homework.gen.tex
	@ $(TEX2PDF) $<

%-homework.gen.tex: template.tex ../imports/%/homework.md
	@ python3 -c 'import sys, yaml; \
		lines = open(sys.argv[2]).read().splitlines(); \
		idx = next((i for i, l in enumerate(lines) if l.startswith("---")), None); \
		meta = (yaml.safe_load("\n".join(lines[:idx])) or {}) if idx is not None else {}; \
		tpl = open(sys.argv[1]).read(); \
		out = (tpl \
			.replace("@@title@@", str(meta.get("title", sys.argv[3]))) \
			.replace("@@date@@", str(meta.get("date", "TBD"))) \
			.replace("@@import_dir@@", f"../imports/{sys.argv[3]}/")); \
		open(sys.argv[4], "w").write(out)' \
		template.tex ../imports/$*/homework.md $* $@

../imports/%/homework.gen.tex: ../imports/%/homework.md
	@ $(MD2TEX) $<

# remove junk per the .gitignore
clean: tidy
	@ git clean -fdX

# remove junk per the .gitignore but leave the PDFs
tidy:
	@ git clean -fdX -e "*.pdf"
