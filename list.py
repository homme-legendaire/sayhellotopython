a=[1,2,3]

print(a)
print(a[0]+a[2])

a=[1,2,3,['a','b','c']]
print(a)
print(a[3])
print(a[-1][1])

a=[1,2,3,4,5]
print(a[0:2])

a=[1,2,3,['a','b','c'],4,5]
print(a[2:5])
print(a[3][:2])

a=[1,2,3]
b=[4,5,6]
print(a+b)
print(len(a))

a[2]=4
print(a)

del a[1]
print(a)

a=[1,2,3]
a.append(4)
print(a)
a.append([5,6])
print(a)

a=[1,5,2,4,3]
a.sort()
print(a)
a.reverse()
print(a)

a=[1,2,3]
print(a.index(3))
print(a.index(1))

a= [1,2,3]
a.insert(0,4)
print(a)

a=[1,2,3,1,2,3]
a.remove(3)
print(a)

a=[1,2,3]
print(a.pop())
print(a)

a=[1,2,3,1]
print(a.count(1))

a=[1,2,3]
a.extend([4,5])
print(a)
a.append([6,7])
print(a)
