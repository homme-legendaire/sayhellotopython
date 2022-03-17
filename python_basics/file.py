f = open("새파일.txt", 'w')
for i in range(1,11):
    data = f"{i}번째 줄입니다.\n"
    f.write(data)
f.close()

f = open("D:/github/sayhellotopython/새파일.txt",'r')
line = f.readline()
print(line)
f.close()

f = open("D:/github/sayhellotopython/새파일.txt",'r')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()

f = open("D:/github/sayhellotopython/새파일.txt",'r')
lines = f.readlines()
for line in lines:
    line = line.strip()
    print(line)
f.close()

f = open("D:/github/sayhellotopython/새파일.txt",'r')
line = f.read()
print(line)
f.close()

f = open("D:/github/sayhellotopython/새파일.txt",'a')
for i in range(11, 20):
    data = f"{i}번째 줄입니다.\n"
    f.write(data)
f.close()

with open("D:/github/sayhellotopython/새.txt",'w') as f:
    f.write("Life is too short, you need python")
    