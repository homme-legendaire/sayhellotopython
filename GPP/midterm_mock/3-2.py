n = int(input())
max = 0
for i in range(n):
    score = int(input())
    if max<score:
        max = score
print(f"Max = {max}")
