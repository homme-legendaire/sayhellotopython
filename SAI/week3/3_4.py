import numpy as np
a = int(input())
arr = np.random.randint(1, 1000, size=a)
arr = np.sort(arr)
print(arr)
result = np.empty((0, 4), dtype=np.int32)
delete = np.empty((0, 4), dtype=np.int32)
i = 0
cnt = 0
while i <= a-3:
    cnt += 1
    result = np.append(result, arr[i:i+4])
    i += 2
    if i+4 >= a-1 and i % 4 != 0:
        delete = np.append(delete, arr[i+2:i+5])
        break
print(result.reshape(cnt, 4))
print(f"삭제된 원소:{delete}")
