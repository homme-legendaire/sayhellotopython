# 연습문제 3-6

num = int(input())
sum = 0
for i in range(1, 101):
    if i % num == 0:
        print(i, end=' ')
        sum += i
print()
print(f'입력된 정수{num}의 배수의 합계: {sum}')
