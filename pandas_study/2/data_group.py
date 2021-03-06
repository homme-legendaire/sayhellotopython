import pandas as pd
student_list = [{'name': 'John', 'major': "Computer Science", 'sex': "male"},
                {'name': 'Nate', 'major': "Computer Science", 'sex': "male"},
                {'name': 'Abraham', 'major': "Physics", 'sex': "male"},
                {'name': 'Brian', 'major': "Psychology", 'sex': "male"},
                {'name': 'Janny', 'major': "Economics", 'sex': "female"},
                {'name': 'Yuna', 'major': "Economics", 'sex': "female"},
                {'name': 'Jeniffer', 'major': "Computer Science", 'sex': "female"},
                {'name': 'Edward', 'major': "Computer Science", 'sex': "male"},
                {'name': 'Zara', 'major': "Psychology", 'sex': "female"},
                {'name': 'Wendy', 'major': "Economics", 'sex': "female"},
                {'name': 'Sera', 'major': "Psychology", 'sex': "female"}
                ]
df = pd.DataFrame(student_list, columns=['name', 'major', 'sex'])
print(df)
groupby_major = df.groupby('major')
print(groupby_major.groups)
for name, group in groupby_major:
    print(name + " : " + str(len(group)))
    print(group)
df_major_cnt = pd.DataFrame({'count': groupby_major.size()}).reset_index()
print(df_major_cnt)
