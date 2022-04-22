
a, b, c = map(int, input().split())
x = a * b * c

count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
while x:
    count[x % 10] += 1
    x //= 10

for i in range(10):
    print(count[i])

