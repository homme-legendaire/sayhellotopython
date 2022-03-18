import numpy as np
a = int(input())
arr = np.random.randint(1, 1000, size=a)
print(arr)
result = np.empty((0, 4), dtype=np.int32)
delete = np.empty((0, 4), dtype=np.int32)
i = 0
cnt = 0
while i <= a-3:
    if i+4 > a:
        if cnt == 0:
            delete = np.append(delete, arr[i:i+3, ])
        else:
            delete = np.append(delete, arr[i+2:i+4, ])
        break
    cnt += 1
    result = np.append(result, arr[i:i+4, ])
    i += 2
print(result.reshape(cnt, 4))
print(f"삭제된 원소:{delete}")
