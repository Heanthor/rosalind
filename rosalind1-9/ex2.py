filename = "ex2.txt"
with open(filename, 'r') as f:
    str = f.read().strip()
    a, b = [int(x) for x in str.split()]
    print a**2 + b**2