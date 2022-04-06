g = int(input())
cnt = 0

for i in range(1,11):
    for j in range(1,11):
        for k in range(1,11):
            if i*2 + j*3 + k*5 == g:
                print(i,j,k)
                cnt += 1

print(cnt)

