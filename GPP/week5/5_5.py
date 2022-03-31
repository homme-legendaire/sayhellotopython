n = int(input())
for i in range(n+1):
    print(f"{str(i).zfill(2)}:00")
    if i == 23:
        break
