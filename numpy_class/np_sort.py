import numpy as np

arr = np.random.randint(10,size=10)
print(arr)

print(np.sort(arr)) # 정렬 (오름차순)
print(np.sort(arr)[::-1]) # 정렬 (내림차순)

arr = np.random.randint(15,size=(3,4))
print(arr)

print(np.sort(arr)) # 정렬
print(np.sort(arr,axis=0)) # 열 기준으로
