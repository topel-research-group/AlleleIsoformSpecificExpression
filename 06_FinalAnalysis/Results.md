# Results of ASE analysis

Total nuclear genes: 17,087

|       | No genomic |   Too much   | All bad  | Two bad  || Analysed |       |       |       |
| Group |  variants  | genomic bias | coverage | coverage ||  genes   |  BAE  |  ASE  |  MAE  |
|-------|------------|--------------|----------|----------||----------|-------|-------|-------|
|   0d  |    1,573   |     2,402    |   5,155  |    211   ||   7,746  | 3,250 | 3,970 |   526 |
|  49d  |    1,312   |     2,075    |   6,397  |    551   ||   6,752  | 2,229 | 4,003 |   520 |
|  56d  |    1,436   |     2,221    |   5,847  |    311   ||   7,272  | 2,517 | 4,145 |   610 |
|  72d  |    1,395   |     2,184    |   5,998  |    448   ||   7,062  | 2,433 | 3,950 |   679 |
|  91d  |    1,420   |     2,215    |   5,900  |    302   ||   7,250  | 2,610 | 3,949 |   691 |
| 126d  |    1,392   |     2,147    |   6,165  |    362   ||   7,021  | 2,355 | 3,967 |   699 |
| 189d  |    1,088   |     1,848    |   7,705  |    841*  ||   5,605  | 1,562 | 3,550 |   493 |

Note: 189d has two samples, thus samples were rejected with only one bad coverage sample

Thresholds used are based on Hoguin et al., 2021:
* Biallelic expression (BAE) - <= 20% expression bias
* Allele-specific expressed (ASE) - 20% < AEB% <= 60%
* Monoallelic expression (MAE) - expression bias > 60%

AFB analysis in R05AC:
* 3,460 with no variants
* 3,409 with too much bias
* 10,218 that can be analysed further

Comparison of numbers to P. tricornutum study:

|              | PhaTr | Smar |
|--------------|-------|------|
| BAE          |  11%  |  19% |
| ASE          |  22%  |  23% |
| MAE          |   1%  |   3% |
| Low cov.     |   -   |  15% |
| No variants  |  40%  |  20% |
| Genomic bias |  26%  |  20% |

#####

|                                                 |         |
|-------------------------------------------------|---------|
| Genes displaying MAE in at all seven timepoints |     111 |
| Genes displaying ASE in at all seven timepoints |   1,018 |
| Genes displaying BAE in at all seven timepoints |     624 |



How many of the 308 0d MAEs have a functional annotation?
* 126 with functional annotation
* 182 'predicted protein'

#####

Pathways of some R05 0d MAEs:
* Prephenate dehydratase (Sm_t00002593-RA) - phenylalanine, tyrosine and tryptophan biosynthesis
* Mevalonate kinase, chloroplastic (Sm_t00004758-RA) - isoprenoid biosynthesis
* D-cysteine desulfhydrase (Sm_t00012835-RA) - cysteine metabolism
  * D-cysteine + H2O <-> sulfide + NH3 + pyruvate
