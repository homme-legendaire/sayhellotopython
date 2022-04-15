p1 = int(input())
p2 = int(input())
p3 = int(input())
if p1 > p2 and p1 > p3:
    print(f"Max = {p1}")
elif p2 > p1 and p2 > p3:
    print(f"Max = {p2}")
else:
    print(f"Max = {p3}")
