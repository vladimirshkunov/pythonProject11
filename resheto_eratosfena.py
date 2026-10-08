from time import time
from math import sqrt

n = int(input()) + 1
start_time = time()
A = [True] * n
for k in range(2, int(sqrt(n)) + 1):
    if A[k]:
        for i in range(k * k, n, k):
            A[i] = False

end_time = time()
print([i for i in range(n) if A[i]][2:])
print(f'{end_time - start_time:.6f}')
