#!/bin/bash

INFILE=$(ls *.Results.tsv)
OUTPREFIX=$(echo $INFILE | cut -f1 -d'.')

grep "^Sm_" $INFILE | awk '$4 <= 20' | cut -f1 > ${OUTPREFIX}.BAE.lst
grep "^Sm_" $INFILE | awk '$4 > 20 && $4 <= 60' | cut -f1 > ${OUTPREFIX}.ASE.lst
grep "^Sm_" $INFILE | awk '$4 > 60' | cut -f1 > ${OUTPREFIX}.MAE.lst
