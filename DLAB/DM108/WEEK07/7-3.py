#week7-3

class Member:
    def __init__(self, name, phone, address):
        self.name = name
        self.phone = phone
        self.address = address

obj1 = Member('김철수', '010-1122-3344', '경기도')

print('이름:%s'%obj1.name)
print('전화번호:%s'%obj1.phone)
print('주소:%s'%obj1.address)
