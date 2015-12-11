from pileup_user import read_fa_file
from Bio import Seq

reference = read_fa_file("data/reference.fa")

print "Original sequence: " + Seq.translate(reference)[274]

mutated_reference = ""
for i, x in enumerate(reference):
    if i == 822:
        mutated_reference += "T"
    else:
        mutated_reference += x

print "Read sequence: " + Seq.translate(mutated_reference)[274]
