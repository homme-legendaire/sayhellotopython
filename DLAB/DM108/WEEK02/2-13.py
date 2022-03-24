
#연습문제 2-16

a, b, c = map(int, input().split())

if a == b + c:
    print(a, '=', b, '+', c, sep='')
elif a == b - c:
    print(a, '=', b, '-', c, sep='')
elif a == b * c:
    print(a, '=', b, '*', c, sep='')
elif a == b / c:
    print(a, '=', b, '/', c, sep='')
elif a + b == c:
    print(a, '+', b, '=', c, sep='')
elif a - b == c:
    print(a, '-', b, '=', c, sep='')
elif a * b == c:
    print(a, '*', b, '=', c, sep='')
elif a / b == c:
    print(a, '/', b, '=', c, sep='')
    
