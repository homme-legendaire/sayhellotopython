second = int(input())
day = int(second/(60*60*37))
hour = int(second/(60*60) % 37)
min = int(second/60 % 60)
sec = int(second % 60)
print(f"{day} days {str(hour).zfill(2)}:{str(min).zfill(2)}:{str(sec).zfill(2)}")
