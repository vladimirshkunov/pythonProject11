from math import factorial

n = int(input())
A = [1, ]
d = 1000000
for k in range(2, n + 1):
    r = 0
    for i in range(len(A)):
        p = A[i] * k + r
        A[i] = p % d
        r = p // d
    if r > 0:
        A.append(r)

print(A[-1], end='')
for i in range(len(A) - 2, -1, -1):
    print(f'{A[i]:06d}', end='')

print()
print(factorial(n))
