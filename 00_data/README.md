# _Skeletonema marinoi_ transcriptomics datasets to include in this study

SotS resting stages

General MMETSP datasets
* All of these datasets were high quality with no apparent adapters, so running `-m 40 -q 30,30` on all of them

|    Strain     |      Origin      | Project | BioProject  | # files | Platform  | Length |                                    QC                                    |
|---------------|------------------|---------|-------------|---------|-----------|--------|--------------------------------------------------------------------------|
| FE60          | Adriatic Sea     | MMETSP  | PRJNA248394 |  2 (PE) | HiSeq2000 | 2x50bp | 30,680,292 pairs, 3,068,029,200 bp; nothing trimmed                      |
| FE7           | Adriatic Sea     | MMETSP  | PRJNA248394 |  2 (PE) | HiSeq2000 | 2x50bp | 31,282,299 pairs, 3,128,229,900 bp; nothing trimmed                      | 
| skelA (0918)  | Narrangasett Bay | MMETSP  | PRJNA248394 |  2 (PE) | HiSeq2000 | 2x50bp | 40,559,018 pairs, 4,055,901,800 bp; nothing trimmed                      |
| skelA (0920)  | (As above?)      | MMETSP  | PRJNA248394 |  2 (PE) | HiSeq2000 | 2x50bp | 20,929,170 pairs, 2,092,917,000 bp -> 20,328,645 pairs, 2,025,485,034 bp |
| SM1012Den-03  | Oresund          | MMETSP  | PRJNA248394 |  2 (PE) | HiSeq2000 | 2x50bp | 42,447,333 pairs, 4,244,733,300 bp; nothing trimmed                      |
| SM1012Hels-07 | Baltic Sea       | MMETSP  | PRJNA248394 |  2 (PE) | HiSeq2000 | 2x50bp | 39,169,175 pairs, 3,916,917,500 bp; nothing trimmed                      |
| UNC1201       | ???              | MMETSP  | PRJNA248394 |  2 (PE) | HiSeq2000 | 2x50bp | 20,929,170 pairs, 2,092,917,000 bp; nothing trimmed                      |

Additional datasets available at NCBI

|  Strain   |      Origin      |                  Project                   | BioProject  | # files  | Platform     | Length  |                       QC                       |
|-----------|------------------|--------------------------------------------|-------------|----------|--------------|---------|------------------------------------------------|
| 142       | Gullmarsfjorden  | Cheregi et al., 2023 - season/growth phase | PRJNA912555 |  24 (PE) | NovaSeq 6000 | 2x150bp | Removed Illumina adapters; `-m 50`             |
| 8 strains | Baltic Sea       | Pinseel et al., 2022 - salinity gradient   | PRJNA772794 | 144 (PE) | HiSeq4000    | 2x100bp | Removing Illumina adapter, `-m 50 -q 30,30`    |
| C1417     |                  | Ferrante et al., 2019 - sex and salinity   | PRJEB33171  |  14 (SE) | HiSeq2000    |    50bp | `-m 40 -q 30,30` (no adapters)                 |
| V32       | Vinga, Skagerrak | Amato et al., 2018 - presence of copepods  | PRJEB22707  |  12 (SE) | HiSeq2000    |    50bp | `-m 40 -q 30,30` (no adapters)                 |
|           | ? (China?)       | Zhang et al., 2021 - CO2 level             | PRJNA661548 |  12 (PE) | BGISEQ-500   | 2x150bp*| ??? No adapters; testing `-m 100 -q 30,30` ???


* Zhang et al. says 2x100bp reads; looking at the sequence files this is a typo
* Check naming convention of BGISEQ-500 for read pairing...

Currently not removing Ns, but see whether this is needed later

Note - MMETSP sequence descriptors on lines 1 and 3 don't match; will need to tweak the FASTQ files to process them

Note 2 - MAKE SURE THE READ DIRECTIONS ARE WHAT YOU EXPECT, AND NOT e.g. MATE PAIR OR SAME-DIRECTION
