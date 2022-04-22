n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))

for i in range(n):
    print('%2d' %a[i], end=' ')
    for _ in range(a[i]):
        print('*', end='')
    print()

