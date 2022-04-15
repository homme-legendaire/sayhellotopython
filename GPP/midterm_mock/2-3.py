sum = 0
cnt = 0
money = 0
while sum < 1000:
    money = int(input())
    if money == 0:
        break
    sum+=money
    cnt+=1
print(f"Count = {cnt}")
if sum >= 1000:
    print(f"Balance = {sum-1000}")
else:
    print(f"Balance = {sum}")
