import numpy as np

a = np.array([1,2,3,4]) # 넘파이 연산
print(a)
print(a+2) # 사칙연산
print(a-2)
print(a*2)
print(a/2)
b = np.array([1,0,1,0])
print(a+b) # 행렬끼리 덧셈
print(a**2)
print(np.sin(a)) # 삼각함수

a = np.ones((2,3))
print(a)
b = np.full((3,2),2)
print(b)

print(np.matmul(a,b)) # 행렬곱
print(np.dot(a,b)) # 내적

arr = np.array([[1,-2],[-4,5]])
print(np.abs(arr)) # 절댓값

c = np.identity(3) # determinant 찾기
print(np.linalg.det(c))

stats = np.array([[1,2,3],[4,5,6]])
print(np.min(stats)) # 최소값 구하기
print(np.min(stats, axis=1))
print(np.sum(stats)) # 합 구하기
print(np.sum(stats, axis=0))
print(np.mean(stats)) # 평균 구하기
print(np.mean(stats, axis=0))
print(np.std(stats)) # 표준편차 구하기
print(np.std(stats, axis=0))
print(np.cumsum(stats)) # 누적합
print(np.cumsum(stats, axis=0))

a = np.array([[1,2,3],[4,5,6]])
b = np.array([[1,0,3],[4,-2,9]])
print(a == b)
print(a > b)
print(np.array_equal(a,b))
