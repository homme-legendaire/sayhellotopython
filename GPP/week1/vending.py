print("1. Orange Juice")
print("2. Soda")
print("3. Coke")

drink = int(input("음료수를 선택하세요: "))

if (drink == 1):
    price = 600
elif (drink == 2):
    price = 700
else:
    price = 900

coin = 0
while True:
    insert = int(input("동전을 투입하세요: "))
    coin += insert
    if (coin > price):
        print(f"거스름돈: {coin-price}")
        break
    elif (coin == price):
        print("No change")
        break