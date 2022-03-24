count = 0
total = 0
while True:
    dice = int(input())
    count += 1
    total += dice
    if dice == 4:
        break
print(f"Count = {count}, Total = {total}")
