def quick_sort(a):
    n = len(a)
    if n <= 1:  # 종료조건 - 정렬해야 하는 배열의 자료 수가 한 개 이하이면 정렬할 필요 없음
        return a

# 기준 값을 정하고 기준에 맞춰 그룹을 나누는 과정
    pivot = a[-1]  # 변수 pivot을 기준으로 하고, 편의상 배열의 마지막 값을 기준으로 설정
    g1 = []  # 기준보다 작은 값을 담을 리스트 g1
    g2 = []  # 기준보다 큰 값을 담을 리스트 g2

    for i in range(0, n-1):  # 배열의 마지막 값은 기준값이므로 제외
        if a[i] < pivot:  # 기준값과 비교하여
            g1.append(a[i])  # 작으면 g1에 추가
        else:  # 크면 g2에 추가
            g2.append(a[i])

# 각 그룹에 대해 재귀 호출로 퀵 정렬 한 후, 기준값과 합쳐 하나의 리스트로 결과 반환
    return quick_sort(g1) + [pivot] + quick_sort(g2)


print(quick_sort([3, 5, 4, 6, 1, 2]))
