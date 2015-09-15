filename = "final2.txt"

alphabet = ["A", "C", "T", "G"]

def neighborhood(kmer, d, strings):
    # base case
    if d == 0:
        if len(strings) == 0:
            return [kmer]
        else:
            strings.append(kmer)
            return strings

    for i in range(len(kmer)): # position in string
        for j in range(len(alphabet)): # letter to swap out
            # make list out of kmer string
            new_kmer = []
            for char in kmer:
                new_kmer.append(char)

            if not kmer[i] == alphabet[j]:
                new_kmer[i] = alphabet[j]
                strings.append("".join(new_kmer))
    return neighborhood(kmer, d - 1, strings)


with open(filename, 'r') as f:
    genome = f.readline().strip()
    k, d = f.readline().strip().split(" ")
    print neighborhood("ACG", 1, [])