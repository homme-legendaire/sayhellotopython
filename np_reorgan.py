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