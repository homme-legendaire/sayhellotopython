def findFriends(graph, start):
    qu = []
    done = set()

    qu.append((start,0))    #(사람이름, 친밀도) 정보를 튜플로 추가 // 자기 자신의 친밀도 : 0
    done.add(start)

    while qu:               #큐에 처리할 사람이 남아 있다면
        (p, d) = qu.pop(0)  #사람이름과 친밀도 정보를 p와 d로 각각 꺼냄
        print(f'친구:{p}, 친밀도:{d}')   #꺼낸 정보를 출력
        for x in graph[p]:
            if x not in done:
                qu.append((x, d+1))   #친밀도를 1 증가시켜 큐에 추가
                done.add(x)

fr_info = {
    'Steve':['Jake', 'John', 'Mike'],
    'Jake':['Steve','John'],
    'John':['Jake','Steve','Mike','May'],
    'Mike':['Steve','John'],
    'May':['John','Kate'],
    'Kate':['May'],
    'Tom':['Jerry'],
    'Jerry':['Tom'],
}

findFriends(fr_info, 'Steve')


