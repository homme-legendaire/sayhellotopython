hour = int(input())
min = int(input())
carrot_min = int(input())
carrot = int(input())
cnt = 0
while hour < 22:
    print(f'{str(hour).zfill(2)}:{str(min).zfill(2)} Carrot Time!')
    hour += (carrot_min//60)
    min += (carrot_min % 60)
    while min > 60:
        hour += 1
        min -= 60
    cnt += 1
    if cnt == carrot:
        break
if carrot > cnt:
    print('Emergency!')
