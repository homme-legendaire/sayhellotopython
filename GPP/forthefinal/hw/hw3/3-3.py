N = int(input())
result = 0
cnt = 0
cnt2 = 0
while True:
    n = int(input())
    if n == N:
        cnt2 += 1
    for _ in range(cnt):
        n *= 10
    if n == 0:
        break
    if n < 0:
        print('Error!')
        continue
    result += n
    cnt += 1
print(f'Result = {result}')
if cnt > 0:
    print(f'Count = {cnt2}')
