# 연습문제 3-8
num = int(input())
even, odd = 0, 0

for i in range(1, num+1):
    if i % 2 == 0:
        even += i
    else:
        odd += i

print(f'짝수의 합: {even}, 홀수의 합: {odd}')
