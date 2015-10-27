filename = "ex22.txt"


def reconstruct_string(kmers, k, d):
    first_strings = [x.split("|")[0] for x in kmers]
    second_strings = [x.split("|")[1] for x in kmers]

    genome = first_strings[0]  # starting string

    for i in xrange(1, d + 1):  # fill d spaces in gap between first two kmers
        genome += first_strings[i][-1:]

    genome += second_strings[0]  # now, can build genome from second strings only

    for string in second_strings[1:]:
        genome += string[-1:]

    return genome

with open(filename, 'r') as f:
    k, d = map(int, f.readline().strip().split(" "))

    kmers = f.read().strip().replace("\r", "").split("\n")

    print reconstruct_string(kmers, k, d)
