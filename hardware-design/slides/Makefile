include ../build/common.mk

MD_SOURCES = $(wildcard ../imports/*/slides.md)
TEX_OUTPUTS = $(MD_SOURCES:.md=.gen.tex)

TARGET = hardware-design-slides.pdf
MAIN_TEX = hardware-design-slides.tex

all: $(TARGET)

$(TARGET): $(MAIN_TEX) $(TEX_OUTPUTS) beamerthemegrape.sty
	@ $(TEX2PDF) $(MAIN_TEX)
