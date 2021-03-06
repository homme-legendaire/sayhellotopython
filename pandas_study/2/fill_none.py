import pandas as pd
school_id_list = [{'name': 'John', 'job': "teacher", 'age': 40},
                  {'name': 'Nate', 'job': "teacher", 'age': 35},
                  {'name': 'Yuna', 'job': "teacher", 'age': 37},
                  {'name': 'Abraham', 'job': "student", 'age': 10},
                  {'name': 'Brian', 'job': "student", 'age': 12},
                  {'name': 'Janny', 'job': "student", 'age': 11},
                  {'name': 'Nate', 'job': "teacher", 'age': None},
                  {'name': 'John', 'job': "student", 'age': None}
                  ]
df = pd.DataFrame(school_id_list, columns=['name', 'job', 'age'])
print(df)
print(df.info())
df.age = df.age.fillna(0)
print(df)
school_id_list = [{'name': 'John', 'job': "teacher", 'age': 40},
                  {'name': 'Nate', 'job': "teacher", 'age': 35},
                  {'name': 'Yuna', 'job': "teacher", 'age': 37},
                  {'name': 'Abraham', 'job': "student", 'age': 10},
                  {'name': 'Brian', 'job': "student", 'age': 12},
                  {'name': 'Janny', 'job': "student", 'age': 11},
                  {'name': 'Nate', 'job': "teacher", 'age': None},
                  {'name': 'John', 'job': "student", 'age': None}
                  ]
df = pd.DataFrame(school_id_list, columns=['name', 'job', 'age'])
df['age'].fillna(df.groupby('job')['age'].transform('median'), inplace=True)
print(df)
