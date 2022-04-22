def sum_besu(n1, n2, num):
    total = 0
    for i in range(n1,n2+1):
        if i % num == 0:
            total += i

    return total

n1 = int(input("시작하는 숫자: "))
n2 = int(input("끝나는 숫자: "))
n = int(input("합계를 구할 배수: "))

result = sum_besu(n1,n2,n)
print(f'배수의 합계: {result}')

