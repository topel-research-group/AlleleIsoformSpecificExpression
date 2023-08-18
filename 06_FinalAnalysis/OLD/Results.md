# Results of ASE analysis
(This is before consideration of genomic data)

Can get results summary using `SummariseResults.sh` script in each subdirectory

Total nuclear genes: 
                                                     Based on 'no NAs'
| Group | Good cov | No NAs | Some NAs | All NAs ||  BAE  |  ASE  | MAE |
|-------|----------|--------|----------|---------||-------|-------|-----|
|   0d  |  11,073  |  9,473 |     213  |  1,387  || 3,481 | 5,684 | 308 |
|  49d  |   8,833  |  7,620 |     243  |    970  || 2,367 | 4,984 | 269 |
|  56d  |   9,566  |  8,258 |     257  |  1,051  || 2,670 | 5,246 | 342 |
|  72d  |   8,554  |  7,373 |     221  |    960  || 2,468 | 4,548 | 357 |
|  91d  |  10,146  |  8,626 |     273  |  1,247  || 2,862 | 5,296 | 468 |
| 126d  |   9,350  |  7,946 |     284  |  1,120  || 2,503 | 5,002 | 441 |
| 189d  |   8,106  |  6,958 |     205  |    943  || 1,710 | 4,885 | 363 |

Thresholds used are based on Hoguin et al., 2021:
* Biallelic expression (BAE) - <= 20% expression bias
* Allele-specific expressed (ASE) - 20% < AEB% <= 60%
* Monoallelic expression (MAE) - expression bias > 60%

Which of the genes contain SNPs?
* Can add some 'All NA' results to MAE if we filter genes by SNPs

#####

|                                                 |         |
|-------------------------------------------------|---------|
| Genes displaying MAE in at all seven timepoints |       7 |
| Genes displaying ASE in at all seven timepoints |   1,583 |
| Genes displaying BAE in at all seven timepoints |     625 |



How many of the 308 0d MAEs have a functional annotation?
* 126 with functional annotation
* 182 'predicted protein'

#####

Pathways of some R05 0d MAEs:
* Prephenate dehydratase (Sm_t00002593-RA) - phenylalanine, tyrosine and tryptophan biosynthesis
* Mevalonate kinase, chloroplastic (Sm_t00004758-RA) - isoprenoid biosynthesis
* D-cysteine desulfhydrase (Sm_t00012835-RA) - cysteine metabolism
  * D-cysteine + H2O <-> sulfide + NH3 + pyruvate
