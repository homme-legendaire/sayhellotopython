#3.2
#sum = 0
#count = 1
#while count <= 1000:
#    if (count%3==0):
#        sum+=count
#    count+=1
#print(sum)

#3.3
#i = 1
#j=1
#while i <= 5:
#    while j <= i:
#        print("*"*j)
#        j+=1
#    i+=1

#i = 0
#while True:
#    i += 1
#    if i > 5: break
#    print('*' * i)

#3.4
#for i in range(1,101):
#    print(i)

#3.5
#a = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
#sum=0
#for i in a:
#    sum+=i
#print(sum/len(a))

#3.6
numbers = [1,2,3,4,5]
result = [num*2 for num in numbers if num%2==1]
print(result)