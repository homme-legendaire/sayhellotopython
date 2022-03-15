N, m, M, T, R = map(int, input().split())
i = 0
cnt = 0
min = m
while i < N:
    if (M - min < T):
        cnt = -1
        break
    if (m+T <= M):
        m += T
        i += 1
    else:
        m -= R
        if(m < min):
            m = min
    cnt += 1
print(cnt)
