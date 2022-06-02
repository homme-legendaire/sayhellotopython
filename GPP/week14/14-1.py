hour = int(input())
min = int(input())
interval = int(input())
carrot = int(input())

cnt = 0

while True:
    print(f'{str(hour).zfill(2)}:{str(min).zfill(2)} Carrot Time!')
    cnt += 1
    min += interval
    while min >= 60:
        hour += 1
        min -= 60
    if cnt == carrot:
        break
    if hour >= 22:
        print('Emergency!')
        break
