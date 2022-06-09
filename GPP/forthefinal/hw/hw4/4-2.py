fruits = []
while True:
    N = int(input())
    fruits.append(N)
    if N == 0:
        break
idx = 0
a_score = 0
b_score = 0
while True:
    A = int(input())
    while A > 0:
        A -= 1
        a_score += fruits[idx]
        idx += 1
        if idx >= len(fruits):
            break
    if idx >= len(fruits):
        a_score -= 5
        break
    B = int(input())
    while B > 0:
        B -= 1
        b_score += fruits[idx]
        idx += 1
        if idx >= len(fruits):
            break
    if idx >= len(fruits):
        b_score -= 5
        break


print(f'A: {a_score}')
print(f'B: {b_score}')
if a_score > b_score:
    print('A wins!')
elif a_score == b_score:
    print('Draw!')
else:
    print('B wins!')
