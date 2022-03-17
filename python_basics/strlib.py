a = "hobby"
print(a.count('b'))

a = "Python is the best choice"
print(a.find('b'))
print(a.find('k'))
print(a.index('t'))
# print(a.index('k')) 오류

print(",".join("abcd"))  # 문자 사이에 , 삽입

a = "hi"
print(a.upper())  # 대문자로

a = "HELLO"
print(a.lower())  # 소문자로

a = "   hi   "
print(a.lstrip())  # 왼쪽 공백 지우기
print(a.strip())  # 공백 지우기

a = "Life is too short"
print(a.replace("Life", "Your leg"))  # 문자열 바꾸기
print(a. split())  # 문자열 쪼개기
