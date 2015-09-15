filename = "rosalind_ini5.txt"
with open(filename, 'r') as f:
    count = 1
    for line in f:
        if count % 2 == 0: # even
            print line.strip()
        count += 1
