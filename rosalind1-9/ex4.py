filename = "rosalind_ini4.txt"
with open(filename, 'r') as f:
    str = f.read()
    a, b = [int(x) for x in str.split(" ")]

    total = 0
    for i in range(a, b + 1):
        if i % 2 == 1: # odd
            total += i

    print total
