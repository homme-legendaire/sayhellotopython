import numpy as np

a=np.zeros(5) # 원소값 0 크기 5인 1차원배열
print(a)
a=np.zeros((2,3)) # 원소값 0 크기 2x3인 2차원배열
print(a)

a = np.ones((4,4,2), dtype='int32') # 원소값 1 크기 4x4x2 & int32인 3차원배열
print(a)

a = np.full((2,2),99) # 원하는 값으로 채우기 (크기,원소값)
print(a)

b = np.full_like(a,5) # 다른 배열의 크기 가져오기 1
print(b)
b = np.full(a.shape,5) # 다른 배열의 크기 가져오기 2
print(b)

c = np.random.rand(4,2) # 랜덤원소값 들어가는 배열 생성
print(c)
c = np.random.random_sample(a.shape)
print(c)

a = np.random.randint(-4,7, size=(3,3)) # (a,b) a는 랜덤범위, size는 크기
print(a)

print(np.identity(3)) # 단위 행렬

arr = np.array([[1,2,3]]) # 값 반복되는 행렬 생성
r1 = np.repeat(arr,3, axis=0)
print(r1)

a = np.array([1,2,3])
b=a.copy()
b[0]=100
print(a)
print(b)
