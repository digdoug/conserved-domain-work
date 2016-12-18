# conserved-domain-work
I made a BLAST-able conserved domain db. There is 5 - 10 domains output on each query typically. This rps-blast method uses a BLOSUM62 matrix which essentially tells you how related any 2 proteins are to each other (used in most global alignment methods).

The slurm scripts are useful for running 1000s of jobs in parallel on a supercomputer. There's also a script on selecting proteins which were found above a certain thershold.
