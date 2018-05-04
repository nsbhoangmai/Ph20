TXT_FILES=$(wildcard books/*.txt)
DAT_FILES=$(patsubst books/%.txt, %.dat, $(TXT_FILES))
include config.mk

# Generate summary table.
results.txt : $(DAT_FILES) $(ZIPF_SRC)
	$(ZIPF_EXE) $(DAT_FILES) > $@

.PHONY : variables
variables : 
	@echo TXT_FILES: $(TXT_FILES)
	@echo DAT_FILES: $(DAT_FILES)
# Count words.
.PHONY : dats
dats : $(DAT_FILES)

%.dat : books/%.txt $(COUNT_SRC)
	$(COUNT_EXE) $< $@
	
.PHONY : clean
clean :
	rm -f $(DAT_FILES)
	rm -f results.txt