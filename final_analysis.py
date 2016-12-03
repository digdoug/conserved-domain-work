#!/usr/bin/python

import sys
import linecache


resultsFile = open("resultsFile_eval_01.txt",'r')
#protein_file = open(,'r')
gene_file = "H_sapiens_genes_only"

new_results_file = open("protein_genes_hits.txt",'w')


resultsFile_line_counter = 0

for line in resultsFile:
	resultsFile_line_counter += 1
	line = line.strip()
	if line == "0": # a hit
		#grab line in protein file
		tmp_protein_fileName = "proteins/protein_" + str(resultsFile_line_counter) + ".txt"
		#protein_file = open(tmp_protein_fileName,'r')
		protein_line = linecache.getline(tmp_protein_fileName,2)
		#grab line in gene file
		gene_line = linecache.getline(gene_file,resultsFile_line_counter)
		
		#output file
		new_results_file.write(protein_line + gene_line)

resultsFile.close()
#gene_file.close()
new_results_file.close()
