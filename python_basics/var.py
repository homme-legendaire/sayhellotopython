from re import A


a=[1,2,3]
print(id(a))

b=a
print(id(b))

a[1]=4
print(a,b)

a=[1,2,3]
b=a[:]
a[1]=4
print(a,b)

from copy import copy
a=[1,2,3]
b=copy(a)
a[0]=5
print(a,b)

a=3
b=5
a,b=b,a
print(a,b)