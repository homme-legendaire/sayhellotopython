# append
# import numpy as np
# while True:
#     cnt = 0
#     arr = np.random.randint(1, 7, size=(10, 3))
#     print(arr)
#     em = np.empty((0, 3), dtype=np.int32)
#     for i in range(10):
#         if arr[i, 0] == arr[i, 1] or arr[i, 0] == arr[i, 2] or arr[i, 1] == arr[i, 2]:
#             cnt += 1
#             em = np.append(em, [arr[i, :]], axis=0)
#     if cnt != 0:
#         print(em)
#         break

# vstack
import numpy as np
while True:
    cnt = 0
    arr = np.random.randint(1, 7, size=(10, 3))
    print(arr)
    em = np.empty((0, 3), dtype=np.int32)
    for i in range(10):
        if arr[i, 0] == arr[i, 1] or arr[i, 0] == arr[i, 2] or arr[i, 1] == arr[i, 2]:
            cnt += 1
            em = np.vstack([em, arr[i, :]])
    if cnt != 0:
        print(em)
        break
