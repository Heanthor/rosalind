filename = 'ex30.txt'


def cyclic_rotations(text):
    rotations = []

    for i in xrange(1, len(text) + 1):
        rotations.append(text[-i:] + text[:-i])

    rotations.sort()
    return rotations


def bwt_rotations(rotations):
    return "".join([rotations[x][-1:] for x in xrange(len(rotations))])


def burrows_wheeler_transform(text):
    return bwt_rotations(cyclic_rotations(text))


# with open(filename, 'r') as f:
#     text = f.readline().strip()
#
#     print burrows_wheeler_transform(cyclic_rotations(text))
