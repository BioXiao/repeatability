#Tessa Pierce
#9.29.2014


# Script to normalize a count matrix by length and library size

import sys, os
from optparse import OptionParser

desc = """ Script to normalize a count matrix by length and library size
"""
parser = OptionParser(description = desc)

### Contig Name Conversion Table ###
parser.add_option("--cnv", "--Conversion", help = "name of the Contig Conversion table", action="store", type="string", dest="conversion")

### Output File ###
parser.add_option("--out", "--OutNormalizedTable", help = "name of the Output Normalized Counts Table File" , action="store", type="string", dest="out")

# Directory for Counts files and Output file #
parser.add_option("--dir", "--Directory", help = "path to all input files" , action="store", type="string", dest="path")

# Input Counts File
parser.add_option("--counts", "--CountsTable", help = "input counts table", action="store", type="string", dest="counts")

#Library Sizes
########input number of files for each population
parser.add_option("--sd", "--numSanDiego", help = "number san diego mapped reads", action="store", type="float", dest="sd")
parser.add_option("--scn", "--numSantaCruz", help = "number of santa cruz mapped reads", action="store", type="float", dest="scn")
parser.add_option("--pes", "--numPescadero", help = "number of pescadero mapped reads", action="store", type="float", dest="pes")
parser.add_option("--bb", "--numBodegaBay", help = "number of bodega bay mapped reads", action="store", type="float", dest="bb")
parser.add_option("--ab", "--numAbaloneCove", help = "number of abalone cove mapped reads", action="store", type="float", dest="ab")
parser.add_option("--br", "--numBirdRock", help = "number of bird rock mapped reads", action="store", type="float", dest="br")


(opts, args) = parser.parse_args()

os.chdir(opts.path)
inCounts = open(opts.counts, 'r')
inConversion = open(opts.conversion, 'r')
outCountTable = open(opts.out, 'w')

sdLibSize = opts.sd
library_size_conversion = [1, opts.br/sdLibSize, opts.ab/sdLibSize, opts.scn/sdLibSize, opts.pes/sdLibSize, opts.bb/sdLibSize]

#read in conversion table

conversionLines =  [ x.strip().split('\t') for x in inConversion.readlines() ]
#read in counts table
countsIN = [ x.strip().split('\t') for x in inCounts.readlines() ]

convDt ={}
for line in conversionLines:
    convDt[line[0]] = [float(line[1]),float(line[3]), float(line[5]), float(line[7]), float(line[9]), float(line[11])] #get lengths of all contigs

outCountTable.write("Contig" + '\t' + '\t'.join(countsIN[0]) + '\n')

for line in countsIN[1:]:
    contigName = line[0][2:]
    counts = [float(a) for a in line[1:]] #,sdCounts,brCounts,abCounts,scnCounts,pesCounts,bbCounts = line
    contigLengths = convDt.get(contigName)
    normalizeLen = [(a/b)*contigLengths[0] for a,b in zip(counts,contigLengths)] # normalize to sd length
    normalizeLib = [a*b for a,b in zip(normalizeLen,library_size_conversion)]
    outCountTable.write(contigName + '\t' + '\t'.join(map(str,normalizeLib)) + '\n')
    

inCounts.close()
inConversion.close()
outCountTable.close()










