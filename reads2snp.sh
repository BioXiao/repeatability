# 1.12.2015

# general format:
#reads2snp -bam <file_to_run.bam> -bamref <reference_transcriptome>

#with options:
#-min 30 # desired coverage
#-nbth  (Number of processors)
#-spa (no number after this flag)
#-bqt 20
#-rqt 20


./reads2snp_2.0.64.bin -bam ${1} -bamref ${2} -min 30 -nbth 16 -spa -bqt 20 -rqt 20 & # coverage 30

## just checking:
###./reads2snp_2.0.64.bin -bam ${1} -bamref ${2} -min 1 -nbth 8 -spa -bqt 20 -rqt 20 & # coverage 1



