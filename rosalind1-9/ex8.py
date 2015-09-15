filename = "rosalind_rna.txt"
with open(filename, 'r') as f:
    str = f.read().strip()
    print "%s" % str.replace("T", "U")
