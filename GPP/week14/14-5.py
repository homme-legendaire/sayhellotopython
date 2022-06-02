n = int(input())
drink = [[]]*n
for i in range(n):
    drink[i] = [0]*n
m = int(input())
snack = [[]]*m
for i in range(m):
    snack[i] = [0]*m
while True:
    new = input()
    row = int(new[1])
    column = int(new[2])
    q = int(new[3:])
    if new[0] == 'd':
        drink[row][column] += q
    elif new[0] == 's':
        snack[row][column] += q
    elif new[0] == 'n':
        break
    else:
        print('Wrong Input')
print(drink)
print(snack)
