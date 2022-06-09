p = [0, 0, 0]
n = int(input())
for _ in range(n):
    for i in range(3):
        card = int(input())
        if p[i] < card:
            p[i] = card
    print(p)
print(f'Person{p.index(max(p))+1} Win')
