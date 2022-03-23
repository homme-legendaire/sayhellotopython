import pandas as pd
friend_dict_list = [  # 더미데이터(딕셔너리)
    {'name': 'John', 'age': 25, 'job': 'student'},
    {'name': 'Rachel', 'age': 30, 'job': 'actress'}
]
df = pd.DataFrame(friend_dict_list)  # 데이터프레임 만들기
print(df.head())
df = df[['name', 'age', 'job']]  # 열 순서 바꼈을경우 고정시키기

friend_list = [  # 더미데이터(리스트)
    ['John', 25, 'student'],
    ['Rachel', 30, 'actress']
]
column_name = ['name', 'age', 'job']
df = pd.DataFrame.from_records(friend_list, columns=column_name)
print(df.head())
