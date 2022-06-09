da1 = {}
da2 = {}
result = {}
str1 = ''
while True:
    gye, cha = map(int, input().split())
    da1[cha] = gye
    if cha == 0:
        break
while True:
    gye, cha = map(int, input().split())
    da2[cha] = gye
    if cha == 0:
        break
for i in da1:
    result[i] = da1[i]
for i in da2:
    if i in result:
        result[i] += da2[i]
    else:
        result[i] = da2[i]
result = dict(reversed(sorted(result.items())))
cnt = 0
for k, v in result.items():
    cnt += 1
    if cnt == 1:
        str1 += f'{v}x^{k}'
        continue
    if k == 0:
        if v != 0:
            str1 += f'+ {v}'
        continue
    str1 += f'+ {v}x^{k}'
print(str1)
