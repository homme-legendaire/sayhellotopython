import pandas as pd
friend_dict_list = [{'age': 20, 'job': 'student'},
                    {'age': 30, 'job': 'developer'},
                    {'age': 30, 'job': 'teacher'}]
df = pd.DataFrame(friend_dict_list, index=['John', 'Jenny', 'Nate'])
print(df)
print(df.drop(['John', 'Jenny']))  # 이름을 index로 삭제

friend_dict_list = [
    {'name': 'Bruce', 'age': 25, 'job': 'student'},
    {'name': 'Rachel', 'age': 30, 'job': 'actress'},
    {'name': 'Jenny', 'age': 30, 'job': 'teacher'},
]
df = pd.DataFrame(friend_dict_list)
print(df.drop(df.index[[0, 2]]))  # 인덱스로 삭제
print(df[df.age > 20])  # 조건에 맞게 삭제
print(df.drop(['age'], axis=1))  # age 열 삭제
print(df.drop([]))
