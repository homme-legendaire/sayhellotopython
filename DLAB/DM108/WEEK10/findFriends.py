def findFriends(graph, start):  #매개변수 : 친구 관계 그래프, 친구 관계를 찾을 사람
    qu = []             #앞으로 처리해야 할 사람들을 저장할 장소
    done = set()        #이미 큐에 추가한 사람들을 집합에 기록

    qu.append(start)    #자신을 큐에 넣고 시작
    done.add(start)     #자신을 집합에 넣고 시작

    while qu:           #큐에 처리할 사람이 남아 있는 동안에
        p = qu.pop(0)   #큐에서 처리 대상을 한 명 꺼내서
        print(p, end=' ')   #이름을 출력
        for x in graph[p]:  #친구들 중에
            if x not in done:   #큐에 추가된 적이 없는 사람을
                qu.append(x)    #큐에 추가
                done.add(x)     #집합에도 추가

#친구 관계 그래프 - 딕셔너리로 표현
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

findFriends(fr_info, 'John')
