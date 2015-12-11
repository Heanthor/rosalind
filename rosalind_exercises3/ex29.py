from ex28 import generate_suffixes, sort_suffixes

filename = "ex29.txt"


def search(pattern, text):
    suffix_array = sort_suffixes(generate_suffixes(text))
    n = len(text)
    l = 0
    r = n

    while l < r:
        mid_point = (l + r) / 2

        if pattern > suffix_array[mid_point][1]:
            l = mid_point + 1
        else:
            r = mid_point

    return l


def search_normal(pattern, text):
    indices = []

    for i in xrange(0, len(text) - len(pattern) + 1):
        if text[i: i + len(pattern)] == pattern:
            indices.append(i)

    return indices

with open(filename, 'r') as f:
    text = f.readline().strip()

    patterns = f.read().split('\n')

    indexes = []

    for pattern in patterns:
        indexes.append(search_normal(pattern, text))

    l = [item for sublist in indexes for item in sublist]
    l.sort()

    print " ".join(map(str, l))

