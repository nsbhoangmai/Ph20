# include config.mk
# Generate energy graphs obtained using different methods.

# PROG_FILES=$(patsubst %.py, %, $(wildcard A*.py))
 
PNG_FILES=$(patsubst %.py, %.png, $(wildcard A*.py))

.PHONY : clean all

all : $(PNG_FILES)

%.png : var.txt %.py
	python $*.py $< $@	
# trunc_t.png : var.txt $(tt_sr)
	#$(tt_exe) $< $@
#trunc_x.png : var.txt $(tx_sr)
	#$(tx_exe) $< $@
#ene_com.png : var.txt $(ec_sr)
	#$(ec_exe) $< $@
#spr_com.png : var.txt $(sc_sr)
	#$(sc_exe) $< $@
#ene_sym.png : var.txt $(es_sr)
	#$(es_exe) $< $@
#err_sym.png : var.txt $(er_sr)
	#$(er_exe) $< $@

.PHONY: clean
clean :
	rm -f *.png

	