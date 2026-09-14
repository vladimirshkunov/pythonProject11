n = int(input())
min_digit = 9
while n:
    min_digit = n % 10 if n % 10 < min_digit else min_digit
    n //= 10
print(min_digit)
