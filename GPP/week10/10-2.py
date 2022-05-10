n = int(input())
list = []
for i in range(n):
    m = int(input())
    list.append(m)
while True:
    x = int(input())
    if x in list:
        print("YES")
    elif x == 0:
        break
    else:
        print("NO")
