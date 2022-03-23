import pandas as pd
friend_dict_list = [
    {'name': 'Bruce', 'age': 25, 'job': 'student'},
    {'name': 'Rachel', 'age': 30, 'job': 'actress'},
    {'name': 'Jenny', 'age': 30, 'job': None},
]
df = pd.DataFrame(friend_dict_list)
print(df)

print(df[1:3])  # 1,2 인덱스 가져오기
print(df.loc[[0, 2]])  # 원하는 인덱스 가져오기
print(df[df.age > 25])  # 조건 충족하는 원소만
print(df.query('age>25'))
print(df[(df.age > 25) & (df.name == 'Jenny')])

friend_list = [
    ['Kevin', 25, 'teacher'],
    ['Megan', 30, 'actress'],
    ['Jason', 24, 'student']
]
df = pd.DataFrame.from_records(friend_list)
print(df)

print(df.iloc[:, :2])  # row/column 인덱싱 해서 자르기

df = pd.read_csv('./data/friend_list_no_head.csv',
                 header=None, names=['name', 'age', 'job'])
print(df)
df_filtered = df[['name', 'age']]  # 열 이름으로 필터링
print(df_filtered)
print(df.filter(items=['age', 'job']))
print(df.filter(regex='b$', axis=1))  # 이름이 b로 끝나는 열
