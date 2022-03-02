#4.1
#def is_odd(a):
#    print(a%2!=0)
#is_odd(5)

#4.2
#def average(*num):
#    sum = 0
#    for i in num:
#        sum+=i
#    return sum / len(num)
#print(average(1,2,3,4,5))

#4.3
#input1 = int(input("첫번째 숫자를 입력하세요:"))
#input2 = int(input("두번째 숫자를 입력하세요:"))
#total = input1 + input2
#print("두 수의 합은 %s 입니다" % total)

#4.4
#3

#4.5
#f1 = open("test.txt", 'w')
#f1.write("Life is too short")
#f1.close()

#f2 = open("test.txt", 'r')
#print(f2.read())
#f2.close()

#with open("test.txt", 'w') as f1:
#    f1.write("Life is too short! ")
#with open("test.txt", 'r') as f2:
#    print(f2.read())

#4.6
#a=input()
#f1 = open("text.txt",'a')
#f1.write(a)
#f1.write("\n")
#f1.close()

#4.7
f = open("text.txt", "r")
body = f.read()
f.close()

body=body.replace("java", "python")

f = open("text.txt","w")
f.write(body)
f.close()