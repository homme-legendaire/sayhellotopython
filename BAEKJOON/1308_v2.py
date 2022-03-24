import datetime
y1, m1, d1 = map(int, input().split())
y2, m2, d2 = map(int, input().split())
begin = datetime.date(y1, m1, d1)  # datetime 라이브러리 사용
end = datetime.date(y2, m2, d2)
camp = end - begin
if (y2 == y1+1000 and m2 >= m1 and d2 >= d1) or y2 > y1+1000:
    print('gg')
else:
    print(f"D-{camp.days}")
