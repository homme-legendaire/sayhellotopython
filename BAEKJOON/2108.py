N = int(input())
list = []
for i in range(N):
    list.append(int(input()))
list.sort()
popular = 0
rank = 0
MAX = 0
for i in list:
    count = 0
    for j in list:
        if i == j:
            count += 1
    if count > MAX:
        rank = 1
        MAX = count
        popular = i
    elif count == MAX and popular != i:
        if rank == 1:
            popular = i
            rank = 2
print(round(sum(list)/N))
print(list[int(N/2)])
print(popular)
print(int(max(list)-min(list)))
