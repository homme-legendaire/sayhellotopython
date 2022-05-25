def merge_sort(a, b, c):
    pa, pb, pc = 0, 0, 0  # 각 배열의 커서
    na, nb, nc = len(a), len(b), len(c)  # 각 배열의 원소 수

    while pa < na and pb < nb:  # pa와 pb를 비교하여 작은 값을 pc에 저장
        if a[pa] <= b[pb]:
            c[pc] = a[pa]
            pa += 1
        else:
            c[pc] = b[pb]
            pb += 1
        pc += 1

    while pa < na:  # a에 남은 원소를 c에 복사
        c[pc] = a[pa]
        pa += 1
        pc += 1

    while pb < nb:  # b에 남은 원소를 c에 복사
        c[pc] = b[pb]
        pb += 1
        pc += 1

    return c


a = [2, 4, 6, 8, 11, 13]
b = [1, 2, 3, 4, 9, 16, 21]
c = [0] * (len(a)+len(b))

result = merge_sort(a, b, c)
print(c)
