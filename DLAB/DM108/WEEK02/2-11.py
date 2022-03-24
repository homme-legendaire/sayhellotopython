
#연습문제 2-14

'''
햄버거 한 개의 가격 : k
사려고 하는 햄버거의 개수 : n
현재 가진돈의 금액: m
'''

k, n, m = map(int, input().split())

if k * n > m:
    print(k * n - m)

else:
    print(0)

