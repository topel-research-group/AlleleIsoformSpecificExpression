From each BioProject, extract a list of SRA accession numbers and download with fasterq-dump
(both part of SRA toolkit v3.0.2)
```
prefetch --option-file SraAccList.txt
for i in ../tmpdir/sra/*sra; do fasterq-dump --split-files $i; done
rm ../tmpdir/sra/*sra

# Or, so we don't accumulate tonnes of intermediate files

while read i; do
	prefetch $i
	fasterq-dump --split-files ../tmpdir/sra/${i}.sra
	rm ../tmpdir/sra/${i}.sra
	gzip ${i}*fastq
done < SraAccList.txt
```
