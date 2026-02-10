
slides:
	mkdir -p build
	cp -r source/ build/
	cp -r ../slides/images build/images
	./slide-maker.py
	cd build && pdflatex -interaction=nonstopmode -shell-escape slides.tex; pdflatex -interaction=nonstopmode -shell-escape slides.tex


clean:
	rm -rf build/*