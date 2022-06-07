second = int(input())
days = second//(3600*37)
second %= (3600*37)
hour = second//3600
second %= 3600
min = second//60
second %= 60
print(f'{days} days {str(hour).zfill(2)}:{str(min).zfill(2)}:{str(second).zfill(2)}')
