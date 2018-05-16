PNG_FILES=$(patsubst %.py, %.png, $(wildcard A*.py))

.PHONY : clean all
all : $(PNG_FILES) log.txt complete.pdf

%.png : var.txt %.py
	python $*.py $< $@	

log.txt:
	git log > $@

%.pdf : %.tex
	pdflatex -shell-escape $^
		
.PHONY: clean
clean :
	rm -f *.png
	rm -f log.txt
	rm -f *.pdf
	rm -rf *.aux

	