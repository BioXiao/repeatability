#Tessa Pierce
#6.2.2013

# take a count table ([0] contig name [1] count), convert the contig name to it's SD population equivalent, and place the counts in a large table containing all populations.

# new parameters: 1. number of populations with 

import sys, re, os

# Input arguments via optparse (works with Python 2.5, which is on the server. Python 2.7 plus prefer argparse...)
from optparse import OptionParser

desc = """ This is a script that reads in individual count files for each population, uses a Contig conversion table to convert all contig names to their San Diego equivalents, and prints out a master table of the counts by population.  
"""
parser = OptionParser(description = desc)

### Contig Name Conversion Table ###
parser.add_option("--cnv", "--Conversion", help = "name of the Contig Conversion table", action="store", type="string", dest="conversion")

### Output File ###
parser.add_option("--out", "--OutCountsTable", help = "name of the Output Counts Table File" , action="store", type="string", dest="out")

# Directory for Counts files and Output file #
parser.add_option("--dir", "--Directory", help = "path to all input files" , action="store", type="string", dest="path")


parser.add_option("--sd", "--SanDiego", help = "names of San Diego counts files", action="append", type="string", dest="sd")
parser.add_option("--scn", "--SantaCruz", help = "names of Santa Cruz counts files", action="append", type="string", dest="scn")
parser.add_option("--pes", "--Pescadero", help = "names of Pescadero counts files", action="append", type="string", dest="pes")
parser.add_option("--bb", "--BodegaBay", help = "names of Bodega Bay counts files", action="append", type="string", dest="bb")
parser.add_option("--ab", "--AbaloneCove", help = "names of Abalone Cove counts files", action="append", type="string", dest="ab")
parser.add_option("--br", "--BirdRock", help = "names of Bird Rock counts files", action="append", type="string", dest="br")

(opts, args) = parser.parse_args()

os.chdir(opts.path)
inConversion = open(opts.conversion, 'r')
outCountTable = open(opts.out, 'w')

#read in conversion table

conversionLines =  [ x.strip().split('\t') for x in inConversion.readlines() ]

# function to read in a single counts file
def readTSV (filename):
    inLines = [ x.strip().split('\t') for x in filename.readlines() ]
    return inLines

# create the conversion table
def createConversions(conversion): 
    SD, BR, AB, SCN, PES, BB, TableDt = {}, {}, {}, {}, {}, {}, {}
    for line in conversion:
	SanDiego = line[0]
	sd, br, ab, scn, pes, bb = line[0], line[2], line[4], line[6], line[8], line[10]
        SD[sd] = SanDiego
	BR[br] = SanDiego
	AB[ab] = SanDiego
	PES[pes] = SanDiego
	SCN[scn] = SanDiego
	BB[bb] = SanDiego
        TableDt[SanDiego] = [0] * numFiles
    return SD, BR, AB, SCN, PES, BB, TableDt

# add counts from a specific population to the counts conversion
     #### NOTE: since we initialized all values in the table to 0, if a contig doesn't show up in a population, it's value will simply remain zero. This gives us all possible data - we then filter out contigs with zeros or counts below a specified threshold via a different script to obtain the final list for Differential Expression

def addToTable(popConversion, popFile, popIndex, TableDt):
    popInfo = readTSV(popFile)
    for line in popInfo:
	if line[0] in popConversion:
	    SDequiv = popConversion.get(line[0])
	    counts = line[1]
	    if SDequiv in TableDt:
		counts_list = TableDt.get(SDequiv)
		counts_list[popIndex] = counts
	        TableDt[SDequiv] = counts_list 


def addAPop(popConversion, popFileList, index, countsdt):
    i = 0
    while i < len(popFileList):
	headerList.append(popFileList[i])
	inF = open(popFileList[i], 'r')
        addToTable(popConversion, inF, index, countsdt)
        i = i + 1
        index = index + 1
        inF.close()
    return index, CountsDt, headerList


#main
numFiles = len(opts.sd) + len(opts.br) + len(opts.ab) + len(opts.scn) + len(opts.pes) + len(opts.bb) # count input files to create right size empty countsTable
SD, BR, AB, SCN, PES, BB, CountsDt = createConversions(conversionLines)
tableIndex = 0
headerList = []
tableIndex, CountsDt, headerList = addAPop(SD, opts.sd, tableIndex, CountsDt) 
tableIndex, CountsDt, headerList = addAPop(BR, opts.br, tableIndex, CountsDt) 
tableIndex, CountsDt, headerList = addAPop(AB, opts.ab, tableIndex, CountsDt) 
tableIndex, CountsDt, headerList = addAPop(SCN, opts.scn, tableIndex, CountsDt) 
tableIndex, CountsDt, headerList = addAPop(PES, opts.pes, tableIndex, CountsDt) 
tableIndex, CountsDt, headerList = addAPop(BB, opts.bb, tableIndex, CountsDt) 

#print header list
outCountTable.write('Contig' + '\t' + '\t'.join(headerList) + '\n')

# write out the table
for key, val in CountsDt.items():
    outCountTable.write('SD' + key + '\t' + '\t'.join(map(str,val)) + '\n')


inConversion.close()
outCountTable.close()



