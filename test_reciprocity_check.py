#!usr/bin/python

from collections import defaultdict
import csv

input = csv.reader(open("Nv_Hs_prot_blast_besthits_table.csv"),delimiter="\t")

lookup = defaultdict(str)

print("hashing first besthit table")
for row in input: lookup[row[0]] = row[1]

input2 = csv.reader(open("Nv_Hs_prot_blast_besthits_table.csv"),delimiter="\t")
print("going through the second besthit table")

rbbh_orth = []
output = csv.writer(open("Nv_Hs_rbbh_orth_table.csv","w"),delimiter="\t")

for row in input2:
    if lookup.get(row[1],False) == row[0]:
	output.writerow([row[0],row[1]])
