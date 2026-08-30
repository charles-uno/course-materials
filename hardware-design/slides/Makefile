MD2TEX = ../build/md2tex/md2tex.py
TEX2PDF = ../build/tex2pdf.sh

MD_SOURCES = $(wildcard ../imports/*/slides.md)
TEX_OUTPUTS = $(MD_SOURCES:.md=.gen.tex)

TARGET = hardware-design-slides.pdf
MAIN_TEX = hardware-design-slides.tex

.PHONY: all clean

all: $(TARGET)

$(TARGET): $(MAIN_TEX) $(TEX_OUTPUTS)
	@ $(TEX2PDF) $(MAIN_TEX)

../imports/%/slides.gen.tex: ../imports/%/slides.md
	@ $(MD2TEX) $<

# remove junk per the .gitignore
clean: tidy
	@ git clean -fdX

# remove junk per .gitignore but leave the PDFs
tidy: 
	@ git clean -fdX -e "*.pdf"
