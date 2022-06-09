N = int(input())
sejong = 0
daeyang = 0
for _ in range(N):
    sejong += int(input())
    daeyang += int(input())
if sejong > daeyang:
    print('Winner : Sejong')
elif sejong == daeyang:
    print('Draw!')
else:
    print('Winner : Daeyang')
