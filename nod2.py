a, b = map(int, input().split())
if b > a: a, b = b, a
p = a * b
while b:
    a %= b
    a, b = b, a
nod = a
nok = p // nod
print(nod, nok)
