from random import randint

n = randint(100, 9999999999)
print(n)
s = 0
while n:
    s += n % 10
    n //= 10
print(s)
