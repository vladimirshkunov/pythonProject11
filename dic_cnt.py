D = {}
f = open("words.txt")
for s in f:
    word = s.strip()
    if word:
        D[word] = D.get(word, 0) + 1

f = open("output.txt", "w+")
for x in sorted(D):
    f.write(f'{x}: {D[x]}\n')
f.close()
