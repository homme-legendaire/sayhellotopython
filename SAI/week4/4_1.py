import pandas as pd
# ㄱ O
friend_dict_list = [  # 더미데이터(딕셔너리)
    {'name': 'John', 'age': 25, 'job': 'student'},
    {'name': 'Rachel', 'age': 30, 'job': 'actress'}
]
df = pd.DataFrame(friend_dict_list)  # 데이터프레임 만들기
print(df.head())
friend_list = [  # 더미데이터(리스트)
    ['John', 25, 'student'],
    ['Rachel', 30, 'actress']
]
column_name = ['name', 'age', 'job']
df = pd.DataFrame.from_records(friend_list, columns=column_name)
print(df.head())

# ㄴ O
# ㄷ X delimiter='\t' 필요
# ㄹ O
