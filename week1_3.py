import random

marble = random.randrange(1,100)
i = 0
print(f"정답:{marble}")
while i < 6:
    a = int(input())
    if (a < marble):
        if (i == 5):
            print("우리 깐부사이는 아니잖아~ 탕탕")
            break
        print("UP")
    elif (a > marble):
        if (i == 5):
            print("우리 깐부사이는 아니잖아~ 탕탕")
            break
        print("DOWN")
    else:
        print("네가..뭐라고 했더라..?")
        break
    i+=1