s = []
while True:
    n = int(input())
    if n == 0:
        break
    s.append(n)
print(s)
print('Avg = %.2f' % (sum(s)/len(s)))
