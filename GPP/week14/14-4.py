student = {}
while True:
    n = int(input())
    if n == 1:
        name = input()
        score = int(input())
        student[name] = score
    elif n == 2:
        name = input()
        if name in student:
            print(f'Name = {name}, Score = {student[name]}')
        else:
            print('No student')
    else:
        break
