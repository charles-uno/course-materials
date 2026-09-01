MD2TEX = ../build/md2tex/md2tex.py
TEX2PDF = ../build/tex2pdf.sh

MD_SOURCES = $(wildcard imports/*.md)
TEX_OUTPUTS = $(MD_SOURCES:.md=.gen.tex)

TARGET = hardware-design-slides.pdf
MAIN_TEX = hardware-design-slides.tex

.PHONY: all clean

all: $(TARGET)

$(TARGET): $(MAIN_TEX) $(TEX_OUTPUTS) beamerthemegrape.sty
	@ $(TEX2PDF) $(MAIN_TEX)

imports/%.gen.tex: imports/%.md
	@ $(MD2TEX) $<

clean:
	cd .. && $(MAKE) clean

tidy:
	cd .. && $(MAKE) tidy
