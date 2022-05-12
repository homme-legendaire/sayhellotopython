n = int(input())
s = []
for i in range(n):
    m = int(input())
    s.append(m)
print(s)
print('Avg = %.2f' % (sum(s)/len(s)))
