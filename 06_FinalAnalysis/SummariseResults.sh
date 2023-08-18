#!/bin/bash

SAMPLE=$1
ANNOTATION=../ref/Annotations.tsv
OUTFILE=${SAMPLE}.Summary.tsv

while read i; do
	gene=$(echo "$i" | cut -f1)
	if grep $gene ${SAMPLE}_MAE.lst
	then
		echo -e "${i}\tMAE" >> $OUTFILE
	elif grep $gene ${SAMPLE}_ASE.lst
	then
		echo -e "${i}\tASE" >> $OUTFILE
	elif grep $gene ${SAMPLE}_BAE.lst
	then
		echo -e "${i}\tBAE" >> $OUTFILE
	else
		echo -e "${i}\t?" >> $OUTFILE
	fi
done < $ANNOTATION
