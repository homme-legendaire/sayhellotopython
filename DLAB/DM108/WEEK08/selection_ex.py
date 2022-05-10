
a = [6, 4, 8, 3, 1, 9, 7]

n = len(a)
for i in range(n - 1):
    min = i  # 정렬 할 부분에서 가장 작은 원소의 인덱스
    for j in range(i + 1, n):
        if a[j] < a[min]:
            min = j
    a[i], a[min] = a[min], a[i]  # 정렬 할 부분에서 맨 앞의 원소와 가장 작은 원소를 교환

print(a)