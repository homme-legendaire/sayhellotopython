a = int(input())
b = int(input())
sum = a+b
if sum % 3 == 0:
    if sum % 6 == 0:
        print(f"{sum} is multiple of 3 and 6")
    else:
        print(f"{sum} is multiple of 3")
else:
    print(f"{sum} is not multiple of 3 or 6")
