# Workflow for ASE analysis
Note for future iterations: should results be weighted by depth/number of SNVs per gene?


When GATK on the genomic data has finished running:
1) Filter the data to only good-quality, biallelic SNPs
2) Filter out genes that have no SNPs at all
3) Include genes that appear in SNP regions but show fully monoallelic expression


## General questions
1) How many genes were disregarded due to no SNPs?
2) How many genes were disregarded for having an AFB >= 20%?
3) How many genes were disregarded due to RNAseq coverage depth?

## Which genes display bias in vegetative cells?
1) Identify the genes that don't show an allelic frequency bias in genomic data (AFB)

2a) Identify the genes that have reasonable coverage in transcriptomic data
  * In this case, defined as at least 10x coverage across at least 80% of the exonic length
2b) Identify the genes that have a similar bias score across all replicates (HOW!?)


3) Investigate the genes showing the highest amount of bias


## Which genes display bias in resting stages?

Repeat the steps above, using each subset of resting stage genes


## How do the two groups compare?

1) Which genes show a big shift between conditions?

##########
R05_0d		P18257_101	P18257_102	P18257_103
R05_49d		P18257_107	P18257_108	P18257_109
R05_56d		P18257_113	P18257_114	P18257_115
R05_72d		P18257_119	P18257_120	P18257_121
R05_91d		P18257_125	P18257_126	P18257_127
R05_126d	P18257_131	P18257_132	P18257_133
R05_189d	P18257_138	P18257_139	-


for i in X Y Z; do
	ln -s ../../../04_ASE_Analysis/SotS/P18257_${i}/P18257_${i}.bias.tsv
done
ln -s ../../../04_ASE_Analysis/SotS/Groups/R05_?d/R05_?d.GoodCov.lst
```
