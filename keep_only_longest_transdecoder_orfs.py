##################################################################
####     Tessa Pierce
#### https://github.com/bluegenes/
#### 5.30.2013, edited 12.5.2014 and 1.13.2015
###################################################################
"""Function: take in a transdecoder.pep file and keep only the longest orf per contig
"""
###################################################################

import sys, re

transDpep = open(sys.argv[1], 'r')
outReport = open(sys.argv[2], 'w')

transDpepLines = [ x.strip() for x in transDpep ]

getLen = re.compile('len:(\d*)')

# initialize some vars
longestORFline = ''
longestLen     = 0

for line in transDpepLines:    
    if line.startswith('>'):
	currentLen = float(re.search(getLen, line).groups()[0])
	currentContig = line.split('|')[0][5:]
	if len(longestORFline) < 1: # only happens w first contig
	    longestORFname = currentContig
	    longestORF_AAs = ''
	if currentContig == longestORFname:
	    if currentLen >= longestLen:
	        longestLen = currentLen
	        longestORFline = line
		getAA = True
	    else:
	        getAA = False
	else:
	    outReport.write(longestORFline + '\n' + longestORF_AAs + '\n')
	    longestORFline = line
	    longestLen = currentLen
            longestORFname= currentContig
	    longestORF_AAs = ''
            getAA = True
    elif getAA:
        longestORF_AAs = longestORF_AAs + line

#catch last one
outReport.write(longestORFline + '\n' + longestORF_AAs + '\n')


transDpep.close()
outReport.close()

