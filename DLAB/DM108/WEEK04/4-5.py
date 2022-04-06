result = []
for i in range(1, 101):
    k = 1
    while k * k < i:
        k += 1
    if k * k == i:
        result.append(i)

print(result)
print(f'1부터 100사이의 완전제곱수의 개수는 {len(result)}개 입니다.')
