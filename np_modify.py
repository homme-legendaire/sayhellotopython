import numpy as np

arr = [1,2,3,4,5,6,7,8]
arr = np.insert(arr,2,50)
print(arr)

arr = np.arange(1,13).reshape(3,4)
arr = np.insert(arr,2,50,axis=0)
print(arr)

arr = np.arange(1,13).reshape(3,4)
print(arr)
arr = np.delete(arr,2,axis=0)
print(arr)
