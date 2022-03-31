num = int(input())
sum1 = 0
sum2 = 0
for i in range(num+1):
    if i % 2 != 0:
        sum1 += i
        continue
    sum2 += i
print(f"Sum1 = {sum1}")
print(f"Sum2 = {sum2}")
