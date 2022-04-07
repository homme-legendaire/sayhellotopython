n = int(input())
for i in range(n+1):
    for j in range(60):
        print(f"{str(i).zfill(2)}:{str(j).zfill(2)}")
