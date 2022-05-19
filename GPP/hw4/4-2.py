list = []
while True:
    n = int(input())
    list.append(n)
    if n == 0:
        break
score_a = 0
score_b = 0
idx = 0
while True:
    A = int(input())
    if idx+A > len(list)-1:
        score_a -= 5
        break
    for i in range(idx, idx+A):
        score_a += list[i]
    idx += A

    B = int(input())
    if idx+B > len(list)-1:
        score_b -= 5
        break
    for i in range(idx, idx+B):
        score_b += list[i]
    idx += B


print(f'A: {score_a}')
print(f'B: {score_b}')
if score_a > score_b:
    print('A wins!')
elif score_a < score_b:
    print('B wins!')
else:
    print('Draw!')
