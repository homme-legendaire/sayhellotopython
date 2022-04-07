n = int(input())
m = int(input())
for i in range(n):
    for j in range(n):
        if i == m-1:
            print('*', end='')
            continue
        if j < m-1 or j > m-1:
            print(' ', end='')
            continue
        print('*', end='')
    print()
