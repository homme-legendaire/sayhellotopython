N = int(input())
M = int(input())
if M == 0:
    for i in range(N):
        print('*'*(i+1)+' '*(N-i-1))
if M == 1:
    for i in range(N):
        print(' '*(N-i-1)+'*'*(i+1))
