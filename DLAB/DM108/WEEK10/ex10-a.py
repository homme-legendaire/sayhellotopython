def bfs(graph, start):
    qu = []
    done = set()
    qu.append(start)
    done.add(start)

    while qu:           #처리할 꼭짓점이 남아 있으면
        p = qu.pop(0)   #큐에서 처리할 대상을 꺼냄
        print(p)        #꼭짓점 이름을 출력
        for x in graph[p]:      #대상 꼭짓점에 연결된 꼭짓점들 중에서
            if x not in done:   #아직 큐에 추가된 적이 없는 꼭짓점들을
                qu.append(x)    #큐에 추가
                done.add(x)     #집합에도 추가

graph = {
    1 : [2,3],
    2 : [1, 4, 5],
    3 : [1],
    4 : [2],
    5 : [2]
}

bfs(graph, 1)