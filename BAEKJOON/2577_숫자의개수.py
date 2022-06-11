A = int(input())
B = int(input())
C = int(input())
result = str(A*B*C)
for i in range(10):
    cnt = 0
    for j in result:
        if i == int(j):
            cnt += 1
    print(cnt)
