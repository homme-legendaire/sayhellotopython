def merge_sort(a):
    # 종료조건 : 정렬할 리스트의 자료 개수가 한 개 이하이면 정렬 할 필요 없음
    n = len(a)

    if n <= 1:
        return a

    #그룹을 나누어 각각 병합 정렬을 호출하는 과정
    mid = n // 2                #중간을 기준으로 두 그룹으로 나눔
    g1 = merge_sort(a[:mid])    #재귀 호출을 사용하여 첫번째 그룹 정렬
    g2 = merge_sort(a[mid:])    #재귀 호출을 사용하여 두번째 그룹 정렬

    result = []                 #최종 정렬된 결과가 저장될 배열 result

    while g1 and g2:            #두 그룹에 정렬할 자료가 남아있는 동안
        if g1[0] < g2[0]:       #두 그룹의 맨 앞 자료 값을 비교
            result.append(g1.pop(0))    #g1값이 작으면 결과리스트에 추가
        else:
            result.append(g2.pop(0))    #g2값이 작으면 결과리스트에 추가

    #아직 남아있는 자료들을 결과에 추가 / g1, g2중 비어있다면 실행하지 않고 지나감
    while g1:
        result.append(g1.pop(0))

    while g2:
        result.append(g2.pop(0))

    #정렬된 리스트 반환
    return result

data = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]

print(merge_sort(data))
