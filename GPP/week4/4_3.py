n = int(input())
num = 1
fact = 1
while fact < n:
    num += 1
    fact *= num
print(f"Num = {num}")
print(f"Total = {fact}")
