# Remap reads with stricter parameters, as was done in the SotS analysis

NEED TO GENERATE STATS FOR THE MAPPING

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

Try SplAdder (and Bisbee?)

|    Study    | Mapped? |
|-------------|---------|
| PRJEB22707  |  Done   |
| PRJEB33171  |  Done   |
| PRJNA772794 |  Done   |
| PRJNA248394 |	 Done   |
| PRJNA912555 |  Done   |
| PRJNA661548 | (???)   |
| SotS        |  Done   |
