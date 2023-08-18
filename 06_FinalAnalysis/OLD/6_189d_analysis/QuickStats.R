#!/usr/bin/env Rscript

file1="P18257_138.bias.GoodCov.tsv"
file2="P18257_139.bias.GoodCov.tsv"

infile1 <- read.table(file1, header=F,
		col.names=c("gene", "bias1", "note"), sep="\t", fill=T, stringsAsFactors=F)

infile2 <- read.table(file2, header=F,
		col.names=c("gene", "bias2", "note"), sep="\t", fill=T, stringsAsFactors=F)

alldata <- data.frame(infile1$gene, as.numeric(infile1$bias1), as.numeric(infile2$bias2))

colnames(alldata) <- c("gene", "bias1", "bias2")

row_means <- apply(alldata[, -1], 1, mean)
alldata$mean <- row_means

row_sd <- apply(alldata[,2:3], 1, sd)
alldata$SD <- row_sd

# How many contain no NAs?
noNAs <- alldata[rowSums(is.na(alldata[,2:3])) == 0,]
print(paste0("No NAs: ", nrow(noNAs)))

# How many contain at least 1-2 NA?
someNAs <- alldata[rowSums(is.na(alldata[,2:3])) == 1,]
print(paste0("Some NAs: ", nrow(someNAs)))

# How many contain all NAs?
allNAs <- alldata[rowSums(is.na(alldata[,2:3])) == 2,]
print(paste0("All NAs: ", nrow(allNAs)))

# Biallelic expression
bae <- noNAs[noNAs$mean <= 20,]
print(paste0("BAE: ", nrow(bae)))
writeLines(as.character(bae$gene), "R05_189d_BAE.lst")

# Allele-specific expression
ase <- noNAs[noNAs$mean > 20 & noNAs$mean <= 60,]
print(paste0("ASE: ", nrow(ase)))
writeLines(as.character(ase$gene), "R05_189d_ASE.lst")

# Monoallelic expression
mae <- noNAs[noNAs$mean > 60,]
print(paste0("MAE: ", nrow(mae)))
writeLines(as.character(mae$gene), "R05_189d_MAE.lst")

#noNAs[order(noNAs$mean),]
#Can also use decreasing=T
