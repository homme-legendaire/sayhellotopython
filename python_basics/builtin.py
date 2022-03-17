print(abs(-3)) # 절댓값

print(all([1,2,3])) # 자료형 참과 거짓 1
print(all([1,2,3,0]))

print(any([1,2,3,0])) # 자료형 참과 거짓 2 (모두 거짓일때만 False)
print(any([0,""]))

print(chr(97)) # 유니코드 => 문자
print(ord('a')) # 문자 => 유니코드

print(dir([1,2,3])) # 객체 내장 변수,함수를 보여줌
print(dir({'1':'a'}))

print(divmod(7,3)) # a를 b로 나눈 몫과 나머지

for i, name in enumerate(['body', 'foo','bar']): # 인덱스 값을 포함하는 enumerate 객체 반환
    print(i,name)

print(eval('1+2')) # 문자열 실행값 출력
print(eval("'hi'+'a'"))
print(eval("divmod(4,3)"))

def positive(x): # 조건에 맞게 걸러줌
    return x>0
print(list(filter(positive, [1,-3,2,0,-5,6])))

print(list(filter(lambda x: x>0, [1,3,-2,0,5,-6])))

print(hex(234)) # 16진수 변환

a =3
print(id(a)) # 고유 주소 값 출력

print(int(3.4)) # 정수 변환
print(int('11',2)) # 2진수
print(int('5A',16)) # 16진수
print(oct(34)) # 8진수

print(list("sooyoung")) # 리스트 생성
print(list((1,2,3,4,5)))
a = [1,2,3]
b = list(a)
print(b)

print(str(3*"hi")) # 문자열 생성
print(tuple("abc")) # 튜플 생성

class Person: pass

a = Person() # 클래스가 만든 인스턴스인지 판별
b = 3
print(isinstance(a,Person))
print(isinstance(b,Person))

print(len('Python')) # 길이 측정

def two_times(x): # 함수, 리스트 => 결괏값
    return x*2
print(list(map(two_times, [1,2,3,4,5])))
print(list(map(lambda a:a*2, [1,2,3,4])))

print(max([1,2,3])) # 최댓값
print(max("young"))

print(min([1,2,3])) # 최솟값
print(min("young"))

print(pow(2,4)) # x의 y제곱

print(list(range(5))) # 0 ~ a미만
print(list(range(5,10))) # a ~ b미만
print(list(range(1,10,2))) # a ~ b미만 c 등차

print(round(4.6)) # 반올림
print(round(5.674,2))

print(sorted([2,3,1])) # 정렬

print(sum([1,3,5])) # 요소 합

print(type(3)) # 자료형 반환

print(list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9]))) # 같은 개수의 자료형 묶어줌
