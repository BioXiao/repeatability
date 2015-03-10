#Tessa Pierce
#9.30.12

import sys

inCounts = open(sys.argv[1], 'r')
outCounts= open(sys.argv[2], 'w')
countThreshold = int(sys.argv[3])

count_lines = [ x.strip().split('\t') for x in inCounts.readlines() ]

countsDt = {}
headerLine = count_lines[0]
for line in count_lines[1: ]:
    key = line[0]
    dlte = False
    #no_scn_line = line[1:9] + line[10:]
    count_list = []
    #for count in no_scn_line:
    for count in line[1:]:
	count = int(float(count)) 
	if count > countThreshold: #keep any contig with a count number > than countThreshold
	    count_list.append(count)
	else:
	    dlte = True
    if not dlte:
	countsDt[key] = count_list


outCounts.write('\t'.join(headerLine) + '\n')

for key, val in countsDt.items():
    outCounts.write(key + '\t' + '\t'.join(map(str,val)) + '\n')


inCounts.close()
outCounts.close()

