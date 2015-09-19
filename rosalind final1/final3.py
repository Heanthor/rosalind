def count(text, pattern):
    c = 0
    pos = 0

    while True:
        pos = text.find(pattern, pos) + 1

        if pos > 0:
            c += 1
        else:
            return c


def lt_clump(l, t, pattern, genome):
    offset = 0
    c = 0

    while offset < len(genome) - l - 1:
        sub_interval = genome[offset:l + offset]
        c = count(sub_interval, pattern)

        if c >= t:
            return pattern

        offset += 1


def unique_substrings(text, length):
    strings = set()
    pos = 0

    while pos < len(text) - length + 1:
        strings.add(text[pos:pos + length])
        pos += 1

    return strings

filename = "ex13.txt"
with open(filename, 'r') as f:
    dna = f.readline().strip()
    k, l, t = f.readline().strip().split(" ")
    substrings = list(unique_substrings(dna, int(k)))

    kmers = []
    for substring in substrings:
        x = lt_clump(int(l), int(t), substring, dna)
        if x is not None:
            kmers.append(x)
    print " ".join(kmers)

