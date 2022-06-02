year = int(input())
month = int(input())
end_month = int(input())
start_day = int(input())
end_day = int(input())

for i in range(month, end_month+1):
    if i % 2 == 0:
        for j in range(start_day, end_day+1):
            if j > 30:
                break
            str1 = str(year).zfill(2)+str(i).zfill(2)+str(j).zfill(2)
            print(str1, end=' ')
            if j == i:
                print('Lucky Day!', end='')
            print()
    if i % 2 != 0:
        for j in range(start_day, end_day+1):
            if j > 31:
                break
            str1 = str(year).zfill(2)+str(i).zfill(2)+str(j).zfill(2)
            print(str1, end=' ')
            if j == i:
                print('Lucky Day!', end='')
            print()
