# Remap reads with stricter parameters, as was done in the SotS analysis

Parameters used by Rastogi _et al._ (alternative splicing)
* Genes with 2+ exons
* Minimum intron length of 50 bp
* Mapping to reference genome with Bowtie: `-n 2 -k 2 --best`
  * These parameters don't all exist in Bowtie2...
* Horizontal gene coverage of at least 80%
* Read depth of at least 4x
* "For exons anticipated to show exon-skipping, the observation had a consensus from more than 20% and less
   than 80% samples."
* "On the other hand, introns having a consensus observation of their retention from more than 20% samples were
   considered as true events."


####

Get mapping stats (examples):

```
for i in ERR*; do
	UNMAP=$(grep "aligned 0 times" ${i}/runHisat2.sge.e* | sed 's/^ *//g' | cut -f-2 -d' ')
	SINGMAP=$(grep "aligned exactly" ${i}/runHisat2.sge.e* | sed 's/^ *//g' | cut -f-2 -d' ')
	MULTIMAP=$(grep "aligned >1" ${i}/runHisat2.sge.e* | sed 's/^ *//g' | cut -f-2 -d' ')
	MAPPC=$(grep "overall" ${i}/runHisat2.sge.e* | cut -f1 -d' ')

	echo -e "| ${i} | |    ${MAPPC} | ${UNMAP} | ${SINGMAP} | ${MULTIMAP} |" >> README.md
done
```

```
for i in SRR*; do
	UNMAP=$(grep "aligned concordantly 0 times" ${i}/runHisat2.sge.e* | cut -f2 -d'(' | cut -f1 -d')')
	SINGMAP=$(grep "aligned concordantly exactly" ${i}/runHisat2.sge.e* | cut -f2 -d'(' | cut -f1 -d')')
	MULTIMAP=$(grep "aligned concordantly >1" ${i}/runHisat2.sge.e* | cut -f2 -d'(' | cut -f1 -d')')
	MAPPC=$(grep "overall" ${i}/runHisat2.sge.e* | cut -f1 -d' ')

	echo -e "| ${i} | |       ${MAPPC}      |  ${UNMAP} | ${SINGMAP} |   ${MULTIMAP}  |" >> README.md
done
```
