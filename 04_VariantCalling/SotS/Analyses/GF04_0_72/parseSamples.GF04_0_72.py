#!/usr/bin/env python3

# Parsing TSV files to identify where variants are occurring in only one subset

import os
import gzip
import pickle

#Debug
from time import time
import datetime

# Define conditions
strain = "GF04"
cond1 = "0d"
cond2 = "72d"

# Define gene gff file
gfffile = "../../../ref/Smar_v1.1.9_Annotation_Final.gff"

# Define the two grouped and filtered VCF files (compressed in this case)
group1 = "../../Groups/" + strain + "_" + cond1 + "/" + strain + "_" + cond1 + "_filtered.vcf.gz"
group2 = "../../Groups/" + strain + "_" + cond2 + "/" + strain + "_" + cond2 + "_filtered.vcf.gz"

# Define outfile for the whole analysis
finalout = strain + "_" + cond1 + "_" + cond2 + "_results.tsv"

# Also need to define the individual genomic VCF files, and stat pickles, so we can get coverage and genotype data
sample1 = "P18257_104"
sample2 = "P18257_105"
sample3 = "P18257_106"
sample4 = "P18257_122"
sample5 = "P18257_123"
sample6 = "P18257_124"

gvcf1 = "../../" + sample1 + "/" + sample1 + "_4_HapCalled.g.vcf.gz"
pickle1 = sample1 + "/" + sample1 + ".pickle"
gvcf2 = "../../" + sample2 + "/" + sample2 + "_4_HapCalled.g.vcf.gz"
pickle2 = sample2 + "/" + sample2 + ".pickle"
gvcf3 = "../../" + sample3 + "/" + sample3 + "_4_HapCalled.g.vcf.gz"
pickle3 = sample3 + "/" + sample3 + ".pickle"
gvcf4 = "../../" + sample4 + "/" + sample4 + "_4_HapCalled.g.vcf.gz"
pickle4 = sample4 + "/" + sample4 + ".pickle"
gvcf5 = "../../" + sample5 + "/" + sample5 + "_4_HapCalled.g.vcf.gz"
pickle5 = sample5 + "/" + sample5 + ".pickle"
gvcf6 = "../../" + sample6 + "/" + sample6 + "_4_HapCalled.g.vcf.gz"
pickle6 = sample6 + "/" + sample6 + ".pickle"


# Define depth threshold
depththresh = 10

# Get the locations of all annotated genes
#geneloci = {'Sm_000000F':[['gene1','1',15']['gene2','345','456'],...]...}

if os.path.isfile("geneloci.pickle"):
	with open("geneloci.pickle", "rb") as infile:
		geneloci = pickle.load(infile)
	infile.close()
	print("Loaded list of gene loci.\n")
else:
	geneloci = {}

	with open(gfffile, 'r') as ingff:
		for line in ingff:
			if not line.startswith("#"):
				if line.split("\t")[2] == "gene":
					chrom = line.split("\t")[0]
					startpos = line.split("\t")[3]
					stoppos = line.split("\t")[4]
					genename = line.split("\t")[8].strip("ID=").strip("\n")
					print(genename)
					if not chrom in geneloci:
						geneloci[chrom] = []
					geneloci[chrom].append([genename,startpos,stoppos])
		ingff.close()
	with open("geneloci.pickle", "wb") as outfile:
		pickle.dump(geneloci, outfile)
	outfile.close()
	print("Gene loci list generated.\n")

# Make a list of all variant positions in both groups by parsing the two grouped VCFs
# variantpos = {'Sm_000000F':['1','5','7']...}

if os.path.isfile("variantpos.pickle"):
	with open("variantpos.pickle", "rb") as infile:
		variantpos = pickle.load(infile)
	infile.close()
	print("Loaded list of all variant positions.\n")

else:
	print("Generating list of all variant positions.")
	variantpos = {}

	for vcffile in [group1, group2]:
		start_time = time()
		print(vcffile)
		with gzip.open(vcffile, 'rt') as infile:
			for line in infile:
				if not line.startswith("#"):
					chrom = line.split("\t")[0]
					position = line.split("\t")[1]
					filter = line.split("\t")[6]

					if filter in ["PASS", "SnpCluster"]:
						if not chrom in variantpos:
							variantpos[chrom] = []
						if not position in variantpos[chrom]:
							variantpos[chrom].append(position)
		print("Done in " + str(round(time() - start_time, 1)) + " seconds.\n")

	for chrom in variantpos:
		variantpos[chrom].sort(key=int)

	with open("variantpos.pickle", "wb") as outfile:
		pickle.dump(variantpos, outfile)
	outfile.close()
	print("Variant list generated.\n")

#print(variantpos)


# Save all depth values, as well as all genotypes/alt bases
# Get separate dictionaries for each sample, to save time down the line when making multiple comparisons
# Per position, save depth, alt. allele, genotype
#statsdict = {'Sm_000000F':{'1':[["1","<NON_REF>","0/0"],["2","C,<NON_REF>", "0/1"],[],[],[],[]]...

