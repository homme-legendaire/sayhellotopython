import numpy as np

list = ['1','2','3']

print(type(list))

a = np.ones((2,3))
print(a)
b = np.full((3,2),2)
print(b)

print(np.matmul(a,b))

a = np.array([1,2,3])
print(a)
print(a.dtype)
b = np.asarray(a,dtype=np.float32)
print(b)
print(b.dtype)
