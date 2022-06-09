year = int(input())
sm = int(input())
em = int(input())
sd = int(input())
ed = int(input())
for i in range(sm, em+1):
    if i % 2 == 0 and ed == 31:
        for j in range(sd, ed):
            print(f'{str(year).zfill(2)}{str(i).zfill(2)}{str(j).zfill(2)}', end='')
            if i == j:
                print(" Lucky Day!")
            else:
                print()
    else:
        for j in range(sd, ed+1):
            print(f'{str(year).zfill(2)}{str(i).zfill(2)}{str(j).zfill(2)}', end='')
            if i == j:
                print(" Lucky Day!")
            else:
                print()
