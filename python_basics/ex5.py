#5.1
#class Calculator:
#    def __init__(self):
#        self.value = 0
#
#    def add(self, val):
#        self.value += val

#class UpgradeCalculator(Calculator):
#    def minus(self,val):
#        self.value -=val

#cal = UpgradeCalculator()
#cal.add(10)
#cal.minus(7)

#print(cal.value)

#5.2
#class Calculator:
#    def __init__(self):
#        self.value = 0

#    def add(self, val):
#        self.value += val

#class MaxLimitCalculator(Calculator):
#    def add(self, val):
#        self.value += val
#        if (self.value >= 100):
#           self.value=100
#cal = MaxLimitCalculator()
#cal.add(50)
#cal.add(60)

#print(cal.value)

#5.3
#False
#True

#5.4
#print(list(filter(lambda a:a>0,[1, -2, 3, -5, 8, -3])))

#5.5
#print(int(0xea))

#5.6
#print(list(map(lambda x:x*3, [1,2,3,4])))

#5.7
#print(max([-8, 2, 7, 5, -3, 5, 0, 1])+min([-8, 2, 7, 5, -3, 5, 0, 1]))

#5.8
#print(round(17/3,4))

###5.9
###5.10
###5.11

#5.12
#import time
#print(time.strftime("%Y/%m/%d %H:%M:%S"))

#5.13
#import random
#result = []
#while (len(result)<6):
#    num = random.randint(1,45)
#    if num not in result:
#        result.append(num)
#print(result)
