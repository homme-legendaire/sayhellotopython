import numpy as np
import pandas as pd
friend_dict_list = [
    {'name': 'Bruce', 'age': 25, 'job': 'student'},
    {'name': 'Rachel', 'age': 30, 'job': 'actress'},
    {'name': 'Jenny', 'age': 30, 'job': 'teacher'},
]
df = pd.DataFrame(friend_dict_list)
print(df)
df['salary'] = 0  # salary 열 추가
print(df)
df['salary'] = np.where(df['job'] != 'student', 'yes',
                        'no')  # salary 값 yes/no 삽입
print(df)

friend_dict_list = [
    {'name': 'Bruce', 'midterm': 85, 'final': 95},
    {'name': 'Rachel', 'midterm': 90, 'final': 85},
    {'name': 'Jenny', 'midterm': 95, 'final': 90},
]
df = pd.DataFrame(friend_dict_list)
print(df)
df['total'] = df['midterm']+df['final']  # total 열 추가
print(df)
df['average'] = df['total']/2  # avg 열 추가
print(df)

grades = []  # grade 열 추가 with 리스트
for row in df['average']:
    if row >= 90:
        grades.append('A')
    elif row >= 80:
        grades.append('B')
    else:
        grades.append('F')
df['grade'] = grades
print(df)


def pass_fail(row):
    if row != 'F':
        return 'Pass'
    else:
        return 'Fail'


df.grade = df.grade.apply(pass_fail)  # 값 바꿔주기
print(df)

date_list = [{'yyyy-mm-dd': '2000-06-27'},
             {'yyyy-mm-dd': '2002-09-24'},
             {'yyyy-mm-dd': '2005-12-20'}]
df = pd.DataFrame(date_list, columns=['yyyy-mm-dd'])


def extract_year(row):
    return row.split('-')[0]


df['year'] = df['yyyy-mm-dd'].apply(extract_year)
print(df)

friend_dict_list = [
    {'name': 'Bruce', 'midterm': 85, 'final': 95},
    {'name': 'Rachel', 'midterm': 90, 'final': 85},
    {'name': 'Jenny', 'midterm': 95, 'final': 90},
]
df = pd.DataFrame(friend_dict_list)
print(df)
df2 = pd.DataFrame([['Ben', 50, 50]], columns=[
                   'name', 'midterm', 'final'])  # 행 추가
print(df2)
print(df.append(df2, ignore_index=True))
