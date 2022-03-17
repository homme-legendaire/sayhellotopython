a = int(input())
b = int(input())
sum = a+b
if a % 2 == 0 and b % 2 == 0:
    print("All dices are even!")
elif a % 2 != 0 and b % 2 != 0:
    print("All dices are odd!")
