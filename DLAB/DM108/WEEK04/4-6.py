a, b = map(int, input().split())
a2, b2 = 0, 0

while a != 0:
    a2 = a2 * 10 + a % 10
    a //= 10

while b != 0:
    b2 = b2 * 10 + b % 10
    b //= 10

if a2 > b2:
    print(a2)
else:
    print(b2)


