y1, m1, d1 = map(int, input().split())
y2, m2, d2 = map(int, input().split())

month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def isLeap(year):
    if year % 4 != 0:
        return 0
    if year % 100 != 0:
        return 1
    if year % 400 == 0:
        return 1
    return 0


def counting_day(y, m, d):
    total = 0
    for i in range(y):
        total += 365+isLeap(i)
    for i in range(m-1):
        if i == 1:
            total += isLeap(y)
        total += month[i]
    total += d
    return total


if (y2 == y1+1000 and m2 >= m1 and d2 >= d1) or y2 > y1+1000:
    print('gg')
else:
    d_day = counting_day(y2, m2, d2)-counting_day(y1, m1, d1)
    print(f"D-{d_day}")
