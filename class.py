result = 0

def add(num):
    global result
    result += num
    return result
print(add(3))
print(add(4))

class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))

class FourCal:
    def setdata(self,first,second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

a = FourCal()
a.setdata(4,2)

print(a.first)
print(a.second)

a = FourCal()
b = FourCal()
a.setdata(4, 2)
b.setdata(3, 7)

print(a.add())
print(a.mul())
print(a.sub())
print(a.div())
print(b.add())
print(b.mul())
print(b.sub())
print(b.div())

class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setdata(self,first,second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

a = FourCal(4,2)
print(a.first)
print(a.second)

class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

a = MoreFourCal(2,6)
print(a.pow())

class SafeFourCal(MoreFourCal):
    def div(self):
        if (self.second == 0):
            return 0
        else:
            return self.first / self.second

a = SafeFourCal(4,0)
print(a.div())

class Family:
    lastname = "이"
print(Family.lastname)

a = Family()
b = Family()
print(a.lastname)
print(b.lastname)
Family.lastname = "박"
print(a.lastname)
print(b.lastname)
