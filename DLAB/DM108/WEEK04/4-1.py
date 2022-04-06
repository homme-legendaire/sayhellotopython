# 연습문제4-1

n, cnt = 0, 0
while n < 100:
    n += 1
    if n % 2 == 1:
        print(n, end=' ')
        cnt += 1
        if cnt % 5 == 0:
            print()
