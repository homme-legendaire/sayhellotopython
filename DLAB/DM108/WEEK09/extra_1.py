from collections import deque

qu = deque()
qu.append('a')  #'a'를 큐에 추가
qu.append('b')  #'b'를 큐에 추가
qu.popleft()    #큐에서 'a'를 꺼냄

print(qu)


