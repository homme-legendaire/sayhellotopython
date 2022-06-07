n1 = int(input())
n2 = int(input())
n3 = int(input())
if (n1 > n2 and n1 < n3) or (n1 < n2 and n1 > n3):
    print(f'Median is n1. n1 is {n1}.')
elif (n2 >= n1 and n2 < n3) or (n2 <= n1 and n2 > n3):
    print(f'Median is n2. n2 is {n2}.')
else:
    print(f'Median is n3. n3 is {n3}.')
