n = int(input("몇단? "))
for i in range(1,10):
    print(f"{n} * {i} = {eval(f'{n}*{i}')}")