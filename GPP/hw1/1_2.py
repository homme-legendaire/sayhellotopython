list = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
total = 0
for i in range(8):
    N = int(input())
    total += N*list[i]
print(f"{total} won")
