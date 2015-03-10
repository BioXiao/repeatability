#Tessa Pierce
#5.31.2013

# $1 = input bam file
# $2 = genes of interest (bed file)

bedtools intersect -abam $1 -b $2 -wb -bed > $3 &



