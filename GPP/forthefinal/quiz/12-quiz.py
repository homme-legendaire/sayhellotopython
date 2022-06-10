result = {}
while True:
    n = int(input())
    if n == 1:
        name = input()
        score = int(input())
        result[name] = score
    elif n == 2:
        name = input()
        if name in result:
            print(f'Name = {name}, Score = {result[name]}')
        else:
            print('No student')
    else:
        break
