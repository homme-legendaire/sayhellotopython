p1 = []
p2 = []
p1_set = 0
p2_set = 0
for _ in range(5):
    sum1 = 0
    sum2 = 0
    for _ in range(3):
        shoot1, shoot2 = map(int, input().split())
        sum1 += shoot1
        sum2 += shoot2
    if sum1 > sum2:
        p1_set += 2
    elif sum1 < sum2:
        p2_set += 2
    else:
        p1_set += 1
        p2_set += 1
    p1.append(sum1)
    p2.append(sum2)
    if p1_set >= 6 or p2_set >= 6:
        break
if p1_set == p2_set:
    shoot1, shoot2 = map(int, input().split())
    if shoot1 > shoot2:
        p1_set += 1
    elif shoot1 < shoot2:
        p2_set += 1
    p1.append(shoot1)
    p2.append(shoot2)

print('Person1 |', end=' ')
for i in p1:
    print(i, end=' ')
print(f'| {p1_set}')
print('Person2 |', end=' ')
for i in p2:
    print(i, end=' ')
print(f'| {p2_set}')

if p1_set == 6:
    print('Person1 win')
elif p2_set == 6:
    print('Person2 win')
else:
    print('need to check target')
