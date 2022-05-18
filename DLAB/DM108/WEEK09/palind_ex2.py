def palindrome(s):
    i = 0           #문자열의 앞에서 비교할 위치
    j = len(s) - 1  #문자열의 뒤에서 비교할 위치

    while i < j:    #중간까지만 검사

        #i위치에 있는 문자가 알파벳 문자가 아니면 뒤로 이동
        if s[i].isalpha() == False:
            i += 1

        #j위치에 있는 문자가 알파밧 문자가 아니면 앞으로 이동
        elif s[j].isalpha() == False:
            j -= 1

        #i와 j위치에 둘다 알파벳 문자가 있으면 두 문자를 비교하고 아니면 회문이 아님
        elif s[i].lower() != s[j].lower():
            return False

        #i와 j위치에 두 문자를 비교하고 같으면 다음 비교 대상으로 넘어간다
        else:
            j += 1
            j -= 1

    return True


