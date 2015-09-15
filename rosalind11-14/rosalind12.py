def find(text, pattern):
    c = []
    pos = 0

    while True:
        pos = text.find(pattern, pos) + 1

        if pos > 0:
            c.append(str(pos - 1))
        else:
            return c

filename = "rosalind_ba1d.txt"
with open(filename, 'r') as f:
    pattern = f.readline().strip()
    string = f.readline().strip()

    print " ".join(find(string, pattern))
