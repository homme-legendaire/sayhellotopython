N = int(input())
M = int(input())
if M == 0:
    for i in range(N):
        for j in range(i+1):
            print("*", end='')
        for j in range(N-i-1):
            print(" ", end='')
        print('')
else:
    for i in range(N):
        for j in range(N-i-1):
            print(" ", end='')
        for j in range(i+1):
            print("*", end='')
        print('')
