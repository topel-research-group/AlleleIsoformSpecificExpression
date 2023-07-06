# Variant calling of reads for feeding into GATK ASEReadCounter

## Notes on best practices from Castel _et al._ (2015)

* Removal of duplicate reads (automatic in GATK)
* Uniquely-mapped reads (which sacrifices highly homologous loci)
  * This will have to be done post-mapping, as hisat2's -k parameter doesn't guarantee a best possible alignment
    * "For reads that have more than <int> distinct, valid alignments, hisat2 does not guarantee that
       the <int> alignments reported are the best possible in terms of alignment score."
* Re: mapping bias - "The simplest approach that can be applied to AE data without realignment is to filter
  sites with likely bias. In previous work and in this paper, unless mentioned otherwise, we remove about 20%
  of hetSNPs that either fall within regions of low mappability (ENCODE 50 bp mappability score < 1) or show
  mapping bias in simulations."
  * "This reduces the number of sites with strong bias by about 50% (Fig. 3b) but the genome-wide reference
     ratio remaining slightly above 0.5 indicates residual bias (Figure S6a in Additional file 6). Using this
     ratio as a null in statistical tests instead of 0.5 can improve results (Figure S6b–e in Additional
     file 6)."
* Re: "homozygous sites appearing as monoallelically expressed" - the main point of the study is looking at
  differences between conditions, therefore we ought to be able to identify mono- vs. bi-allelic expression


## Notes from Rastogi _et al._ (2018) and Hoguin _et al._ (2021) studies on _Phaeodactylum_

* Include only variants that appear within coding sequences?
  * Or do we want to include loci within UTRs or introns?
  * Try with the whole gene model and see how many interesting variants fall in each category?
* "The approximate read depth (RD) of a given variant is more than or equal to 20 and 5 in gDNA and cDNA
   samples, respectively. We fixed these thresholds based on the first peak attained in the read depth
   frequency distribution (Supplementary Fig. 1) of all the variants in each respective sample."
* The Hoguin et al. paper also includes a formula for calculating average percent allele frequency and average
  allele expression bias per gene, so will need to check this formula


###################

## Additional notes

Gene models should be filtered by read coverage, so we don't get false positive results from weird-looking loci
* Average genomic coverage of ~2,000 (~2,200?), with a low variance (to exclude loci with fluctuating coverage
  that just happen to have a 2k average)


Note: In GF04, Sm_t00008231-RA shows signs of allele-specific expression when viewed in IGV
