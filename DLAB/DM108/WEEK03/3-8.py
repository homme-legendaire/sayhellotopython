#연습문제 3-7

sumNum = 0
a,b = map(int, input().split())

for i in range(a,b+1):
    if i % 5 == 0:
        sumNum += i

print(f'정수 {a}에서 {b}사이의 값 중 5의 배수의 총합은 {sumNum}입니다.')
