#2.25.2014, modified from https://groups.google.com/forum/#!topic/bedtools-discuss/PyHsfXHuFm0
#9.26.2014, modified for tigriopus orthologs

library(ggplot2)

# Load our hists
covSD <- read.table('/ni2/sio296/squid/tigriopus/orthologous_contigs/one_orthologs.coverage')
covBR <- read.table('/ni2/sio296/squid/tigriopus/orthologous_contigs/two_orthologs.coverage')
covAB <- read.table('/ni2/sio296/squid/tigriopus/orthologous_contigs/three_orthologs.coverage')
covSCN <- read.table('/ni2/sio296/squid/tigriopus/orthologous_contigs/four_orthologs.coverage')
covPES <- read.table('/ni2/sio296/squid/tigriopus/orthologous_contigs/five_orthologs.coverage')
covBB <- read.table('/ni2/sio296/squid/tigriopus/orthologous_contigs/six_orthologs.coverage')

# Create a cumulative distribution from the "raw" hist (truncate at depth >=50)
covSDc = 1 - cumsum(covSD[,5])
covBRc = 1 - cumsum(covBR[,5])
covABc = 1 - cumsum(covAB[,5])
covSCNc = 1 - cumsum(covSCN[,5])
covPESc = 1 - cumsum(covPES[,5])
covBBc = 1 - cumsum(covBB[,5])

# Create a plot of the cumul
pdf('/ni2/sio296/squid/tigriopus/orthologous_contigs/orthologs_coverage.pdf')
#plot(cov[2:51,2], covC[1:50],  type='b', lwd=2, xlab="Depth", ylab="Fraction of transcriptome >= depth", main="Transcriptome Coverage", xaxt="n", yaxt="n")
#par(new=T)
#pdf('/ni2/sio296/squid/transcriptome_metrics/h082_good_nonrmdup_repaired.seed22_N1_ref_h082_highQ_trinity_sorted.coverage_plot_annot_only.pdf')
plot(covSD[2:51,2], covSDc[1:50], col='darkblue', type='b', lwd=2, pch =2, xlab="Depth", ylab="Fraction of transcriptome >= depth", main="Transcriptome Coverage", xaxt="n", yaxt="n")
par(new=F)

# Draw the axis labels for the x (1) and y (2) axes
axis(1,at=c(1,5,10,15,20,25,30,35,40,45,50))
axis(2,at=c(0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0))

# add dashed vertical lines.
abline(v=c(1,5,10,15,20,25,30,35,40,45,50),lty=3,col="grey") 

# add dash horizontal lines
abline(h=c(0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0),lty=3,col="grey") 

dev.off()

