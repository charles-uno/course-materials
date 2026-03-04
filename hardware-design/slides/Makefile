REPO_ROOT := $(shell git rev-parse --show-toplevel)
MD2TEX := $(REPO_ROOT)/hardware-design//md2tex/md2tex.py
BUILD_SLIDES := pdflatex -interaction=nonstopmode -shell-escape slides.tex >/dev/null

# call pdflatex twice to make sure the TOC is populated correctly
slides: clean
	@ $(MD2TEX) sections/*.md
	@ printf "\033[95mpreliminary build for toc ... \033[0m"; \
		$(BUILD_SLIDES); \
		if [[ -f slides.pdf ]]; then \
		echo "\033[92mdone\033[0m"; \
		printf "\033[95mfinal build ... \033[0m"; \
		$(BUILD_SLIDES); \
		echo "\033[92mdone\033[0m"; \
		else \
		echo "\033[91mfailed\033[0m (see slides.log)"; \
		fi
	
clean:
	@ rm -rf *.log *.aux *.toc *.log *.nav *.out *.snm *.pdf *.fdb_latex *.fls *.vrb _minted* *.data.minted *.fdb_latexmk *.cpt *.gen.tex sections/*.log sections/*.gen.tex ||:
