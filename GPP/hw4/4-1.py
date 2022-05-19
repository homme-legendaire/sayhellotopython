A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(f'A: {round(sum(A)/3,1)}')
print(f'B: {round(sum(B)/3,1)}')
print('A awards: ', end='')
for i in range(3):
    if A[i] >= 90:
        if i == 0:
            print('Korean ', end='')
        elif i == 1:
            print('Math ', end='')
        else:
            print('English ', end='')
print()
print('B awards: ', end='')
for i in range(3):
    if B[i] >= 90:
        if i == 0:
            print('Korean ', end='')
        elif i == 1:
            print('Math ', end='')
        else:
            print('English ', end='')
