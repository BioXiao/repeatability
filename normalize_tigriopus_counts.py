#Tessa Pierce
#2.8.13

#Normalize counts in the count matrix exported by remove_low_counts.py

#count matrix: contig \t sd2c \t sd3c \t br1c \t br2c \t ab1c \t ab2c \t scn1c \t scn2c \t pes1c \t pes2c \t bb1c \t bb2c \n

##RPKM = reads per kilobase per million mapped reads
import sys
#import numpy as np

from optparse import OptionParser

desc = """ This is a script that reads in a count table for the six populations and normalizes the counts by the lengths of the contigs relative to the SD length.  
"""
parser = OptionParser(description = desc)

### Contig Name Conversion Table ###
parser.add_option("--counts", "--inCountsTable", help = "name of the input counts file", action = "store", type = "string", dest="counts")

parser.add_option("--cnv", "--Conversion", help = "name of the Contig Conversion table", action="store", type="string", dest="conversion")

### Output File ###
parser.add_option("--out", "--OutCountsTable", help = "name of the Output Counts Table File" , action="store", type="string", dest="out")

# Directory for Counts files and Output file #
parser.add_option("--dir", "--Directory", help = "path to all input files" , action="store", type="string", dest="path")

########input number of files for each population
parser.add_option("--sd", "--numSanDiego", help = "number san diego columns", action="store", type="int", dest="sd")
parser.add_option("--scn", "--numSantaCruz", help = "number of santa cruz columns", action="store", type="int", dest="scn")
parser.add_option("--pes", "--numPescadero", help = "number of pescadero columns", action="store", type="int", dest="pes")
parser.add_option("--bb", "--numBodegaBay", help = "number of bodega bay columns", action="store", type="int", dest="bb")
parser.add_option("--ab", "--numAbaloneCove", help = "number of abalone cove columns", action="store", type="int", dest="ab")
parser.add_option("--br", "--numBirdRock", help = "number of bird rock columns", action="store", type="int", dest="br")

(opts, args) = parser.parse_args()

inCounts = open(opts.counts, 'r')
conversionFile = open(opts.conversion, 'r') #same conversion table used to convert the contig names
outNorm = open(opts.out, 'w')

counts_per_sd_contig = [ x.strip().split('\t') for x in inCounts.readlines() ]
conversionTable = [ x.strip().split('\t') for x in conversionFile.readlines() ]

#functions
def createLengthConversionDt(conversion, columns):
    lengthDt = {} 
    for line in conversion:
        contig = 'SD' + line[0]
	sdLen = line[1]
	brLen = line[3]
	abLen = line[5]
	scnLen = line[7]
	pesLen = line[9]
	bbLen = line[11]
	lenList = []	# need to iterate through column list, if has sd = sd Len, etc
	for col in columns:
	    if col == "sd":
		lenList.append(sdLen)
	    elif col == "br":
		lenList.append(brLen)
	    elif col == "ab":
		lenList.append(abLen)
	    elif col == "scn":
		lenList.append(scnLen)
	    elif col == "pes":
		lenList.append(pesLen)
	    elif col == "bb":
		lenList.append(bbLen)
	lengthDt[contig] = lenList #dynamically maps to the # of files you used for each population (input those numbers in the options above)
    return lengthDt


def mapPopsToColumns(colsToAdd, popName, cols):
    i = 0 
    popName = str(popName)
    while i < colsToAdd:
	cols.append(popName)
	i = i + 1
    return cols

def normalizeCounts(inCounts, lengthConversion):
    normDt = {}
    for line in inCounts:
        contigName = line[0]
        contigLengths = lengthConversion.get(contigName) 
        contigLengths = [float(item) for item in contigLengths]
        counts = line[1:] # get all counts
        counts = [float(list_item) for list_item in counts]
        counts_per_bp =[a/b for a,b in zip(counts,contigLengths)] #divide each count by it's population's reference contig length
        RPK = [x*1000 for x in counts_per_bp]  # multiply each of these length-normalized counts by 1000 .. or [x for x in counts_per_bp] if don't want to multiply
        normDt[contigName] = RPK 
    return normDt

#main
#map populations back to the columns
columnList = mapPopsToColumns(opts.sd, "sd", [])
columnList = mapPopsToColumns(opts.br, "br", columnList)
columnList = mapPopsToColumns(opts.ab, "ab", columnList)
columnList = mapPopsToColumns(opts.scn, "scn", columnList)
columnList = mapPopsToColumns(opts.pes, "pes", columnList)
columnList = mapPopsToColumns(opts.bb, "bb", columnList)

lengthConversionDt = createLengthConversionDt(conversionTable, columnList)
headerLine = counts_per_sd_contig[0]

#create RPK dictionary of normalized counts
RPK_Dt = normalizeCounts(counts_per_sd_contig[1:], lengthConversionDt)

# write out header line
outNorm.write('\t'.join(headerLine) + '\n')

# write out normalized (RPK) counts
for key, val in RPK_Dt.items():
    outNorm.write(key + '\t' + '\t'.join(map(str,val)) + '\n')


inCounts.close()
conversionFile.close()
outNorm.close()

sys.exit()


