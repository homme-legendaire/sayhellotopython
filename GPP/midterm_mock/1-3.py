book = int(input())
num = int(input())
if book == 1:
    if num <= 5:
        print("The Alchemist")
        print(f"{5-num}")
    else:
        print("Not exist")
elif book == 2:
    if num <= 5:
        print("Koguryo")
        print(f"{5-num}")
    else:
        print("Not exist")
else:
    if num <= 5:
        print("Empire of the angels")
        print(f"{5-num}")
    else:
        print("Not exist")
