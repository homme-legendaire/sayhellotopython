import numpy as np
# ㄱ ?
arr = np.arange(1, 13).reshape(3, 4)
print(arr)
print(arr[0][0])
print(arr[0, 0])
arr2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print(arr2)
print(arr2[0][0])
#print(arr2[0, 0])
# ㄴ X
arr = np.array([[1, 2], [3, 4]])
print(arr)
arr = np.argsort(arr)
print(arr)
# ㄷ X
# ㄹ
arr = np.array([[[1], [2]], [[3], [4]], [[5], [6]]])
print(arr)
arr = np.squeeze(arr, axis=2)  # axis를 기준으로 작게 줄여줌
print(arr)
