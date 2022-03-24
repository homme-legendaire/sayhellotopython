count = 0
total = 0
while total < 20:
    dice = int(input())
    count += 1
    if dice == 4:
        break
    total += dice
print(f"Count = {count}")
print(f"Total = {total}")
