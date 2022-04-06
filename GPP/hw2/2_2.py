n1 = int(input())
n2 = int(input())
n3 = int(input())
mid = 0
if n1 >= n2:
    if n2 >= n3:
        mid = n2
    elif n3 >= n1:
        mid = n1
    else:
        mid = n3
elif n3 < n1:
    mid = n1
elif n2 > n3:
    mid = n3
else:
    mid = n2

if mid == n3:
    print(f"Median is n3. n3 is {n3}.")
elif mid == n2:
    print(f"Median is n2. n2 is {n2}.")
else:
    print(f"Median is n1. n1 is {n1}.")
