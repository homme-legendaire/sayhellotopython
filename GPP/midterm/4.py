n = int(input())
total = 0
for i in range(n):
    sex = input()
    weight = int(input())
    if sex == 'M':
        if weight >= 50:
            total+=1
    else:
        if weight >= 45:
            total+=1
print(f"total = {total}")
rate = total / n * 100
print("rate : %.2f" % rate)
