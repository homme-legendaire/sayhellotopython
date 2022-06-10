result = {}
n = input()
for i in n:
    if i not in result:
        cnt = 0
        for j in n:
            if i == j:
                cnt += 1
        result[i] = cnt
print('result =', end=' ')
for k, v in result.items():
    print(f'{k}{v}', end='')
