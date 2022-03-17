import numpy as np
# 1
print("1")
arr = np.full((3, 4, 5), 3)
print(arr)

# 2
print("2")
arr = np.random.randint(-50, 50, (4, 5))
print(arr)
print(np.sort(arr))
print(np.sort(arr, axis=None))

# 3
print("3")
py_list = [np.full(3, 8), np.array([33, -15, 26]), np.linspace(17, 26, 3)]
result_arr = []
for i in py_list:
    result_arr.append(np.mean(i))
    result_arr.append(np.std(i))
    result_arr.append(np.median(i))
print(result_arr)

# 4
print("4")
arr = np.arange(2, 20, 2).reshape((3, 3))
print(arr)

s1 = np.vsplit(arr, 3)
print(s1)
s2 = np.square(s1)
print(s2)
s3 = np.squeeze(s2, axis=1)
print(s3)
print(np.concatenate((arr, s3)))
