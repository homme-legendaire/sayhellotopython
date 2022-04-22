import random

def whoWin(x,y):
    if x == '가위':
        if y == '가위':
            msg = '무승부 입니다.'
        elif y == '바위':
            msg = 'computer의 승리입니다.'
        else:
            msg = 'player의 승리입니다.'

    elif x == '바위':
        if y == '가위':
            msg = 'player의 승리입니다.'
        elif y == '바위':
            msg = '무승부 입니다.'
        else:
            msg = 'computer의 승리입니다.'

    else:
        if y == '가위':
            msg = 'computer의 승리입니다.'
        elif y == '바위':
            msg = 'player의 승리 입니다.'
        else:
            msg = '무승부 입니다.'

    return msg

print('='*30)
print('가위 바위 보 게임')
print('='*30)

rps = ['가위', '바위', '보']
again = 'y'

while again == 'y':
    player = random.choice(rps)
    computer = random.choice(rps)

    result = whoWin(player, computer)

    print('player: %s' %player)
    print('computer: %s' %computer)
    print(result)
    print('-'*30)

    again = input('계속하려면 y를 입력하세요: ')
    print()