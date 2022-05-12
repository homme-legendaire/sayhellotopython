a = [2, 3, 1, 4]
max = 0
print(f'a = {a}')
for i in range(len(a)):
    if max < a[i]:
        max = a[i]
    print(i, max)
print(f'Max = {max}')
