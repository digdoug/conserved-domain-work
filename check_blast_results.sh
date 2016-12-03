#!/bin/bash


for filename in blasted_proteins/*.txt; do 
		./scan_cd_results.py "$filename" "resultsFile.txt" 
done

