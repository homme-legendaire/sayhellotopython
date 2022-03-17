import numpy as np

filedata = np.genfromtxt('data.txt',delimiter=",")
print(filedata)
print(filedata.astype('int32'))
filedata=filedata.astype('int32')

print(filedata>50) # boolean 연산
print(filedata[filedata>50])

a = np.array([1,2,3,4,5,6,7,8,9])
print(a[[1,2,8]])

print(np.any(filedata > 50, axis=0)) # 또는
print(np.all(filedata > 50, axis=0)) # 그리고

print((filedata > 50) & (filedata < 100))
