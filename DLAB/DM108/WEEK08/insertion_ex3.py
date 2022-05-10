def insertion3(k):
    n = len(k)
    for i in range(1, n):   #1부터 n-1까지
        key = k[i]          #1번 위치에 있는 값을 key에 저장
        j = i-1             #j를 바로 왼쪽 위치로 저장
                            #리스트의 j번 위치에 있는 값과 key를 비교해서 key가 삽입될 적절한 위치를 찾음
        while j >= 0 and k[j] > key:
            k[j+1] = k[j]   #삽입될 공간이 생기도록 값을 오른쪽으로 한칸 이동
            j -= 1

        k[j+1] = key        #찾은 위치에 key를 저장
        #print(f'k={k}')    #정렬되는 과정 보기
    return k

data = [2, 4, 5, 1, 3]
result = insertion3(data)
print(result)

