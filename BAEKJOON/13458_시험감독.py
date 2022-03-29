N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
cnt = 0
for i in A:
    i -= B  # 총감독관 한 명
    cnt += 1
    while i > 0:  # 부감독관의 수 계산
        if i <= C:
            cnt += 1
            break
        cnt += i//C
        i %= C
print(cnt)
