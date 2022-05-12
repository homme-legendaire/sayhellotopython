n = int(input())
p = [0, 0, 0]
for i in range(n):
    for j in range(3):
        m = int(input())
        if m > p[j]:
            p[j] = m
    print(p)
max = max(p)
print(f'Person{p.index(max)+1} Win')
