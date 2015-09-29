def unique_substrings(text, length):
    strings = set()
    pos = 0

    while pos < len(text) - length + 1:
        strings.add(text[pos:pos + length])
        pos += 1

    return strings


nucleotides = list('ACGT')
def get_neighbors(pattern, d):
    if d == 0:
        return [(pattern,0)]
    if len(pattern) == 1:
        return [(nuc, 1 if nuc != pattern else 0) for nuc in nucleotides]

    neighborhood = set()
    suffix_neighbors = get_neighbors(pattern[1:], d)
    for (text, cur_d) in suffix_neighbors:
        if cur_d < d:
            for nuc in nucleotides:
                distance = cur_d + 1 if nuc != pattern[0] else cur_d
                neighborhood.add((nuc + text, distance))
        else:
            neighborhood.add((pattern[0] + text, d))
    return neighborhood


def count(text, pattern):
    c = 0
    pos = 0

    while True:
        pos = text.find(pattern, pos) + 1

        if pos > 0:
            c += 1
        else:
            return c


def in_every_list_list(list_of_candidates, lists):
    for l in lists:
        to_return = 0
        for elt in list_of_candidates:
            if elt in l:
                to_return += 1
        if to_return == 0:
            return False
    return True


def in_every_list(item, lists):
    for l in lists:
        if count(item, l) == 0:
            return False
    return True


def motif_enumeration(dna, k, d):
    patterns = set()
    all_dna = "".join(dna)
    kmers = unique_substrings(all_dna, k)

    for kmer in kmers:
        tmp = get_neighbors(kmer, d)
        neighbors = [x[0] for x in tmp]

        for neighbor in neighbors:
            tmp2 = get_neighbors(neighbor, d)
            n2 = [x[0] for x in tmp2]

            if in_every_list_list(n2, dna):
                patterns.add(neighbor)
    return list(patterns)


filename = "rosalind_ba2a.txt"
with open(filename, 'r') as f:
    raw = f.read().strip().split('\n')
    k, d = raw[0].split()
    items = raw[1:]
    print " ".join(motif_enumeration(items, int(k), int(d)))

# print "Yes" if in_every_list('a', [['a'], ['a', 'b,'], ['a']]) else "no"
