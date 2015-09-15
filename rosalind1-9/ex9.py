def complement(letter):
    return {
        "A": "T",
        "T": "A",
        "C": "G",
        "G": "C"
    }[letter]


filename = "rosalind_revc.txt"
with open(filename, 'r') as f:
    str = f.read().strip()
    str2 = str[::-1]  # reverse string
    s = ""
    for i in range(len(str2)):
        s += complement(str2[i])
    print s
