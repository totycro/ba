TEXFILE="quadtrees.arbeit.tex"
PDFFILE="quadtrees.arbeit.pdf"
BASENAME="quadtrees.arbeit"

all: pdf1

spell:
	 aspell -l de -t -c ${TEXFILE}

everything:
	make all
	make bib
	make all
	make all

bib:
	bibtex ${BASENAME}

pdf1:
	pdflatex ${TEXFILE}

pdf: dvi ps ps2pdf

dvi:
	latex ${TEXFILE}

ps: dvi
	dvips quadtrees.presentation.dvi

ps2pdf:ps
	ps2pdf quadtrees.presentation.ps

dvi2pdf2:
	dvipdf quadtrees.presentation.dvi

oldall:
	latex cli-shells.presentation.tex
	dvipdf cli-shells.presentation.dvi

edit:
	vim ${TEXFILE}

view:
	okular ${PDFFILE} 2>/dev/null 1>&2 &

#view:
#okular quadtrees.presentation.ps 2>/dev/null 1>&2 &

