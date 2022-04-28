def process(n):
    cnt = 0
    for i in range(1, n+1):
        if n % i == 0:
            cnt += 1
    if cnt == 2:
        print(f'{n} is prime number')
    else:
        print(f'The number of factors of {n} is {cnt}')


n = int(input())
process(n)
