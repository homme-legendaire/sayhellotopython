list = []
for i in range(10):
    n = int(input())
    if n in list:
        print("exist")
        continue
    list.append(n)
print(list)
