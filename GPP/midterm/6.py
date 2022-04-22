n = int(input())
i = 1
j = 1
tmp = 0
fibonacci = False
while i <= 2000:
    if n == i:
        fibonacci = True
        break
    tmp = i
    i+=j
    j=tmp
if fibonacci:
    print(f"{n} is a Fibonacci number.")
else:
    print(f"{n} is not a Fibonacci number.")
