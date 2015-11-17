filename = "ex27.txt"


def knuth_morris_pratt_preprocess(string):
    j = -1
    failure_array = [-1]

    for c in string:
        while j >= 0 and string[j] != c:
            j = failure_array[j]
        j += 1
        failure_array.append(j)

    return failure_array[1:]

with open(filename, 'r') as f:
    genome = f.read().strip().split("\n")[1]

    print " ".join(map(str, knuth_morris_pratt_preprocess(genome)))