from ex20 import substrings
from collections import defaultdict


def largest_k_with_repeats(genome):
    kmer_size = 1

    while True:
        repeats = max_repeats(genome, kmer_size)

        if repeats == 1:
            return kmer_size - 1

        kmer_size += 1


def max_repeats(genome, kmer_length):
    counts = defaultdict(int)

    unique_ss = substrings(genome, kmer_length)

    for string in unique_ss:
        counts[string] += 1

    max_occurrences = -1

    for string, count in counts.iteritems():
        if count > max_occurrences:
            max_occurrences = count

    return max_occurrences

with open("assembled_genome.txt", 'r') as f:
    genome = f.read().strip()

    print largest_k_with_repeats(genome)
