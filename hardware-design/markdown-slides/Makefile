
slides:
	mkdir -p build
	cp -r source/* build/
	./slide-maker.py
	cd build && pdflatex -interaction=nonstopmode -shell-escape slides.tex; pdflatex -interaction=nonstopmode -shell-escape slides.tex


clean:
	rm -rf build/*