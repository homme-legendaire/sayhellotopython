def palindrome(s):
    # 큐와 스택을 리스트로 정의
    qu = []
    st = []

    # 문자열의 알파벳 문자를 각각 큐와 스택에 넣음
    for x in s:
        if x.isalpha():
            qu.append(x.lower())
            st.append(x.lower())

    # 큐와 스택에 들어있는 문자를 꺼내면서 비교
    while qu:  # 큐에 문자가 남아 있는 동안 반복
        if qu.pop(0) != st.pop():  # 큐와 스택에서 꺼낸 문자가 다르면
            return False  # False를 리턴하여 회문이 아님

    return True


str = input()
print(palindrome(str))
