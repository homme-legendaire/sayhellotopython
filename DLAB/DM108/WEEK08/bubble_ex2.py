
a = [6, 4, 3, 7, 1, 9, 8]
n = len(a)

for i in range(n-1):
    exchange = 0    #패스에서 교환 횟수
    for j in range(n-1, i, -1):
        if a[j-1] > a[j]:
            a[j-1], a[j] = a[j], a[j-1]
            exchange += 1

    if exchange == 0:
        break

print(a)


