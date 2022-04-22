n = int(input())
for _ in range(n):
    val = int(input())
    print('%2d' %val, end=' ')
    for _ in range(val):
        print('*', end='')
    print()

