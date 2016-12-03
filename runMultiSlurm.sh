#!/bin/bash
X=19840
TOTAL=19841
#19840 total cds for H_Sapiens
while [ $X -lt $TOTAL ]
do
	PBS=bash_scripts/bash_$X.txt 
	cp runMultiProteinsTemplate.sh $PBS
 
	echo -n "/fslhome/lpinto/fsl_groups/fslg_RidgeLab/compute/software/blast/ncbi-blast-2.2.31+/bin/rpsblast \
		-query /fslhome/lpinto/fsl_groups/fslg_RidgeLab/lucas/conserved_domain_stuff/proteins/protein_${X}.txt \
		-db /fslhome/lpinto/fsl_groups/fslg_RidgeLab/compute/conserved_domain/ftp.ebi.ac.uk/pub/databases/Pfam/releases/Pfam28.0/smp_files/Pfam28 \
			-evalue 0.001 \
				-out /fslhome/lpinto/fsl_groups/fslg_RidgeLab/lucas/conserved_domain_stuff/blasted_proteins_eval_001/blasted_protein_${X}.txt" >> $PBS
	sbatch -C avx $PBS
	X=$((X+1))					
done
