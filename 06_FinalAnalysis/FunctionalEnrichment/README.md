# Functional enrichment of each timepoint's subsets

Note: Revigo was run only on genes with p < 0.05 unless otherwise specified

## Code for running an analysis of common GO terms in a dataset
```
for i in *analysis; do
        cd ${i}
        for j in R05*.lst; do
		cat $j | while read k; do
			grep $k ../R05_v1.1.9.GOterms.AllGenes.tsv | grep -o "GO:......."
		done | while read l; do
			grep $l ../GOterms.tsv
		done | sort | uniq -c | sort -h >> GOabund.${j}
	done
	cd ..
done
```

## Gode for running TopGO for all samples
```
for i in *analysis; do
	cd ${i}
	for j in *.lst; do
		Rscript ../TopGO.R ${j}
	done
	cd ..
done
```

## Get significantly enriched GO terms in a format suitable for Revigo
## Then running Revigo on everything
## And sort it by log10 p value
```
for i in *analysis; do
	cd ${i}
	for j in GO.R05*.lst; do
		awk -F'\t' '$6 + 0 < 0.05' ${j} | grep "^GO:" | cut -f1,6 > ForRevigo.${j}
		java -jar ~/bin/Revigo/RevigoStandalone.jar ForRevigo.${j}
	done
	for k in *_revigoOut.txt; do
		header=$(head -n1 ${k})
		tail -n+2 ${k} | sort -h -k8 > temporaryGO
		echo -e "${header}\n$(cat temporaryGO)" > ${k}
		rm temporaryGO
	done	
	cd ..
done
```

## And then sorting the table of results by p-value
```


`sort -h -k8 ForRevigo.[]_revigoOut.txt | cut -f-8 | column -t | less`
```
* Note - the table works by log10 of the p-value, thus only values below -1.301 should be considered
  * log10(0.05) ~= -1.301
* Revigo seems to limit its output to this value anyway, more or less
