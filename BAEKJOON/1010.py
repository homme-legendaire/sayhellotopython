def combi(N, M):
    ja = 1
    mo = 1
    for j in range(M, M-N, -1):
        ja *= j
    for j in range(1, N+1):
        mo *= j
    return(int(ja/mo))


T = int(input())
for i in range(T):
    N, M = input().split()
    print(combi(int(N), int(M)))
