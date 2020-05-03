TARGET = paper
OUT = paper.pdf
TEX = *.tex
BIB = paper.bib
SRC = $(TEX) $(BIB) $(IMG)
FIGFILES=./figures/


all: $(OUT)
fast:
	pdflatex paper.tex;
	pdflatex paper.tex

$(OUT): $(SRC)


clean:
	rm -f $(addprefix $(TARGET)., aux bbl blg log dvi toc lof out ps pdf)


.SUFFIXES: .tex .pdf

.tex.pdf:
		pdflatex --shell-escape $(<:.tex=)
		bibtex $(<:.tex=)
		pdflatex $(<:.tex=)
		pdflatex $(<:.tex=)
		rm -f $(addprefix $(TARGET)., aux bbl blg log dvi toc lof out ps)
