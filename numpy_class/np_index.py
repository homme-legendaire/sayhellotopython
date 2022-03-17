import numpy as np

a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(a)
print(a[1,5]) # 원하는 원소에 접근 r:c
print(a[0,:])
print(a[:,1])
print(a[0,1:6:2])
a[1,5] = 20 # 원하는 위치에 새로운 값 삽입
print(a)
a[:,2] = 5 # 원하는 열에 새로운 값 삽입
print(a)

b = np.array([[[1,2],[3,4]],[[5,6],[7,8]]]) # 3차원 배열
print(b)
print(b[0,1,1]) # 원하는 원소에 접근
print(b[:,0,:])
b[:,1,:] = [[9,9],[8,8]] # 원소 값 변경
print(b)