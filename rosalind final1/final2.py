from collections import defaultdict
from itertools import chain, combinations, product

filename = "rosalind_ba1j.txt"

alphabet = ["A", "C", "T", "G"]
# store calculated neighbor lists to avoid unnecessary calculations
neighbors_dict = {}
neighbors_dict_rev = {}


def complement(letter):
    return {
        "A": "T",
        "T": "A",
        "C": "G",
        "G": "C"
    }[letter]


def reverse_compliment(g):
    str2 = g[::-1]  # reverse string
    s = ""
    for i in range(len(str2)):
        s += complement(str2[i])
    return s


def unique_substrings(text, length):
    strings = set()
    pos = 0

    while pos < len(text) - length + 1:
        strings.add(text[pos:pos + length])
        pos += 1

    return strings


def generate_all_kmers(length):
    kmers = [[]]
    for i in range(length):
        kmers = [[x] + y for x in alphabet for y in kmers]

    return map("".join, kmers)


def count(text, pattern):
    c = 0
    pos = 0

    while True:
        pos = text.find(pattern, pos) + 1

        if pos > 0:
            c += 1
        else:
            return c

# return neighbors for string kmer in range d
def neighbors(kmer, d):
    return chain.from_iterable(hamming_d(kmer, i) for i in range(d + 1))

# returns neighbor strings of kmer ONLY distance d away
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


def count_occurrences(genome, k, d):
    unique_kmers = list(unique_substrings(genome, k))
    found_mismatches_per_kmer = defaultdict(int)
    all_possible_kmers = set()

    # calculate neighbors of all substrings, these are the kmers that are possible solutions
    for uk in unique_kmers:
        tmp = list(neighbors(uk, d))
        neighbors_dict[uk] = tmp
        for item in tmp:
            all_possible_kmers.add(item)

    # debug strings
    print len(all_possible_kmers)
    counter = 0
    for kmer in all_possible_kmers:
        if counter % 100 == 0:
            print "Count: %d" % counter # track progress of script
        # compute neighbors of kmer
        mismatches = neighbors(kmer, d) if kmer not in neighbors_dict.keys() else neighbors_dict[kmer]

        # for every neighbor of candidate kmer, count occurrences, store them
        for mismatch in mismatches:
            occurrences = count(genome, mismatch)
            if occurrences > 0:
                found_mismatches_per_kmer[kmer] += occurrences

        # reverse compliment
        rev_cmp = reverse_compliment(kmer)
        tmp2 = list(neighbors(rev_cmp, d))
        for uk2 in tmp2:
            neighbors_dict_rev[kmer] = (tmp2)

        mismatches_rev_cmp = neighbors(rev_cmp, d) if kmer not in neighbors_dict_rev.keys() else neighbors_dict_rev[kmer]

        # calculate occurrences for reverse compliment too, add to "sum"
        for mismatchb in mismatches_rev_cmp:
            occurrences = count(genome, mismatchb)
            if occurrences > 0:
                found_mismatches_per_kmer[kmer] += occurrences

        counter += 1
    max_occurrences = max(found_mismatches_per_kmer.values())
    to_return = []
    # add kmers that appear most frequently to return value
    for kmer, num in found_mismatches_per_kmer.iteritems():
        if num == max_occurrences:
            to_return.append(kmer)

    return to_return


with open(filename, 'r') as f:
    genome = f.readline().strip()
    k, d = map(int, f.readline().strip().split(" "))

    to_return = count_occurrences(genome, k, d)

    print "\n".join(to_return)
