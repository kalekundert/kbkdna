# LaTeX Makefile
FILE=publishing_python_code

all: $(FILE).pdf

$(FILE).pdf: $(FILE).tex ../setup.py ../README.rst ../LICENSE.txt $(wildcard ../kbkdna/*.py) $(wildcard screenshots/*.png)
	pdflatex -shell-escape $(FILE)
	pdflatex -shell-escape $(FILE)

show: $(FILE).pdf
	fork zathura $(FILE).pdf

clean:
	\rm -f *.aux *.blg *.out *.bbl *.log *.toc *.use *.doc *.test *.pdf

.PHONY: show clean

