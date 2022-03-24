import numpy as np
arr = np.array([38, 16, 1, 27, 55, 8, 19])
print(arr > 20)
print(arr % 2 == 0)
print(np.where(arr > 20))
Filter = np.where(arr > 20)
print(arr[Filter])

boolArr = np.array([True, True, False, True, False, False, False])
print(np.where(boolArr))
