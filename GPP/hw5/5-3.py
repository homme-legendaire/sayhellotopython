a_win = 0
b_win = 0
set = 0
a_score = []
b_score = []

for i in range(6):
    a_score.append(0)
    b_score.append(0)
    set += 1
    if set == 6:
        A, B = map(int, input().split())
        a_score[i] = A
        b_score[i] = B
        if A > B:
            a_win = 6
        elif B > A:
            b_win = 6
        break
    for j in range(3):
        a, b = map(int, input().split())
        a_score[i] += a
        b_score[i] += b
    if a_score[i] > b_score[i]:
        a_win += 2
    elif a_score[i] == b_score[i]:
        a_win += 1
        b_win += 1
    else:
        b_win += 2
    if a_win == 6:
        break
    elif b_win == 6:
        break
str1 = "Person1 | "
str2 = "Person2 | "
for i in range(set):
    str1 += f'{a_score[i]} '
    str2 += f'{b_score[i]} '
str1 += f'| {a_win}'
str2 += f'| {b_win}'
print(str1)
print(str2)
if a_win == 6:
    print('Person1 win')
elif b_win == 6:
    print('Person2 win')
else:
    print('need to check target')
