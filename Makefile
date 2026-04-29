main = report
compiler = pdfcompiler

.PHONY: all clean

all: $(main).pdf

$(main).pdf: $(main).tex
	$(compiler) $(main).tex
	$(compiler) $(main).tex

clean:
	rm -f *.aux *.log *.out *.toc *.lof *.lot