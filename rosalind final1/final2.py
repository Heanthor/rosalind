from itertools import chain, combinations, product

filename = "final2.txt"

alphabet = ["A", "C", "T", "G"]


def hamming_all_d(kmer, d):
    return chain.from_iterable(hamming_d(kmer, i) for i in range(d + 1))

def hamming_d(kmer, d):
    for pos in combinations(range(len(kmer)), d):
        for replacements in product(range(len(alphabet) - 1), repeat = d):
            cousin = list(kmer)
            for p, r in zip(pos, replacements):
                if cousin[p] == alphabet[r]:
                    cousin[p] = alphabet[-1]
                else:
                    cousin[p] = alphabet[r]
            yield ''.join(cousin)


with open(filename, 'r') as f:
    genome = f.readline().strip()
    k, d = f.readline().strip().split(" ")
    print "\n".join(hamming_all_d(genome, int(d)))