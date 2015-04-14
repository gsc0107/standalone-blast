#!usr/bin/python
"""
import time

counter = 0 


while True:
	print "hello " + str(counter)
	time.sleep(2)
	counter+=1
"""

import subprocess

subprocess.call("blastp -query proteins.FilteredModels1.fasta -db hs_embl_prot_db -out nv_hs_embl_table.csv -outfmt \"6 qseqid qlen sseqid slen qframe qstart qend sframe sstart send evalue bitscore pident nident length\" -num_alignments 1 -evalue 1e-05",shell=True)

