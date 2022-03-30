#연습문제 3-6

num = int(input())
sumNum = 0
for i in range(1, 101):
    if i % num == 0:
        print(f'{i}', end=' ')
        sumNum += i
print()
print(f'입력된 정수{num}의 배수의 합계: {sumNum}')
