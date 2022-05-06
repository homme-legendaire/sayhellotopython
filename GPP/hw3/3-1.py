N = int(input())
sejong = 0
daeyang = 0
for i in range(N):
    sejong += int(input())
    daeyang += int(input())
if sejong > daeyang:
    print("Winner : Sejong")
elif daeyang > sejong:
    print("Winner : Daeyang")
else:
    print("Draw!")
