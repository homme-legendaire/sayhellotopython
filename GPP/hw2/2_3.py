date = input()
Y = int(date[:2])
M = int(date[2:4])
D = int(date[4:])

if Y < 10:
    Y += 2000
else:
    Y += 1900

if M > 12 or M < 1:
    print("Wrong")
elif M == 2:
    if D > 29:
        print("Wrong")
    else:
        print(f"{Y}/{M}/{D}")
elif M == 4 or M == 6 or M == 9 or M == 11:
    if D > 30:
        print("Wrong")
    else:
        print(f"{Y}/{M}/{D}")
else:
    if D > 31:
        print("Wrong")
    else:
        print(f"{Y}/{M}/{D}")
