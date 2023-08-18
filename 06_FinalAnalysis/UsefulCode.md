# Get annotations of genes MAE in all groups
```
cat */*MAE.lst | sort | uniq -c | grep " 7 " | sed 's/      7 //g' | sed 's/Sm_g/Sm_t/g' | sed 's/$/-RA/g' | \
	while read i; do grep $i ../04_ASE_Analysis/ref/Annotation_FINAL.v3.tsv | cut -f-2; done
```

# Get annotations of genes MAE in all resting stages
```
cat 1_49d_analysis/R05_49d_MAE.lst 2_56d_analysis/R05_56d_MAE.lst 3_72d_analysis/R05_72d_MAE.lst \
	4_91d_analysis/R05_91d_MAE.lst 5_126d_analysis/R05_126d_MAE.lst 6_189d_analysis/R05_189d_MAE.lst | \
	sort | uniq -c | grep " 6 " | sed 's/      6 //g' | sed 's/Sm_g/Sm_t/g' | sed 's/$/-RA/g' | \
	 while read i; do grep $i ../04_ASE_Analysis/ref/Annotation_FINAL.v3.tsv | cut -f-2; done
```
