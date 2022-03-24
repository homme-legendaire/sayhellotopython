
kor = int(input("국어 점수를 입력하세요: "))
eng = int(input("영어 점수를 입력하세요: "))
math = int(input("수학 점수를 입력하세요: "))

total = kor + eng + math
average = total / 3

print("점수의 총합: %d점, 평균 : %.2f점" %(total, average))

