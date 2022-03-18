import numpy as np
a = int(input())
arr = np.random.randint(1, 1000, size=a)
print(arr)
result = np.empty((0, 4), dtype=np.int32)
delete = np.empty((0, 4), dtype=np.int32)
i = 0
cnt = 0
while i <= a-3:
    cnt += 1
    result = np.append(result, arr[i:i+4, ])
    i += 2
    if i+4 > a and a % 4 != 0:
        delete = np.append(delete, arr[i:i+3, ])
        break
print(result.reshape(cnt, 4))
print(f"삭제된 원소:{delete}")
