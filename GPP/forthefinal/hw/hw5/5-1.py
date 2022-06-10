alpha = "abcdefghijklmnopqrstuvwxyz"
sentence = input()
for i in sentence:
    cnt = 0
    for j in sentence:
        if i == j:
            cnt += 1
    print(alpha[cnt-1], end='')
