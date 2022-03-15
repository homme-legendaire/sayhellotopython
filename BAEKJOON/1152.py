str = input()
cnt = 0
if str[0] != ' ':
    cnt += 1
for i in range(len(str)-1):
    if str[i] == ' ':
        if str[i+1] != ' ':
            cnt += 1
print(cnt)
