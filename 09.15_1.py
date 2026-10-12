a, b = map(int, input().split())
if a > b: a, b = b, a
i = a
while i <= b:
    print(f'{i}**2 = {i ** 2}')
    i += 1

"""
for i in range(a, b + 1)
"""
