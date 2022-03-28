import pandas as pd
job_list = [{'name': 'John', 'job': "teacher"},
            {'name': 'Nate', 'job': "teacher"},
            {'name': 'Fred', 'job': "teacher"},
            {'name': 'Abraham', 'job': "student"},
            {'name': 'Brian', 'job': "student"},
            {'name': 'Janny', 'job': "developer"},
            {'name': 'Nate', 'job': "teacher"},
            {'name': 'Obrian', 'job': "dentist"},
            {'name': 'Yuna', 'job': "teacher"},
            {'name': 'Rob', 'job': "lawyer"},
            {'name': 'Brian', 'job': "student"},
            {'name': 'Matt', 'job': "student"},
            {'name': 'Wendy', 'job': "banker"},
            {'name': 'Edward', 'job': "teacher"},
            {'name': 'Ian', 'job': "teacher"},
            {'name': 'Chris', 'job': "banker"},
            {'name': 'Philip', 'job': "lawyer"},
            {'name': 'Janny', 'job': "basketball player"},
            {'name': 'Gwen', 'job': "teacher"},
            {'name': 'Jessy', 'job': "student"}
            ]
df = pd.DataFrame(job_list, columns=['name', 'job'])
print(df)
print(df.job.unique())
print(df.job.value_counts())
