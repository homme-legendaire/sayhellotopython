sum = 0
while sum < 20:
    color = input("color: ")
    if color == "red":
        break
    dice = int(input("dice: "))
    sum += dice
print("Sum: ",sum)