filename = "rosalind_ba1f.txt"

countG = []
countC = []

def find_multiple_minimums(list_in):
    # find locations where minimum value occurs
    min_value = min(list_in)
    min_pos = []

    for i in range(len(list_in)):
        if list_in[i] == min_value:
            min_pos.append(i + 1)

    return min_pos

def count_nucleotides(str, nucleotide, i):
    # this implementation assumes you will populate the lists starting at i = 0
    # which is true if skew is calculated starting at i = 0
    if nucleotide == "G":
        if str[i] == "G":
            countG[i] = countG[i - 1] + 1
        else:
            countG[i] = countG[i - 1]
        return countG[i]
    else:
        if str[i] == "C":
            countC[i] = countC[i - 1] + 1
        else:
            countC[i] = countC[i - 1]
        return countC[i]


def skew(genome):
    # calculates the G C skew of a genome using efficient algorithm from class
    skews = []
    for i in range(len(genome)):
        skews.append(count_nucleotides(genome, "G", i) - count_nucleotides(genome, "C", i))
    return skews

with open(filename, 'r') as f:
    dataset = f.readline().strip()
    # initialize shared lists
    countG = [0] * len(dataset)
    countC = [0] * len(dataset)
    print " ".join(map(str, find_multiple_minimums(skew(dataset))))
