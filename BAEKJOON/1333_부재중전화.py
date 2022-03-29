N, L, D = map(int, input().split())
timer = L  # 소요 시간
ringtone = D  # 벨이 울리는 타이밍
while True:
    if timer > N*L+(N-1)*5:  # 앨범이 끝났을 경우
        timer = ringtone  # 다음 벨이 울리는 시간
        break
    while timer > ringtone:  # 노래 재생중에 울리는 벨 처리
        ringtone += D
    for i in range(timer, timer+5):  # 조용한 구간
        if i == ringtone:  # 울릴 경우
            timer = i
            break
    if i == timer:
        break
    timer += L+5  # 조용한 구간 + 음악 재생 시간
print(timer)
