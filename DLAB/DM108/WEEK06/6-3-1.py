import random

again = 'y'
count = 1

while again == 'y':
    print('-'*30)
    print('주사위 던지기 %d번째' %count)
    player = random.randint(1,6)
    computer = random.randint(1,6)
    print('사용자: %d' %player)
    print('컴퓨터: %d' %computer)

    if player > computer:
        print("사용자 승리!")
    else:
        print("컴퓨터 승리!")

    count += 1
    again = input("계속하려면 'y'를 입력하세요")
