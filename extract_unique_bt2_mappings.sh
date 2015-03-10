#Tessa Pierce
#2.8.13


#input bam file
#samtools view $1.bam | grep -v XS:i: > $1_unique.sam &

#input sam file
#grep -v XS:i: ${1}.sam > ${1}_unique.sam &
#rm -rf ${1}_unique.sam &
######### IF HEADER IS MISSING ##############
#get header from sam
#samtools view -SH $1.sam > $1_head.sam &

#get header from bam
#samtools view -H $1.bam > $1_head.sam &

# cat header to unique file
#cat $1_head.sam $1_unique.sam > $1_unique_H.sam & 


########## CONVERT TO BAM #############
#convert sam to bam, keeping the unique and full bam files

####samtools view -Sb ${1}_unique_H.sam > ${1}_unique.bam & # when need to add header
#rm -rf  ${1}_unique.bam #  ${1}.bam & #(remove files if need to re-run)
#samtools view -Shb ${1}_unique.sam > ${1}_unique.bam &
#samtools view -Shb ${1}.sam > ${1}.bam &

#sort and index the bam file (optional)
#samtools sort $1_unique.bam $1_unique_sorted &
samtools index $1_unique_sorted.bam &

######### CLEANUP ############
# remove all sam files

 #rm -rf  ${1}*.sam



