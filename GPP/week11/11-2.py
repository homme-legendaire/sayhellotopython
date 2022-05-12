s = [8, 6, 9, 10, 4, 7, 10, 6, 8, 7]
max = 0
idx = 0
print(f's ={s}')
for i in range(len(s)):
    if max < s[i]:
        max = s[i]
        idx = i
print(f'Max = {max}')
print(f'Idx = {idx}')
