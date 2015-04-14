#!usr/bin/python 

import sys, csv
import subprocess
import datetime, time
from collections import defaultdict

#Since it is reciprocal blast, a rather high e-value cutoff is used. 
#It can be avoided alltogether, since filtering for reciprocity is
#expected to sort out high e-value matches.
#NtS: try out other cutoffs
E_CUTOFF = "1e+10"

"""
#Load blast into the environment first
#NtS: make this statement more generic
shell_out = subprocess.call("module load blast+/2.2.29",shell=True)
#Wait for the process to complete
if shell_out == 0:
    pass
else:
    print("Problem loading blast to the environment.")
"""

#usage:
#NtS: convey usage info somehow
#python rbbh_orth_find.py org_1 fasta_1 org_2 fasta_2

#NtS: change these hardcoded parts
org_I = "Nv"
fasta_I = "proteins.FilteredModels1.fasta"
org_II = "Hs"
fasta_II = "uniprot-organism%3A9606+AND+keyword%3A%22Complete+proteome+%5BKW-0\
181%5D%22.fasta"


print("\n"*2+"_"*79)
print("Information on this run:")
print("Organism I: " + org_I)
print("Fasta file containing protein sequences of organism I:")
print(fasta_I)
print("Organism II: " + org_II)
print("Fasta file containing protein sequences of organism II:")
print(fasta_II)
print("E-value cutoff: " + E_CUTOFF)
print("_"*79)

"""
org_I = "tsI"
fasta_I = "test_prot_A.fasta"
org_II = "tsII"
fasta_II = "test_prot_B.fasta"
"""
#One way blasting takes more than 3 hours, therefore interactive
#parts are commented out. Instead they will be inputted with the
#initial command.

"""
print("This script finds pairs of potential orthologue proteins\
of two different organisms, using reciprocal blast best hits.\
To use please enter protein fasta files of the two organisms.")

#get user input
org_I = raw_input("Please enter the name of the first organism.")
fasta_I = raw_input("Please enter the name of the first fasta \
file, containing protein sequences of the first organism.")

org_II = raw_input("Please enter the name of the second organism.")
fasta_II = raw_input("Please enter the name of the second fasta \
file, containing protein sequences of the second organism.")
"""

#Create a subfolder with names of the organisms
#use the subfolder to store intermediate blast tables and
#reciprocal blast best hit table
ts = datetime.datetime.fromtimestamp(time.time()).\
	strftime('%Y-%m-%d_%H:%M:%S_')
subfolder_name = ts + org_I + "_" + org_II + "_rbbh_orth"
subprocess.call("mkdir " + subfolder_name,shell=True)
#subprocess.call("cd " + subfolder_name,shell=True)

###############################################################################
#
#	CREATING BLAST DATABASES
#
###############################################################################
#create a blast database for first organism's
#prot sequences
print("\n"*2+"_"*79)
print("Creating a blast database for first organism's \
protein sequences.")
prot_db_I = org_I + "_prot_blastdb"
cmd_blastdb_org_I = "makeblastdb -in " + fasta_I + " -dbtype \"prot\"\
 -out \"" + subfolder_name + "/" + prot_db_I +"\""
shell_out = subprocess.call(cmd_blastdb_org_I, shell = True)
#Wait for the process to complete
if shell_out == 0:
    pass
else:
#NtS: change this message, handle the error
    print("Blast has not worked")
print("_"*79)

#create a blast database for second organism's
#prot sequences
print("\n"*2+"_"*79)
print("Creating a blast database for second organism's \
protein sequences.")
prot_db_II = org_II + "_prot_blastdb"
cmd_blastdb_org_II = "makeblastdb -in " + fasta_II + " -dbtype \"prot\"\
 -out \"" + subfolder_name + "/" + prot_db_II +"\""
shell_out = subprocess.call(cmd_blastdb_org_II, shell = True)
#Wait for the process to complete
if shell_out == 0:
    pass
else:
#NtS: change this message, handle the error
    print("Blast has not worked")
print("_"*79)
###############################################################################

