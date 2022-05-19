dic = {}
while True:
    N = int(input())
    if N == 0:
        break
    elif N == 1:
        name = input()
        score = int(input())
        dic[name] = score
    else:
        name = input()
        if name in dic:
            print(f'Name = {name}, Score = {dic[name]}')
        else:
            print('No student')
