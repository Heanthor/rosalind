filename = "rosalind_ini3.txt"
with open(filename, 'r') as f:
    str = f.readline().strip()
    numbers = f.readline().strip().split(" ")

    print "%s %s" % (str[int(numbers[0]): int(numbers[1]) + 1], str[int(numbers[2]): int(numbers[3]) + 1])
