def bp_range(genome, starting_pos, range):
    # circular genome
    if starting_pos + range >= len(genome):
        hang_over = (starting_pos + range) - len(genome)
        tmp = genome[starting_pos - range: len(genome)] + genome[0: hang_over]
        return tmp
    else:
        return genome[starting_pos - range:starting_pos + range]


filename = "campy.fa"
with open(filename, 'r') as f:
    dataset = f.read().strip()
    dataset = dataset.replace("\n", "").replace("\r", "")
    print bp_range(dataset, len(dataset) - 1, 250)