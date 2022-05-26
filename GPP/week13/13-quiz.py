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
        i = int(code[1])
        j = int(code[2])
        N = int(code[3:])
        drink[i][j] += N
    elif code[0] == 's':
        i = int(code[1])
        j = int(code[2])
        N = int(code[3:])
        snack[i][j] += N
    elif code[0] == 'n':
        break
    else:
        print('Wrong Input')
print(drink)
print(snack)
