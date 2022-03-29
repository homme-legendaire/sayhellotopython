while True:
    teams = 0
    match = 0
    add_team = 0
    i = 1
    G, T, A, D = map(int, input().split())  # 그룹, 팀, 토너먼트 진출, 토너먼트 직행
    if G == -1:
        break
    match = T*(T-1)//2*G  # 조별리그 매치 수 계산
    teams = G*A+D  # 조별리그를 거친 토너먼트 진출 팀의 수
    while i < teams:  # 토너먼트 진행에 추가로 필요한 팀 계산
        i *= 2
    add_team = i-teams
    teams += add_team
    match += teams-1
    print(f"{G}*{A}/{T}+{D}={match}+{add_team}")
