def sum(start, end):
    total = 0
    for i in range(start, end+1):
        total += i
    print(f'{start}부터 {end}의 정수의 합계:{total}')


sum(10, 100)
sum(100, 1000)
