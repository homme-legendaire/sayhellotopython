import pickle
f = open("text.txt","wb")
data = {1:"python", 2:"you need"}
pickle.dump(data,f)
f.close()

import tempfile
filename = tempfile.mkstemp()
print(filename)

import time
print(time.time())
print(time.localtime(time.time()))
print(time.asctime(time.localtime(time.time())))
print(time.ctime())

for i in range(10):
    print(i)
    time.sleep(0.1)

import calendar
print(calendar.calendar(2022))
print(calendar.prmonth(2022, 12))
print(calendar.weekday(2022, 3, 3))
print(calendar.monthrange(2022,2))

import random
print(random.random())
print(random.randint(1,55))
data = [1,2,3,4,5]
random.shuffle(data)
print(data)
