#Tessa Pierce

## Contigs that are merged from other contigs during Cap3 run are given the name "Contig1" etc .. when we run cap3 a second time, we don't want any contigs to have the same name ... so just rename them by adding "_cap3_contigs" at the end of each one"

import sys

contigsIN = open(sys.argv[1], 'r')
contigsOUT= open(sys.argv[2], 'w')

contigLines = [ x.strip() for x in contigsIN.readlines() ]

for line in contigLines:
    if line.startswith('>'):
        contigsOUT.write(line + '_cap3_contigs' + '\n')
    else:
        contigsOUT.write(line + '\n' )


contigsIN.close()
contigsOUT.close()


