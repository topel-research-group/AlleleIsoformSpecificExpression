#!/bin/bash

for i in 131 132 133; do
	grep "Sm_t" R05_126d.GoodCov.lst | sed 's/Sm_t/Sm_g/g' | sed 's/-RA//g' | while read j; do
		grep $j P18257_${i}.bias.tsv >> ../P18257_${i}.bias.GoodCov.tsv
	done
done
