N = int(input())
m = 1
mul = 1
result = 0
cnt = 0
while m != 0:
    m = int(input())
    if m < 0:
        print("Error!")
        continue
    elif m == N:
        cnt += 1
    m *= mul
    result += m
    mul *= 10
print(f"Result = {result}")
if result != 0:
    print(f"Count = {cnt}")
