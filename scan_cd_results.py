#!/usr/bin/env python

import sys

file = open(sys.argv[1],'r')

string = "***** No hits found *****"
resultsCount = 0
for line in file:
	if string not in line:
		continue
	else:
		resultsCount +=1

file.close()

with open(sys.argv[2],"a") as myfile:
	myfile.write(str(resultsCount) + "\n")

myfile.close()

#print "no results count " + str(resultsCount)



