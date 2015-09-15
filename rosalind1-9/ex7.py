filename = "rosalind_dna.txt"
with open(filename, 'r') as f:
    str = f.read().strip()
    print "%d %d %d %d" % (str.count("A"), str.count("C"), str.count("G"), str.count("T"))
