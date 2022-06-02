num = input()
str1 = ""
cnt = []
idx = 0
for i in num:
    if i not in str1:
        cnt.append(0)
        str1 += i
        for j in num:
            if i == j:
                cnt[idx] += 1
        idx += 1
print('result = ', end='')
for i in range(len(cnt)):
    print(f'{str1[i]}{cnt[i]}', end='')
