import bisect


def binaryIns2(x):
    for i in range(1, len(x)):
        bisect.insort(x, x.pop(i), 0, i)
    return x


data = [6, 4, 3, 7, 1, 9, 8]
result = binaryIns2(data)
print(result)
