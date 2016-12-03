#!/usr/bin/python

import sys

from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

cds_file = open(sys.argv[1],'r')
aminoAcid_file = open(sys.argv[2],'w')

for line in cds_file:
	line = line.strip()
	line = line.split()
	if line[0] != '>':
		# Biopython methods don't modify Seq objects they simply return
		# Seqs so that's why I override objects
		dna_sequence = Seq(''.join(line),IUPAC.unambiguous_dna)
		dna_sequence = dna_sequence.reverse_complement()
		rna_sequence = dna_sequence.transcribe()
		protein_sequence = rna_sequence.translate()
		aminoAcid_file.write(str(protein_sequence)+'\n')
	else:
		aminoAcid_file.write(''.join(line)+'\n')


cds_file.close()
aminoAcid_file.close()
