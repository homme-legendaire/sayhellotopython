import numpy as np

a = np.array([1,2,3,4]) # 넘파이 연산
print(a)
print(a+2)
print(a-2)
print(a*2)
print(a/2)
b = np.array([1,0,1,0])
print(a+b)
print(a**2)
print(np.sin(a))

a = np.ones((2,3))
print(a)
b = np.full((3,2),2)
print(b)

print(np.matmul(a,b)) # 행렬곱

c = np.identity(3) # determinant 찾기
print(np.linalg.det(c))

stats = np.array([[1,2,3],[4,5,6]])
print(np.min(stats)) # 최소값 구하기
print(np.min(stats, axis=1))
print(np.sum(stats))
print(np.sum(stats, axis=0))