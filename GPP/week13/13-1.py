dic = {'white': 1000, 'yellow': 2000, 'blue': 3000, 'red': 5000}
price = 0
while True:
    plate = input()
    if plate not in dic:
        break
    for i in dic:
        if i == plate:
            price += dic[plate]
print(f'Total price = {price}')
