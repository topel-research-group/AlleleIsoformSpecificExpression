#!/usr/bin/env Rscript

library("topGO")

args = commandArgs(trailingOnly=TRUE)

infile <- args[1]

# Tab-separated file of gene ID (Sm_...) and associated GO terms

geneID2GO <- readMappings("../R05_v1.1.9.GOterms.AllGenes.tsv")
geneNames <- names(geneID2GO)

interesting_genes <- as.character(read.csv(infile, header=FALSE)$V1)
geneList <- factor(as.integer(geneNames %in% interesting_genes))
names(geneList) <- geneNames

GOdata <- new("topGOdata", ontology = "BP", allGenes = geneList,
	annot = annFUN.gene2GO, gene2GO = geneID2GO)
resultFis <- runTest(GOdata, algorithm = "classic", statistic = "fisher")
allRes <- GenTable(GOdata, classic = resultFis, orderBy = "weight",
	ranksOf = "classic", topNodes = 1000)
write.table(allRes, paste0("GO.", infile), quote = FALSE, sep = "\t", row.names = FALSE)

