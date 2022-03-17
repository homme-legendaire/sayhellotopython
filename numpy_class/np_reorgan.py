import numpy as np

before = np.array([[1,2,3,4],[5,6,7,8]])
print(before)

after = before.reshape((8,1)) # 모양 조정
print(after)
after = before.reshape((2,2,2))
print(after)

v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])
print(np.vstack([v1,v2,v1,v2])) # 위에서 아래로 쌓기

h1 = np.ones((2,4))
h2 = np.zeros((2,2))
print(np.hstack((h1,h2))) # 왼쪽에서 오른쪽으로 쌓기

arr = np.arange(12)
print(arr)

arr.resize(3,4)
print(arr)

arr = arr.ravel()
print(arr)

arr = np.arange(1,13)
print(arr)

arr = arr.reshape(3,-1)
print(arr)

arr = arr.reshape(3,2,-1)
print(arr)

arr = np.array([1,2])
print(arr)

arr = np.expand_dims(arr, axis=1) # axis를 기준으로 크게 늘려줌
print(arr)

arr = np.squeeze(arr, axis=1) # axis를 기준으로 작게 줄여줌
print(arr)

arr = np.array([[1,2],[3,4]]) # transpose (전치)
print(arr.T)
