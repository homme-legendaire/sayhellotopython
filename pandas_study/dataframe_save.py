import pandas as pd
friend_dict_list = [
    {'name': 'Bruce', 'age': 25, 'job': 'student'},
    {'name': 'Rachel', 'age': 30, 'job': 'actress'},
    {'name': 'Jenny', 'age': 30, 'job': None},
]
df = pd.DataFrame(friend_dict_list)
print(df.head())
df.to_csv('friends.csv', na_rep="-")  # csv 파일 생성
