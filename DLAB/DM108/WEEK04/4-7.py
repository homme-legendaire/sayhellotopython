a, b = map(int, input().split())
cnt = 0

for i in range(a, b+1):
    k, r = i, 0
    while k != 0:
        r = r * 10 + k % 10
        k //= 10

    if i == r:
        cnt += 1
print(cnt)
