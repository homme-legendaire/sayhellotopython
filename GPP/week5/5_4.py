sum = 0
for i in range(10):
    dice = input()
    if dice == 'yellow':
        continue
    elif dice == 'red':
        break
    else:
        num = int(input())
        sum += num
print(f"Sum = {sum}")
