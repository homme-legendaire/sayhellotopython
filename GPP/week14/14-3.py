p = [0, 0, 0]
n = int(input())
for i in range(n):
    for j in range(3):
        card = int(input())
        if card > p[j]:
            p[j] = card
    print(p)
for i in range(3):
    if p[i] == max(p):
        print(f'Person{i+1} Win')
        break
