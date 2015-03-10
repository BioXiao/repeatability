# Tessa Pierce

import sys

inOrthologTable = open(sys.argv[1], 'r')
outF = open(sys.argv[2], 'w')


orthoTable = [ x.strip().split('\t') for x in inOrthologTable.readlines() ]

for line in orthoTable:
    names = line[::2]
    lengths = line[1::2]
    lengthsFloat = [float(x) for x in lengths] # convert lengths to int
    maxLen = max(lengthsFloat)
    minLen = min(lengthsFloat)
    maxBpDiff = str(maxLen -minLen)
    refLength = lengthsFloat[0] # if using sd as the reference length
    percLengths =[str((x/refLength)*100) for x in lengthsFloat]
    lists = [names, lengths, percLengths]
    full_info = [x for y in zip(*lists) for x in y]
    outF.write('\t'.join(full_info) + '\t' + maxBpDiff + '\n' ) 

inOrthologTable.close()
outF.close()
 


