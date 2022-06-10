n = int(input())
m = int(input())
drink = [[]]*n
for i in range(n):
    drink[i] = [0]*n
snack = [[]]*m
for i in range(m):
    snack[i] = [0]*m
while True:
    code = input()
    if code[0] == 'd':
        row = int(code[1])
        column = int(code[2])
        drink[row][column] += int(code[3:])
    elif code[0] == 's':
        row = int(code[1])
        column = int(code[2])
        snack[row][column] += int(code[3:])
    elif code[0] == 'n':
        break
    else:
        print('Wrong Input')
print(drink)
print(snack)
