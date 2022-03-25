import pandas as pd
report = {
    'math': [90],
    'science': [100],
    'english': [95],
    'computer': [98],
    'korean': [100],
}
df = pd.DataFrame(report)
df['spanish'] = [70]
print(df)
list = []
edit_report = []
for i in df.values:
    for j in i:
        if j != 100:
            j = 100
        else:
            j = 'perfect'
        list.append(j)
edit_report.append(list)
column_name = ['math', 'science', 'english', 'computer', 'korean', 'spanish']
df2 = pd.DataFrame.from_records(edit_report, columns=column_name)
df3 = pd.DataFrame([['오늘', '저녁은', '치', '킨', '이다', '야호!']], columns=column_name)
print(pd.concat([df2, df3], ignore_index=True))
