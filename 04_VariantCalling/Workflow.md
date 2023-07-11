# Workflow for the allele-specific expression analysis

1.) QC and trimming
* The parameters depend on the exact datasets

2.) Mapping trimmed reads to reference
* `--no-unal --no-mixed --no-discordant --max-intronlen 10000`
  * No unaligned reads to reduce file size where possible
  * No mixed and no discordant as these are parameters used in Trinity utility script `align_and_estimate_abundance`
  * Max intron length 10,000 to try and reduce spurious read ends

3.) Preparing BAMs for GATK
* MarkDuplicates (MergeBamAlignment skipped for now)
* SplitNCigarReads
* Base quality recalibration skipped as we don't have this data available

4.) Variant calling using HaplotypeCaller
* Currently running to generate both a per-sample VCF, and a per-sample, all-BP GVCF
  * VCFs may not be required, as we merge and genotype the GVCFs in the next step
  * Also generating BAM files to visualise the variants in the active regions
* After running this step, can remove `*_1_WithRG.bam` and `*_2_marked_duplicates.bam`
  * These files are no longer required and take up a lot of space

5.) Merge GVCFs from a given strain/condition using CombineGVCFs, and genotype using GenotypeGVCFs
* This should make it easier to identify relevant variants than parsing all the files separately
  * If a variant shows up in any samples of this condition, it should show up in the GVCF,
    making for easier comparison versus the other condition

6.) Variant filtration
* Recommended filters for FS and QD, but these were for single samples and not grouped, so exercise caution
* Depth filter of 30, which should imply at least 10 depth per sample, but need to filter further to be sure

7.) Further filtering
* Need to use per-sample GVCFs to get depth info for all positions, to ensure a lack of variant isn't due to zero coverage
* Ensure that genotypes differ between groups
  * A variant in both (non-R05) groups could mean homozygous non-ref versus heterozygote, potentially

8.) Checking on the gene level
* Are these patterns consistent across the entire gene?
  * Best way to work on a per-gene bases?


########################

# Running through the GATK workflow one step at a time
## [Preprocessing](https://gatk.broadinstitute.org/hc/en-us/articles/360035531192)

Try on P18257_101 first

* Map to Reference - done

* Data cleanup - MergeBamAlignment (skipped for now) and MarkDuplicates - done

* SplitNCigarReads - done

* Base quality recalibration - BaseRecalibrator, ApplyBQSR, AnalyzeCovariates
  * We don't have a list of known variant positions so I can't run these steps...
  * May be okay to skip? See https://www.biostars.org/p/280274/

* Variant calling - HaplotypeCaller - done
  * Only recommended change for RNAseq is setting `--standard-min-confidence-threshold-for-calling` to 20,
    rather than 30 (default)
  * Some (older?) sources suggest the `-dontUseSoftClippedBases` parameter?

* Variant filtering - VariantFiltration
  * "We recommend specific hard filters, since VQSR and CNNScoreVariants require truth data for training that
     we don’t yet have for RNA."
  * Recommendations from [GATK's GitHub page](https://github.com/broadinstitute/gatk-docs/blob/master/gatk3-methods-and-algorithms/Calling_variants_in_RNAseq.md):
    * Note that these are for GATK v3, we're using v4...
    * "We recommend that you filter clusters of at least 3 SNPs that are within a window of 35 bases between
       them by adding `-window 35 -cluster 3` to your command. This filter recommendation is specific for RNA-seq
       data."
    * "As in DNA-seq, we recommend filtering based on Fisher Strand values (FS > 30.0) and Qual By Depth values
       (QD < 2.0)."
    * Need to add a depth filter so we're not trusting in single reads!
      * Added a depth filter of 10 for now; can adjust later as needed
        * 10 is too low, up it to 30?

Note: [This post](https://gatk.broadinstitute.org/hc/en-us/community/posts/5516533395099-GVCF-vs-VCF-INFO-tags-relevance-for-filtering-RNAseq-SNPs)
      seems to imply that GVCFs can be used with RNAseq

Note: Delete the readgroup and marked duplicate BAM files to save ~50% space!

########################################

Conditions:
1. Position must have good coverage in all samples, to ensure this isn't purely a coverage issue
2. One condition must be het, the other homo, to ensure this isn't a mapping issue
3. All samples of one condition must contain the variant, and none of the others can
4. The pattern must be consistent throughout the gene model
5. Need to be aware of the potential for aneuploidy (genomic coverage too high)
   and half-coverage regions (genomic coverage too low)

Using `EMIT_ALL_CONFIDENT_SITES` in HaplotypeCaller, we can identify confident reference sites as well
as variant sites, so we can filter for sites that appear in all samples
* If this works as it sounds like it should, this should help fix the coverage issue?
All sites can be output using a GVCF, but still uncertain about its use with RNAseq data
* Check this article: https://jasbsci.biomedcentral.com/articles/10.1186/s40104-019-0359-0

Should also consider other levels of biased expression, not just monoallelic

########################################

Let's try this workflow:
1. Output a GVCF for each sample using HaplotypeCaller with `-ERC GVCF` (or `BP_RESOLUTION`?)
  * `BP_RESOLUTION` gives the output I've been looking for, more or less
2. Combine the GVCFs for each condition using CombineGVCFs
3. Filter the combined files, and compare the two

Problem - GVCF and subsequent genotyping analysis is giving unusual results, likely as a result of the non-uniform nature of
          RNAseq reads vs. genomic, so this may be a dead end
* BUT, we can use the GVCF to identify those sites with zero coverage, versus just homozygous reference sites
  * The paper cited above uses a similar approach

In the interests of time, should we use a .list file of intervals representing the loci we're interested in
* This could, however, cause complications in partial models, and models missing from the annotation...
  * Can always rerun on the whole genome if desired, once the kinks are worked out of the pipeline
Format:		<chr>:<start>-<stop>
Also use the -ip (interval padding) parameter to add padding to the intervals (100bp?)

Hoguin et al. have a decent post-processing workflow regarding assessing bias by depth of each allele
