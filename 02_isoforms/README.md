# Identifying ASE/ISE events

## rMats

Try analysing with rMats, as this has the most citations (albeit one of the older tools on the list)
* Installation problematic but has a Docker container!
  * Available on Annotation-3

Example script to get list of significant genes from the output files
```
for i in *_0_*; do
	echo $i
	echo "SE JC"
	awk '$20 <= 0.05' ${i}/SE.MATS.JC.txt | cut -f2 | tr -d '"' | sed 's/Sm_g/Sm_t/g' | sed 's/$/-RA/g'
	echo "SE JCEC"
	awk '$20 <= 0.05' ${i}/SE.MATS.JCEC.txt | cut -f2 | tr -d '"' | sed 's/Sm_g/Sm_t/g' | sed 's/$/-RA/g'
	echo "MXE JC"
	awk '$22 <= 0.05' ${i}/MXE.MATS.JC.txt | cut -f2 | tr -d '"' | sed 's/Sm_g/Sm_t/g' | sed 's/$/-RA/g'
	echo "MXE JCEC"
	awk '$22 <= 0.05' ${i}/MXE.MATS.JCEC.txt | cut -f2 | tr -d '"' | sed 's/Sm_g/Sm_t/g' | sed 's/$/-RA/g'
	echo ""
done
```

### 03 April 2023 - test run

Try running PRJEB22707 (copepod) data - control 65h vs. copepod 65h

One significant result - Sm_g00009370
* Good model, but v. low coverage in the copepod study...
  * Predicted protein

### 05 April 2023

Try running PRJNA912555 (season/growth phase) data - S1 (skip _103) vs. W1

Four significant results?
* Sm_g00004215 - This model should be split!
* Sm_g00009385 - This model should be split!
* Sm_g00010631 - Half coverage, and should be split
* Sm_g00020211 - Funky coverage, should possibly be split?

### 17 April 2023

Try running SotS data - R05 control vs 49d

Significant results
* Sm_g00003456 - Model needs a little fixing but the relevant introns seem legit? Predicted protein
* Sm_g00004215 - This model should be split!
* Sm_g00008214 - Model should be merged with upstream models, but the introns seem legit
* Sm_g00010631 - Half coverage, and should be split
* Sm_g00012950 - Model needs a little fixing but the alt. splicing seems legit
* Sm_g00013116 - Some 'introns' caused by indels, but the real introns show evidence of alt. splicing
* Sm_g00015430 - Funky coverage but seems legit?
* Sm_g00020211 - Funky coverage, should possibly be split?

#####

Possible software to use
* SplAdder	2016	125 citations in Scholar
* rMats		2014	1,489 citations in Scholar
* SUPPA2	2018	304 citations in Scholar
* SpliceTrap	2011	108 citations in Scholar
* JUM		2018	55 citations in Scholar
