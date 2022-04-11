# 연습문제 4-3

n = int(input())  # 일한 날 수
S, day, gold = 0, 0, 0

while day < n:
    gold += 1
    day += gold
    S += gold*gold

S -= (day-n)*gold
print(S)
