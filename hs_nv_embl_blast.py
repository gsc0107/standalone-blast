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

subprocess.call("blastp -query Homo_sapiens.GRCh38.pep.abinitio.fa -db nv_prot_db -out hs_nv_embl_table.csv -outfmt \"6 qseqid qlen sseqid slen qframe qstart qend sframe sstart send evalue bitscore pident nident length\" -num_alignments 1 -evalue 1e-05",shell=True)

