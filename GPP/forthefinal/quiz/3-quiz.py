sum = 0
for _ in range(2):
    sum += int(input())

if sum % 3 == 0:
    if sum % 6 == 0:
        print(f"{sum} is multiple of 3 and 6")
    else:
        print(f"{sum} is multiple of 3")
else:
    print(f"{sum} is not multiple of 3 or 6")
