from random import sample, randint, random
from copy import deepcopy
from math import log

filename = "final2.txt"
alphabet = "ACGT"


# calculates total entropy over a profile
def score(profile):
    k = len(profile['A'])
    total_entropy = 0.0

    for i in xrange(k):  # iterate over every column
        tmp = 0.0
        for letter in alphabet:  # every row
            val = profile[letter][i]
            tmp += val * log(val, 2)
        total_entropy += -tmp

    return total_entropy


# select a number based on a probability distribution
def roll_n_sided_dice(distribution):
    roll = random()
    s = 0
    result = 1

    for m in distribution:
        s += m
        if roll < s:
            return result
        result += 1

    return result


# returns a random number from the RNG created using probabilities of kmers in string using profile
def profile_random_number_generator(string, profile):
    k = len(profile['A'])
    probabilities = []

    # calculate probabilities
    for i in xrange(len(string) - k):
        kmer = string[i:i + k]
        prob = 0.0
        j = 0
        for nuc in kmer:
            prob += profile[nuc][j]
            j += 1
        probabilities.append(prob)

    # create and return random number
    c = sum(probabilities)
    new_list = [x / c for x in probabilities]
    return roll_n_sided_dice(new_list)


def vector_to_strings(strings, vector, k):
    motifs = []
    i = 0
    for starting_index in vector:
        motifs.append(strings[i][starting_index: starting_index + k])
        i += 1
    return motifs


# generate profile with pseudocounts of motifs
def profile(motifs):
    c = counts(motifs)

    # convert count into profile
    for letter in alphabet:
        for i in xrange(len(c[letter])):
            curr_number = c[letter][i] + 1  # pseudocounts
            c[letter][i] = float(curr_number) / (len(motifs) + 4)
    return c


# generate count(motifs) matrix
def counts(motifs):
    # motifs are same length
    n = len(motifs[0])
    count = {}

    # initialize dicts
    for letter in alphabet:
        count[letter] = [0]*n

    for pos in xrange(n):
        for motif in motifs:
            x = motif[pos]
            count[x][pos] += 1

    return count


def gibbs_sampler(dna, k, t, n):
    indices = sample(range(len(dna[0])-k), t)  # starting indices
    motifs = [dna[x][y:y + k] for x, y, in enumerate(indices)]
    best_motifs = [deepcopy(motifs), score(profile(motifs))]

    for x in xrange(n):
        # select all motifs except at location i
        i = randint(0, t - 1)
        tmp = []

        for j in xrange(len(motifs)):
            if i != j:
                tmp.append(motifs[j])
        p_p = profile(tmp)

        chosen_index = profile_random_number_generator(dna[i], p_p)
        motif_i = dna[i][chosen_index:chosen_index + k]

        motifs_p = deepcopy(motifs)
        motifs_p[i] = motif_i

        score_motifs_p = score(profile(motifs_p))
        if score_motifs_p < best_motifs[1]:
            best_motifs = [motifs_p, score_motifs_p]
            motifs = motifs_p
    return best_motifs

def run():
    with open(filename, 'r') as f:
        k, t, n = map(int, f.readline().strip().split(" "))
        strings = []

        while True:
            line = f.readline().strip()

            if not line:
                break
            strings.append(line)

        best_score = k*t  # too high
        best_kmers = []

        for i in xrange(20):
            result = gibbs_sampler(strings, k, t, n)
            if result[1] < best_score:
                best_kmers = result[0]

                best_score = result[1]

        print "\n".join(list(best_kmers))
        print best_score

#run()
