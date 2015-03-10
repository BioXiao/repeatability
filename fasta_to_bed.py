#Tessa Pierce
# 2.8.13
# modified for orthologs 9.26.2014

#Input - fasta file
#Output - basic BED file ( chr_name + '\t' + start_pos + '\t' + end_pos )


import sys, re

in_fasta = open(sys.argv[1], 'r')
out_BED = open(sys.argv[2], 'w')


fasta_lines = in_fasta.readlines()

#info = re.compile('^>(\S*) len=(\d*)')
#info = re.compile('^>(\S*) (\d*)')
info = re.compile('^>(\S*)')
start_pos = str(0) # BED files: start is 0-indexed, end is 1-indexed
end_pos = 0
contig_info = None


for line in fasta_lines:
    if line.startswith('>'):
        if contig_info is not None:
	    out_BED.write(contig_name+ '\t' + start_pos + '\t' + str(end_pos) + '\n')	
	    contig_info = None
	    end_pos = 0
	contig_info = info.match(line)
        contig_name = contig_info.groups()[0] # for re.compile('^>(\S*)')
            #contig_name, end_pos = contig_info.groups()
    else:
        end_pos = end_pos + len(line)
    


in_fasta.close()
out_BED.close()

sys.exit()





