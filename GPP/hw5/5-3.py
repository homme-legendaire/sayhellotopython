a_win = 0
b_win = 0
set = 0

for i in range(6):
    a_score = 0
    b_score = 0
    set += 1
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
