#!/usr/bin/python

import sys


cds_file = open(sys.argv[1],'r')

protein = 1
counter = 0
filestring = ''
for line in cds_file:
	counter += 1
	filestring += line
	if counter == 2:
		fileName = "proteins/protein_" + str(protein) + ".txt"
		new_file = open(fileName, 'w')
		new_file.write(filestring)
		counter = 0
		filestring = ''
		new_file.close()
		protein += 1		
	


cds_file.close()

