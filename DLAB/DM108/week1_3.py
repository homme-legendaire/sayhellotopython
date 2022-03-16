import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr)

arr = np.full(3, 6)
print(arr)

arr = np.zeros(4, dtype=int)
print(arr)

arr = np.ones(4, dtype=int)
print(arr)

arr = np.random.random(6)
print(arr)

arr = np.random.choice(10, 5)
print(arr)

arr = np.arange(4)
print(arr)

arr = np.arange(2, 8)
print(arr)

arr = np.arange(3, 16, 3)
print(arr)

arr = np.arange(6, 80, 6)
print(arr)

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr)
