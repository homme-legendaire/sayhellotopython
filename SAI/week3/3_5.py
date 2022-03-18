import numpy as np
N = int(input())
arr = np.zeros((N, N), dtype=np.int32)
num = 1
for i in range(N):
    for j in range(i+1):
        arr[i, j] = num % 10
        num += 1
print(arr)
