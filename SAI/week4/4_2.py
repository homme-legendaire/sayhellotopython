import pandas as pd
# ㄱ 전체 행렬을 말하는거? X
# ㄴ O
# ㄷ X
# ㄹ O
# ㅁ X
friend_dict_list = [
    {'name': 'Bruce', 'age': 25, 'job': 'student'},
    {'name': 'Rachel', 'age': 30, 'job': 'actress'},
    {'name': 'Jenny', 'age': 30, 'job': 'teacher'},
]
df = pd.DataFrame(friend_dict_list)
print(df)
df2 = pd.DataFrame([
    {'salary': 8},
    {'salary': 22},
])
print(df2)
print(pd.concat([df, df2], axis=1, ignore_index=True))
