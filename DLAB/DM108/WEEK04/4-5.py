result = []
k = 1
for i in range(1, 101):
    if k*k < i:
        k += 1
    if k*k == i:
        result.append(i)

print(result)
print(len(result))
