a,b,c,d = input().split()
s = ['+', '-', '*', '/', '%']
for i in s:
    for j in s:
        if (j!=i):
            if (int(d)==eval(f'{a}{i}{b}{j}{c}')):
                print(f'{a}{i}{b}{j}{c}={d}')
