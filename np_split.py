import numpy as np

arr = np.arange(1,13).reshape(3,4)
print(arr)

arr_vsplit = np.vsplit(arr,3) # axis=0 기준으로 분할
print(arr_vsplit)

arr_hsplit = np.hsplit(arr,2) # axis=1 기준으로 분할
print(arr_hsplit)
