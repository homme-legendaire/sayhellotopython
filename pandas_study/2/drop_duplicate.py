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
                {'name': 'Sera', 'major': "Psychology", 'sex': "female"},
                {'name': 'John', 'major': "Computer Science", 'sex': "male"},
                ]
df = pd.DataFrame(student_list, columns=['name', 'major', 'sex'])
print(df)
print(df.duplicated())
print(df.drop_duplicates(['name']))
print(df.drop_duplicates(['name'], keep='last'))
