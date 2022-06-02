small = input()
alpha = 'abcdefghijklmnopqrstuvwxyz'
for i in small:
    cnt = 0
    for j in small:
        if i == j:
            cnt += 1
    print(alpha[cnt-1], end='')