def getfilestats(inputfile, outputfile):
	start_time = time()

	statsdict = {}

	with open(inputfile, 'r') as infile:
		for line in infile:
			if not line.startswith('#'):
				chrom = line.split("\t")[0]
				pos = line.split("\t")[1]
				altbase = line.split("\t")[4]
				genotype = line.split("\t")[9].split(":")[0]

				# Set depth to zero if it's problematic
				if len(line.split("\t")[8].split(":")) >= 3 and line.split("\t")[8].split(":")[2] == "DP":
					depth = int(line.split("\t")[9].split(":")[2])
				else:
					depth = "0"

				if not chrom in statsdict:
					statsdict[chrom] = {}
				statsdict[chrom][pos] = [depth,altbase, genotype]

		infile.close()
		print("Done in " + str(round(time() - start_time, 1)) + " seconds.\n")
	with open(outputfile, 'wb') as outfile:
		pickle.dump(statsdict, outfile)
	outfile.close()
	return(statsdict)

# Load/generate stats for sample 1
if os.path.isfile(pickle1):
	print("Loading stats dictionary for sample 1...")
	with open(pickle1, 'rb') as infile1:
		statsdict1 = pickle.load(infile1)
	infile1.close()
	print("Loaded.\n")
else:
	print("Generating sample stats for " + sample1 + ".")
	statsdict1 = getfilestats(gvcf1, pickle1)
	print("Generated sample stats for sample 1.\n")

# Load/generate stats for sample 2
if os.path.isfile(pickle2):
	print("Loading stats dictionary for sample 2...")
	with open(pickle2, 'rb') as infile2:
		statsdict2 = pickle.load(infile2)
	infile2.close()
	print("Loaded.\n")
else:
	print("Generating sample stats for " + sample2 + ".")
	statsdict2 = getfilestats(gvcf2, pickle2)
	print("Generated sample stats for sample 2.\n")

# Load/generate stats for sample 3
if os.path.isfile(pickle3):
	print("Loading stats dictionary for sample 3...")	
	with open(pickle3, 'rb') as infile3:
		statsdict3 = pickle.load(infile3)
	infile3.close()
	print("Loaded.\n")
else:
	print("Generating sample stats for " + sample3 + ".")
	statsdict3 = getfilestats(gvcf3, pickle3)
	print("Generated sample stats for sample 3.\n")

# Load/generate stats for sample 4
if os.path.isfile(pickle4):
	print("Loading stats dictionary for sample 4...")
	with open(pickle4, 'rb') as infile4:
		statsdict4 = pickle.load(infile4)
	infile4.close()
	print("Loaded.\n")
else:
	print("Generating sample stats for " + sample4 + ".")
	statsdict4 = getfilestats(gvcf4, pickle4)
	print("Generated sample stats for sample 4.\n")

# Load/generate stats for sample 5
if os.path.isfile(pickle5):
	print("Loading stats dictionary for sample 5...")
	with open(pickle5, 'rb') as infile5:
		statsdict5 = pickle.load(infile5)
	infile5.close()
	print("Loaded.\n")
else:
	print("Generating sample stats for " + sample5 + ".")
	statsdict5 = getfilestats(gvcf5, pickle5)
	print("Generated sample stats for sample 5.\n")

# Load/generate stats for sample 6
if os.path.isfile(pickle6):
	print("Loading stats dictionary for sample 6...")
	with open(pickle6, 'rb') as infile6:
		statsdict6 = pickle.load(infile6)
	infile6.close()
	print("Loaded.\n")
else:
	print("Generating sample stats for " + sample6 + ".")
	statsdict6 = getfilestats(gvcf6, pickle6)
	print("Generated sample stats for sample 6.\n")


# Now filter out any positions in the depth dictionary that don't have good coverage throughout the whole dataset
# goodloci = {'Sm_000000F':['1', '7', '16', '42', ...]}

with open(finalout, "w") as outfile:
	for chrom in variantpos:
		for pos in variantpos[chrom]:
			depth1 = statsdict1[chrom][pos][0]
			geno1 = statsdict1[chrom][pos][1:]
			depth2 = statsdict2[chrom][pos][0]
			geno2 = statsdict2[chrom][pos][1:]
			depth3 = statsdict3[chrom][pos][0]
			geno3 = statsdict3[chrom][pos][1:]
			depth4 = statsdict4[chrom][pos][0]
			geno4 = statsdict4[chrom][pos][1:]
			depth5 = statsdict5[chrom][pos][0]
			geno5 = statsdict5[chrom][pos][1:]
			depth6 = statsdict6[chrom][pos][0]
			geno6 = statsdict6[chrom][pos][1:]

			alldepths = [int(depth1), int(depth2), int(depth3), int(depth4), int(depth5), int(depth6)]
			allgenos = [geno1, geno2, geno3, geno4, geno5, geno6]

			# Make sure all depths are acceptable
			if "NA" in alldepths or min(alldepths) < depththresh:
				continue

			# Make sure the genotypes are the same within groups and different between groups
			elif (geno1 == geno2 == geno3) and (geno4 == geno5 == geno6) and (geno1 != geno4):
				thislocus = []
				for locus in geneloci[chrom]:
					if int(pos) in range(int(locus[1]),int(locus[2]) + 1):
						thislocus.append(locus[0])
				outfile.write(chrom + "\t" + pos + "\t" + geno1[0] + "\t" + geno1[1] + "\t" + geno4[0] + "\t" + geno4[1] + "\t" + ",".join(thislocus) + "\n")
outfile.close()

print("Done")
