list = []
sum = 0
for i in range(9):
    list.append(int(input()))
    sum += list[i]
for i in list:
    for j in list:
        result = sum
        if i != j:
            result -= (i+j)
            if result == 100:
                list.remove(i)
                list.remove(j)
                break
    if result == 100:
        break
list.sort()
for i in list:
    print(i)
