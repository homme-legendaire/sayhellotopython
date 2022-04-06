n = int(input())
cnt = 0

for i in range(1,11):
    for j in range(i+1, 11):
        for k in range(j+1, 11):
            if i + j + k == n:
                print(i,j,k)
                cnt += 1
print(cnt)

