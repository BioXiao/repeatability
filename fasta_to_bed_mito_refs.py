#Tessa Pierce
# 2.8.13


#Input - fasta file
#Output - basic BED file ( chr_name + '\t' + start_pos + '\t' + end_pos )


import sys, re

in_fasta = open(sys.argv[1], 'r')
out_BED = open(sys.argv[2], 'w')


fasta_lines = in_fasta.readlines()
fastaDt = {}
bp = 0
contig_name = re.compile('^>(\S*)')
start_pos = str(0) # BED files: start is 0-indexed, end is 1-indexed

for line in fasta_lines:
    if line.startswith('>'):
        if bp > 0:
            fastaDt[name] = bp
            bp = 0
        name = re.match(contig_name, line).groups()[0]
    else:
        bp = bp + len(line)


for fasta, length in fastaDt.items():
    out_BED.write(fasta +  '\t' + start_pos + '\t' + str(length) + '\n')


in_fasta.close()
out_BED.close()

sys.exit()





