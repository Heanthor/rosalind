filename = "ex31.txt"


def last_to_first(last_column):
    first_column = sorted(last_column)
    mapped_indexes = []

    for ch in last_column:
        i = first_column.index(ch)
        mapped_indexes.append(i)
        first_column[i] = "\0"

    return mapped_indexes


def bw_matching(first_column, last_column, pattern, l2f):
    top = 0
    bottom = len(last_column) - 1

    while top <= bottom:
        if len(pattern) > 0:
            symbol = pattern[-1:]
            pattern = pattern[:-1]

            substr = last_column[top: bottom + 1]
            if symbol in substr:
                top_index = substr.index(symbol) + top
                bottom_index = len(substr) - substr[::-1].index(symbol) + top - 1
                top = l2f[top_index]
                bottom = l2f[bottom_index]
            else:
                return 0
        else:
            return bottom - top + 1

with open(filename, 'r') as f:
    bwt = f.readline().strip()
    patterns = f.readline().strip().split(" ")

    first_col = sorted(bwt)
    l2f = last_to_first(bwt)
    match_indexes = []

    for p in patterns:
        match_indexes.append(bw_matching(first_col, bwt, p, l2f))

    print " ".join(map(str, match_indexes))

