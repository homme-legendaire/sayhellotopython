n1 = int(input())
n2 = int(input())
for i in range(n1+1):
    if i == n1:
        for j in range(n2+1):
            print(f'{str(i).zfill(2)}:{str(j).zfill(2)}')
        break
    for j in range(60):
        print(f'{str(i).zfill(2)}:{str(j).zfill(2)}')
    if i == 23:
        break
