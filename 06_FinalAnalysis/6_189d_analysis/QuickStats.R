#!/usr/bin/env Rscript

library(dplyr)

options(width=100)

sample1 <- "P18257_138"
sample2 <- "P18257_139"

outtsv <- "R05_189d.Results.tsv"

#####

file1=paste0("infiles/", sample1, ".bias.v2.tsv")
file2=paste0("infiles/", sample2, ".bias.v2.tsv")

infile1 <- read.table(file1, header=F,
		col.names=c("gene", "bias1", "note1"), sep="\t", fill=T, stringsAsFactors=F)

infile2 <- read.table(file2, header=F,
		col.names=c("gene", "bias2", "note2"), sep="\t", fill=T, stringsAsFactors=F)

alldata <- data.frame(infile1$gene, as.character(infile1$bias1), as.character(infile2$bias2),
				infile1$note1, infile2$note2)

colnames(alldata) <- c("gene", "bias1", "bias2", "note1", "note2")

## How many genes contain no variants?

print(paste0("No genomic variants: ",
	nrow(alldata %>%
	filter(bias1 == 'No variants' | bias2 == 'No variants' |
		note1 == 'No variants' | note2 == 'No variants'))))

alldata <- alldata %>%
		filter(bias1 != 'No variants' & bias2 != 'No variants' &
			note1 != 'No variants' & note2 != 'No variants')

## How many genes have too much allelic frequency bias?

print(paste0("Too much genomic bias: ",
	nrow(alldata %>%
	filter(note1 == 'Too much bias' | note2 == 'Too much bias'))))

alldata <- alldata %>%
		filter(note1 != 'Too much bias' & note2 != 'Too much bias')

## How many genes have bad coverage across all samples?

print(paste0("All bad coverage: ",
	nrow(alldata %>%
	filter(bias1 == 'Bad cov' & bias2 == 'Bad cov'))))

alldata <- alldata %>%
		filter(!(bias1 == 'Bad cov' & bias2 == 'Bad cov'))

## How many genes have bad coverage across two samples?

print(paste0("One bad coverage: ", sum(rowSums(alldata[, c('bias1', 'bias2')] == 'Bad cov') == 1)))

alldata <- subset(alldata, rowSums(alldata[, c('bias1', 'bias2')] == 'Bad cov') == 0)

## Convert all instances of 'Monoallelic' to 100
alldata[, c('bias1')] <- gsub('Monoallelic', '100', alldata[, c('bias1')])
alldata[, c('bias2')] <- gsub('Monoallelic', '100', alldata[, c('bias2')])

# Convert 'bias' columns to numeric
alldata$bias1 <- as.numeric(alldata$bias1)
alldata$bias2 <- as.numeric(alldata$bias2)

# Get the mean and standard deviation
alldata$mean <- rowMeans(alldata[,2:3], na.rm = T)
alldata$SD <- apply(alldata[, 2:3], 1, sd, na.rm = T)

##### Preliminary figures

# Biallelic expression
bae <- alldata[alldata$mean <= 20,]
print(paste0("BAE: ", nrow(bae)))
#writeLines(as.character(bae$gene), "R05_0d_BAE.lst")

# Allele-specific expression
ase <- alldata[alldata$mean > 20 & alldata$mean <= 60,]
print(paste0("ASE: ", nrow(ase)))
#writeLines(as.character(ase$gene), "R05_0d_ASE.lst")

# Monoallelic expression
mae <- alldata[alldata$mean > 60,]
print(paste0("MAE: ", nrow(mae)))
#writeLines(as.character(mae$gene), "R05_0d_MAE.lst")

alldata <- alldata[order(alldata$gene),]

outframe <- alldata[, c("gene", "bias1", "bias2", "mean", "SD")]

write.table(outframe, outtsv, quote=F, sep="\t", row.names=F)
