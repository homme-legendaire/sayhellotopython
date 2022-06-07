bill = 0
cash = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

for i in cash:
    bill += int(input())*i
print(f'{bill} won')
