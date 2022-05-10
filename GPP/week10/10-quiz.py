N = int(input())
list = []
for i in range(N):
    n = int(input())
    list.append(n)
A = int(input())
B = int(input())
print(list)
for i in range(A, B+1):
    for j in range(i, B+1):
        if list[i] < list[j]:
            list[i], list[j] = list[j], list[i]
            print(list)
