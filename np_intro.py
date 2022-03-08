import numpy as np

a = np.array([1,2,3]) # 1차원 배열 선언
print(a)

b=np.array([[9.0,8.0,7.0],[6.0,5.0,4.0],[3.0,2.0,1.0]]) # 2차원 배열 선언
print(b)

print(a.ndim, b.ndim) # 몇차원 배열인지
print(a.shape, b.shape) # 모양 ex) 행,렬의 수
print(a.dtype,b.dtype) # 데이터타입&크기 ex) int=32 float=64

c = np.array([1,2,3], dtype='int16') # 선언할때 크기를 정해줄 수 있음
print(c.dtype)

print(a.itemsize, b.itemsize, c.itemsize) # 사이즈 8비트 = 1
print(a.nbytes, b.nbytes, c.nbytes) # 사이즈 * 원소개수