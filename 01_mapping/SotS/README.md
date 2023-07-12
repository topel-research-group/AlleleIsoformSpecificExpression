# Mapping and variant calling of Survivors of the Sea data

Note: This version uses stricter mapping, including the following hisat2 parameters to try and avoid artifacts:
`--no-mixed --no-discordant --max-intronlen 10000`

## Testing on P18257_101 (old depth filter of 10)

244,345 total variants called

Of these, 205,726 (84.2%) are okay
* 152,199 PASS
*  53,527 SnpCluster

38,619 variants were filtered out
*  19,667 DP
*   6,068 DP;SnpCluster
*     924 FS
*     113 FS;QD
*      70 FS;QD;SnpCluster
*     675 FS;SnpCluster
*   7,480 QD
*   3,622 QD;SnpCluster

Eyeballing loci identiied in _101, when compared across all R05 0d and 49d samples, while other samples are running
* Sm_t00000217-RA (predicted protein) shows an imbalance, apparently favouring one allele during the resting stages
* Sm_t00000278-RA (phosphatidylinositide polyphosphatase, Sac family) seems to go from near-monoallelic at 0d to biased in 49d (i.e. resting stages express both genes)

##################

Test: comparison of R05 0d samples vs. R05 49d
* 101, 102, 103 vs. 107, 108, 109
* Need to filter the relevant reads, then compare files
  * May be a way to generate a table in GATK?
    * `VariantsToTable`, but doesn't seem to work with the SnpCluster designation in the filter field...?

```
for i in x y z; do
	grep "^Sm_" ${i}/${i}_filtered.vcf | awk '$7 == "PASS" || $7 == "SnpCluster"' | cut -f1,2,4,5 > ${i}/${i}_InterestingPositions.tsv
done
```
Then `sort | uniq -c` to determine which replicates all show the same pattern, and THEN compare between timepoints using `comm`

```
cat P18257_101/P18257_101_InterestingPositions.tsv P18257_102/P18257_102_InterestingPositions.tsv \
P18257_103/P18257_103_InterestingPositions.tsv | sort | uniq -c | grep " 3 Sm_" | \
sed 's/      3 //g' > R05_0d_variants.tsv

cat P18257_107/P18257_107_InterestingPositions.tsv P18257_108/P18257_108_InterestingPositions.tsv \
P18257_109/P18257_109_InterestingPositions.tsv | sort | uniq -c | grep " 3 Sm_" | \
sed 's/      3 //g' > R05_49d_variants.tsv
```
######

Sm_t00004265-RA (Sm_000002F:667987-669087) shows, if not monoallelic, at least strongly biased expression
* TBC domain-containing protein
* Use this as an indicator of what to look for?

Possibly Sm_t00004393-RA (Rossmann-fold NAD(P)-binding domain-containing protein) (Sm_000002F:722160-723469)

Sm_t00001624-RA (ZIP family metal transporter) (Sm_000001F:918083-919516)
* Possibly monoallelic in both subsets?

Sm_t00002141-RA (predicted protein) (Sm_000005F:231628-231981)
* Definitely seems to shift to monoallelic in resting stages
* Also Sm_t00002142-RA? Possibly a split gene model...

Sm_t00011379-RA (DUF2196 domain-containing protein) (Sm_000020F:437306-438653)
* Resting stages showing monoallelic expression?

Sm_t00002587-RA (transmembrane amino acid transporter protein) (Sm_000005F:1224495-1226381)
* Definitely showing bias in resting stages

Sm_t00000284-RA - shifts to ~mono in resting stages?

Sm_t00000380-RA - shifts to biallelic in resting stages? (predicted protein, chloroplastic)
* Check localisation of the different variants, as some variants are in the 5' end of the CDS

__In S1 vs W1 in the Nordic algal biomass data, Sm_t00003046-RA seems to show a biased expression in S1, and biallelic in W1__

######

Use snpEff to annotate variants?

######

# Check numbers of variants
```
comm -2 -3 <(cat P18257_101/P18257_101_filtered.vcf P18257_102/P18257_102_filtered.vcf \
	P18257_103/P18257_103_filtered.vcf | grep -v "^#" | cut -f1,2 | sort | uniq -c | grep "      3 " | \
	sed 's/^      3 //g') <(cat P18257_107/P18257_107_filtered.vcf P18257_108/P18257_108_filtered.vcf \
	P18257_109/P18257_109_filtered.vcf | grep -v "^#" | cut -f1,2 | sort | uniq -c | grep "      3 " | \
	sed 's/^      3 //g') | wc -l

comm -1 -3 <(cat P18257_101/P18257_101_filtered.vcf P18257_102/P18257_102_filtered.vcf \
	P18257_103/P18257_103_filtered.vcf | grep -v "^#" | cut -f1,2 | sort | uniq -c | grep "      3 " | \
	sed 's/^      3 //g') <(cat P18257_107/P18257_107_filtered.vcf P18257_108/P18257_108_filtered.vcf \
	P18257_109/P18257_109_filtered.vcf | grep -v "^#" | cut -f1,2 | sort | uniq -c | grep "      3 " | \
	sed 's/^      3 //g') | wc -l

comm -1 -2 <(cat P18257_101/P18257_101_filtered.vcf P18257_102/P18257_102_filtered.vcf \
	P18257_103/P18257_103_filtered.vcf | grep -v "^#" | cut -f1,2 | sort | uniq -c | grep "      3 " | \
	sed 's/^      3 //g') <(cat P18257_107/P18257_107_filtered.vcf P18257_108/P18257_108_filtered.vcf \
	P18257_109/P18257_109_filtered.vcf | grep -v "^#" | cut -f1,2 | sort | uniq -c | grep "      3 " | \
	sed 's/^      3 //g') | wc -l
```
Total variants across all six files	- 320,338
Number in group 1 only			- 60,075
Number in group 2 only			- 26,384
Number in all samples			- 145,296
