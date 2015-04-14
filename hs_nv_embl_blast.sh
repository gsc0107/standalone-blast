#!/bin/bash
#echo "hello world!"
date
SCRIPT_PATH="hs_nv_embl_blast.py"
PYTHON="/usr/bin/python"
 
# call script via the interrupter
$PYTHON $SCRIPT_PATH
date
#blastp -query proteins.FilteredModels1.fasta -db hs_embl_prot_db -out nv_hs_embl_table.csv -outfmt "6 qseqid qlen sseqid slen qframe qstart qend sframe sstart send evalue bitscore pident nident length" -num_alignments 1 -evalue 1e-05
