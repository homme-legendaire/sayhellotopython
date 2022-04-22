
n = int(input())
a = list(map(int, input().split()))
even, odd = 0, 0

for i in range(n):
    if a[i] % 2 == 0:
        even += 1
    else:
        odd += 1

print(even)
print(odd)