###############################################################################
#
#	BLASTING PROTEIN SEQUENCES
#
###############################################################################
#blast prot sequences of first organism against
#the prot sequences of second organism 
#write results into a tab limited file
print("\n"*2+"_"*79)
print("Blasting protein sequences of first organism\n\
against protein sequences of the second organism.")
blast_table_I = org_I + "_" + org_II+ "_prot_blast_table.csv"
cmd_blast_org_I_org_II = "blastp \
-query " + fasta_I + " \
-db "	+ subfolder_name + "/" + prot_db_II + " \
-out " 	+ subfolder_name + "/" + blast_table_I + " \
-outfmt 6 -num_alignments 1 -evalue " + E_CUTOFF
 
shell_out = subprocess.call(cmd_blast_org_I_org_II, shell=True)
#Wait for the process to complete
if shell_out == 0:
    print("\nComplete.")
else:
#NtS: change this message, handle the error
    print("Blast has not worked")

#Contstruct new table that only contain best hits.
blast_besthits_table_I = org_I + "_" + org_II+ "_prot_blast_besthits_table.csv"
cmd_besthits_I = "sort -k1,1 -k12,12gr -k11,11g -k3,3gr " + \
subfolder_name + "/" + blast_table_I + " | sort -u -k1,1 --merge > " + \
subfolder_name + "/" + blast_besthits_table_I

shell_out = subprocess.call(cmd_besthits_I, shell = True)
if shell_out == 0:
    print("First best hits table constructed.")
else:
#NtS: Handle this
    print("Failure")
print("_"*79)

#blast prot sequences of second organism against
#the prot sequences of first organism 
#write results into a tab limited file
print("\n"*2+"_"*79)
print("Blasting protein sequences of second organism\n\
against protein sequences of the first organism.")
blast_table_II = org_II + "_" + org_I+ "_prot_blast_table.csv"
cmd_blast_org_II_org_I = "blastp \
-query " + fasta_II + " \
-db "	+ subfolder_name + "/" + prot_db_I + " \
-out " 	+ subfolder_name + "/" + blast_table_II + " \
-outfmt 6 -num_alignments 1 -evalue " + E_CUTOFF
 
shell_out = subprocess.call(cmd_blast_org_II_org_I, shell=True)
#Wait for the process to complete
if shell_out == 0:
    print("\nComplete.")
else:
#NtS: change this message, handle the error
    print("Blast has not worked")

#Contstruct new table that only contain best hits.
blast_besthits_table_II = org_II + "_" +org_I+ "_prot_blast_besthits_table.csv"
cmd_besthits_II = "sort -k1,1 -k12,12gr -k11,11g -k3,3gr " + \
subfolder_name + "/" + blast_table_II + " | sort -u -k1,1 --merge > " + \
subfolder_name + "/" + blast_besthits_table_II

shell_out = subprocess.call(cmd_besthits_II, shell = True)
if shell_out == 0:
    print("Second best hits table constructed.")
else:
#NtS: Handle this
    print("Failure")
print("_"*79)
###############################################################################

###############################################################################
#
#	CHECKING FOR RECIPROCITY
#
###############################################################################
#check blast results for reciprocity
#write reciprocal best hits into a final tab limited file
#output = csv.writer(sys.stdout,delimiter='\t')
print("\n"*2+"_"*79)
input = csv.reader(open(subfolder_name + "/" + \
		blast_besthits_table_I),delimiter="\t")
lookup = defaultdict(str)
print("Hashing first besthit table.")
for row in input: lookup[row[0]] = row[1]
input2 = csv.reader(open(subfolder_name + "/" +\
		 blast_besthits_table_II),delimiter="\t")
print("Going through the second besthit table.")
rbbh_table = org_I + "_" + org_II+ "_rbbh_orth_table.csv" 
output = csv.writer(open(subfolder_name + "/" + rbbh_table,"w"),delimiter="\t")
for row in input2:
    if lookup.get(row[1],False) == row[0]:
        output.writerow([row[1],row[0]])
print("_"*79)
###############################################################################





