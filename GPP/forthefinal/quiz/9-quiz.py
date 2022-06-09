def yark(n):
    cnt = 0
    for i in range(1, n+1):
        if n % i == 0:
            cnt += 1
    return cnt


def process(n):
    if yark(n) == 2:
        print(f'{n} is prime number')
    else:
        print(f'The number of factors of {n} is {yark(n)}')


n = int(input())
process(n)
