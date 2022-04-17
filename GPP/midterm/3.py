n = int(input())
n1 = n//100000000
n2 = n//10000000%10
n3 = n//1000000%10
n4 = n//100000%10
n5 = n//10000%10
n6 = n//1000%10
n7 = n//100%10
n8 = n//10%10
n9 = n%10
if n1 > n9:
    n1,n9=n9,n1
if n2 > n8:
    n2,n8=n8,n2
if n3 > n7:
    n3,n7=n7,n3
if n4 > n6:
    n4,n6=n6,n4
print("result =",end=' ')
print(n1,n2,n3,n4,n5,n6,n7,n8,n9, sep='')
