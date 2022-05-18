
#리스트 a에서 어디 부터(start) 어디 까지(end) 정렬 대상인지 범위를 지정하여 정렬하는 재귀호출 함수
def quick_sort_sub(a, start, end):
    if end - start <= 0:                #종료조건 - 정렬 대상의 크기가 1개 이하면 정렬할 필요가 없음
        return

#기준 값을 정하고 그 값에 맞춰 리스트 안에서 각 자료의 위치를 바꾼다.
    pivot = a[end]                      #리스트의 맨 마지막 값을 기준값으로 설정
    i = start
    for j in range(start, end):
        if a[j] <= pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i], a[end] = a[end], a[i]

#재귀 호출
    quick_sort_sub(a, start, i-1)       #기준값보다 작은 그룹을 재귀 호출로 다시 정렬
    quick_sort_sub(a, i+1, end)         #기준값보다 큰 그룹을 재귀 호출로 다시 정렬

#전체 리스트(0 ~ len(a-1) 대상으로 재귀함수 호출
def quick_sort(a):
    quick_sort_sub(a, 0, len(a)-1)





