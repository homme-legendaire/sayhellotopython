f = open("새파일.txt", 'w')
for i in range(1,11):
    data = f"{i}번째 줄입니다."
    f.write(data)
f.close()