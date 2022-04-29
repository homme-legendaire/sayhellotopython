class Member:
    def __init__(self, info):
        self.name = info['name']
        self.phone = info['phone']
        self.address = info['address']


data = {'name': '김철수', 'phone': '010-1122-3344', 'address': '경기도'}
human = Member(data)
print("이름: ", human.name)
print("전화: ", human.phone)
print("주소: ", human.address)
