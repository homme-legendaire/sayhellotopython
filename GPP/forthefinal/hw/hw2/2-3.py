YYMMDD = input()
year = int(YYMMDD[:2])
month = int(YYMMDD[2:4])
day = int(YYMMDD[4:])
thir = [4, 6, 9, 11]
wrong = 0

if year < 10:
    year += 2000
else:
    year += 1900
if month > 12 or month < 1:
    wrong = 1
if month == 2:
    if day > 29:
        wrong = 1
elif month in thir:
    if day > 30:
        wrong = 1
else:
    if day > 31:
        wrong = 1

if wrong == 1:
    print('Wrong')
else:
    print(f'{year}/{month}/{day}')
