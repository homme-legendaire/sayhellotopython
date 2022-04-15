n = int(input())
max = 0
for i in range(n):
    score = 0
    for j in range(2):
        score += int(input())
    average = score/2
    if average > max:
        max = average
print(f"Average = {max}")
