#!/bin/bash
#echo "hello world!"
echo "Start Date:"
date
#module load blast+/2.2.29
SCRIPT_PATH="rbbh_orth_find.py"
PYTHON="/usr3/graduate/oyoruk/anaconda/bin/python"
#/usr/bin/python
# call script via the interrupter
$PYTHON $SCRIPT_PATH
echo
echo
echo "Finish Date:"
date
#blastp -query proteins.FilteredModels1.fasta -db hs_embl_prot_db -out nv_hs_embl_table.csv -outfmt "6 qseqid qlen sseqid slen qframe qstart qend sframe sstart send evalue bitscore pident nident length" -num_alignments 1 -evalue 1e-05
