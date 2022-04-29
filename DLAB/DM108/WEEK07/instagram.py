import random


class Instakilogram:
    secret = "교촘치킨 와사비맛 치킨 출시예정"

    def __init__(self, name):
        self.name = name

    def giveCoupon(self, n1, n2):
        num = random.randint(n1, n2)
        print(f"{self.name}님 치킨할인 쿠폰 {num}개 발급")


'''
alice = Instakilogram()

print(alice.secret)
alice.setName('Alice')
alice.giveCoupon(1, 5)

bob = Instakilogram()
bob.giveCoupon()
'''

alice = Instakilogram("Alice")
alice.giveCoupon(100, 200)
