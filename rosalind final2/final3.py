from random import random
from random import randint
from random import shuffle
from final2 import profile, score
import threading

import re


nruns = 10
num_offspring = 5
mutation_rate = 1. / 15
max_age = 10
max_population_size = 100
mutations = {
    "A": "CGT",
    "C": "GAT",
    "G": "ACT",
    "T": "CGA"
}


def calculate_entropy(population):
    kmers = []
    for individual in population:
        kmers.append(individual[1])  # gather genes from population
    entropy = score(profile(kmers))
    return entropy


def yearend(population, max_population_size):
    # kill off random members
    if len(population) > max_population_size:
        shuffle(population)
        population = population[:max_population_size]

    for i in xrange(len(population)):
        population[i] = (population[i][0] + 1, population[i][1])  # tuples aren't mutable, right?

    return population


def remove_elders(population, max_age):
    return filter(lambda x: x[0] <= max_age, population)


def remove_nonbinding(population):
    # the rule for pattern T[C|G]GTNNNNT[A|G]NT
    # match C or G in the second position
    # match A,C,G or T in positions 5-8 ([ACGT]) is the set of characters
    # that match {4} is the exact number of matches
    # match A or G in position 10
    # match A,C,G or T in position 11
    matchRE = re.compile("T[CG]GT[ACGT]{4}T[AG][ACGT]T")
    match2 = re.compile("T[CG][ACGT]{8}[ACGT]T")

    return filter(lambda x: match2.match(x[1]) is not None, population)


def reproduce(population, num_offspring, mutation_rate):
    children = []
    for individual in population:  # every individual reproduces
        for i in xrange(num_offspring):  # generate this number of offspring
            parent_gene = individual[1]
            child_age = 0
            child_gene = ""

            # build gene for child
            for nuc in parent_gene:
                if random() <= mutation_rate:
                    child_gene += mutations[nuc][randint(0, 2)]  # random mutation
                else:
                    child_gene += nuc
            children.append((child_age, child_gene))

    for child in children:
        population.add_node(child)
    return population


def version_1(nyears):
    entropies = []
    for i in xrange(nruns):
        # age and sequence of primodial organism
        population = [(0, 'TCGTACGGTATT')]
        for j in xrange(nyears):
            # five new individuals per
            # individual in the population, with random mutations at each
            # position with given probability
            population = reproduce(population, num_offspring, mutation_rate)

            # remove members of the population with non-binding sequence
            # (only in version 1 of the game)
            population = remove_nonbinding(population)

            # remove members of the population that are too old (10 years old)
            population = remove_elders(population, max_age)

            # increase the age of each individual and keep at most 100
            #  individuals, choose randomly if populations is larger that 100
            population = yearend(population, max_population_size)
        entropies.append(calculate_entropy(population))
    return sum(entropies) / float(len(entropies))


def version_2(nyears):
    entropies = []
    for i in xrange(nruns):
        # age and sequence of primodial organism
        population = [(0, 'TCGTACGGTATT')]
        for j in xrange(nyears):
            # five new individuals per
            # individual in the population, with random mutations at each
            # position with given probability
            population = reproduce(population, num_offspring, mutation_rate)

            # remove members of the population that are too old (10 years old)
            population = remove_elders(population, max_age)

            # increase the age of each individual and keep at most 100
            #  individuals, choose randomly if populations is larger that 100
            population = yearend(population, max_population_size)
        entropies.append(calculate_entropy(population))
    return sum(entropies) / float(len(entropies))


def get_results(output):
    entropies_version1 = []
    entropies_version2 = []

    entropies_version1.append((version_1(100)))
    entropies_version1.append((version_1(100)))
    entropies_version1.append((version_1(1000)))
    entropies_version1.append((version_1(5000)))

    entropies_version2.append(version_2(10))
    entropies_version2.append(version_2(100))
    entropies_version2.append(version_2(1000))
    entropies_version2.append(version_2(5000))

    if output:
        print "Version 1:", " ".join(map(str, entropies_version1))
        print "Version 2:", " ".join(map(str, entropies_version2))
    return entropies_version1, entropies_version2

#print "Version 1 (10 years):", version_1(10)
#print "Version 2 (10 years):", version_2(10)
#
print "Version 1 (100 years):", version_1(100)
print "Version 2 (100 years):", version_2(100)

print "Version 1 (1,000 years):", version_1(1000)
print "Version 2 (1,000 years):", version_2(1000)



