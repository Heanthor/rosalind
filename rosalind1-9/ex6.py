filename = "rosalind_ini6.txt"
with open(filename, 'r') as f:
    str = f.read().strip()
    words = {}

    for word in str.split(" "):
        if word in words:
            words[word] += 1
        else:
            words[word] = 1

    for word in words:
        print "%s %d" % (word, words[word])
