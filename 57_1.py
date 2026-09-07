a, b, c, d, e = map(int, input().split())
m = a
m = b if b > m else m
m = c if c > m else m
m = d if d > m else m
m = e if e > m else m
print(m)
