import operator

filename = "ex28.txt"


def generate_suffixes(text):
    suffixes = {}

    for i in xrange(len(text)):
        suffixes[i] = text[i:]

    return suffixes


def sort_suffixes(suffix_dict):
    sorted_suffixes = sorted(suffix_dict.items(), key=operator.itemgetter(1))

    return [suffix[0] for suffix in sorted_suffixes]


def get_suffix_array(text):
    return sort_suffixes(generate_suffixes(text))

# with open(filename, 'r') as f:
#     text = f.read().strip()
#
#     print ", ".join(map(str, [x[0] for x in sort_suffixes(generate_suffixes(text))]))
