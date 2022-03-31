wake_hour = int(input())
wake_min = int(input())
wake_time = wake_hour*60+wake_min
M = int(input())
N = int(input())
for i in range(N):
    print(f"{str(wake_time//60).zfill(2)}:{str(wake_time%60).zfill(2)} Carrot Time!")
    wake_time += M
    carrot = i
    if wake_time//60 >= 22:
        break
if carrot+1 != N:
    print("Emergency!")
