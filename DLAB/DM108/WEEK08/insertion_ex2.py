#리스트 x에서 y가 들어가야 할 위치를 돌려주는 함수
def findInsIdx(x, y):
    for i in range(0, len(x)):  #이미 정렬된 리스트 x의 자료를 앞에서부터 차례로 확인하여
        if y < x[i]:    #y값 보다 i번 위치에 있는 자료가 크면
            return i    #y가 그 값 바로 앞에 놓여야 정렬 순서가 유지됨
    return len(x)       #적절한 위치를 찾지 못하면, y가 x의 모든 자료보다 크다는 뜻이므로 맨 뒤에 삽입

def insertion2(k):
    result = []         #새로운 리스트를 만들어 정렬된 값을 저장
    while k:            #기존 리스트에 값이 남아 있는 동안 반복
        value = k.pop(0)    #기존 리스트에서 한 개를 꺼냄
        ins_idx = findInsIdx(result, value)     #꺼낸 값이 들어갈 적당한 위치 찾기
        result.insert(ins_idx, value)           #찾은 위치에 값 삽입(이후 값은 한 칸씩 밀려남)
        print(f'k={k}, result={result}')        #단계별로 삽입정렬되는 내용을 확인
    return result

data = [2, 4, 5, 1, 3]
print(insertion2(data))

