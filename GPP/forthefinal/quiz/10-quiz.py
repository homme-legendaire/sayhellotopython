L = []
N = int(input())
for i in range(N):
    L.append(int(input()))
print(L)
A = int(input())
B = int(input())
for i in range(A, B+1):
    for j in range(i, B+1):
        if L[i] < L[j]:
            L[i], L[j] = L[j], L[i]
            print(L)
