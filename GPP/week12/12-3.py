n = int(input())
for i in range(n):
    a, b, c = map(int, input().split())
    print(f'Student {i+1}\'s Average Score : {round((a+b+c)/3,2)}')
