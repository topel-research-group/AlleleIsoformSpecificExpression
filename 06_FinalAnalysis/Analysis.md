# Check the spread of replicate results for outliers

```
# Low-coverage genes have already been filtered out
# 11,073 / 17,087 genes included

infile1 <- read.table("P18257_101.bias.GoodCov.tsv", header=F,
		col.names=c("gene", "bias1", "note"), sep="\t", fill=T, stringsAsFactors=F)

infile2 <- read.table("P18257_102.bias.GoodCov.tsv", header=F,
		col.names=c("gene", "bias2", "note"), sep="\t", fill=T, stringsAsFactors=F)

infile3 <- read.table("P18257_103.bias.GoodCov.tsv", header=F,
		col.names=c("gene", "bias3", "note"), sep="\t", fill=T, stringsAsFactors=F)

alldata <- data.frame(infile1$gene, as.numeric(infile1$bias1),
			as.numeric(infile2$bias2), as.numeric(infile3$bias3))


colnames(alldata) <- c("gene", "bias1", "bias2", "bias3")

row_means <- apply(alldata[, -1], 1, mean)
alldata$mean <- row_means

row_sd <- apply(alldata[,2:4], 1, sd)
alldata$SD <- row_sd

# How to identify genes with monoallelic expression?
## These seem to appear as NAs in the table
## And how to distinguish these from genes in homozygous stretches of the genome?





# How many contain all NAs?
sum(rowSums(is.na(alldata[,2:4])) == 3)			# 1,387 contain all NAs
allNAs <- alldata[rowSums(is.na(alldata[,2:4])) == 3,]

# How many contain at least one NA?
sum(rowSums(is.na(alldata[,2:4])) > 0)			# 1.600 with at least one NA
someNAs <- alldata[rowSums(is.na(alldata[,2:4])) > 0,]
someNAs <- alldata[rowSums(is.na(alldata[,2:4])) %in% c(1,2),]

# No NAs, for completeness
sum(rowSums(is.na(alldata[,2:4])) == 0)			# 9,473
noNAs <- alldata[rowSums(is.na(alldata[,2:4])) == 0,]

# Sorting the dataframe

noNAs[order(noNAs$mean),]	# Can also use decreasing=T



########

# Plotting

alldata$gene <- gsub('Sm_g','', alldata$gene)

plot(alldata$gene,alldata$bias1, xlim=c(0,50))
points(alldata$gene, alldata$bias2)
points(alldata$gene, alldata$bias3)
```
