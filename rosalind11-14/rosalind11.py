import collections


def count(text, pattern):
    c = 0
    pos = 0

    while True:
        pos = text.find(pattern, pos) + 1

        if pos > 0:
            c += 1
        else:
            return c


def unique_substrings(text, length):
    strings = set()
    pos = 0

    while pos < len(text) - length + 1:
        strings.add(text[pos:pos + length])
        pos += 1

    return strings


def maximum_kmer(text, length):
    kmers = list(unique_substrings(text, length))
    max_num = 0
    max_kmers = collections.defaultdict(list)

    for kmer in kmers:
        c = count(text, kmer) # number of times kmer appears in text
        if c >= max_num: # kmer is a max kmer
            max_num = c
            max_kmers[max_num].append(kmer)

    return max_kmers[max(max_kmers.keys())]

filename = "rosalind_ba1b.txt"
with open(filename, 'r') as f:
    dna = f.readline().strip()
    num = f.readline().strip()
    print " ".join(maximum_kmer(dna, int(num)))
