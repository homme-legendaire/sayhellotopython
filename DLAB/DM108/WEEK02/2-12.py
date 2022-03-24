
x1, x2, x3, x4 = map(int, input().split())
s = x1 + x2 + x3 + x4

y1, y2, y3, y4 = map(int, input().split())
t = y1 + y2 + y3 + y4

if s > t:
    print("하이드:",s)

else:
    print("디콘:",t)

