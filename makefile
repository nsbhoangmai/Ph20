PNG_FILES=$(patsubst %.py, %.png, $(wildcard A*.py))

.PHONY : clean all
all : $(PNG_FILES)

%.png : var.txt %.py
	python $*.py $< $@	

.PHONY: clean
clean :
	rm -f *.png

	