import numpy as np
# ㄱ X
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr)
arr = np.delete(arr, 0)
print(arr)
# ㄴ - 5-1. 4:00
# ㄷ X
arr = np.arange(8)
print(arr)
arr = arr.reshape(2, 4)
print(arr)
# ㄹ X
# ㅁ X
arr1 = np.ones((2, 3))
arr2 = np.zeros((4, 3))

test = np.hstack((arr1, arr2))
print(test)
