import numpy as np
import pandas as pd
date_list = [{'date': '2000-06-27'},
             {'date': '2002-09-24'},
             {'date': '2005-12-20'}]
df = pd.DataFrame(date_list, columns=['date'])
print(df)


def extract_year(date):
    return date.split('-')[0]


def integer_to_string(age):
    return str(age)


df['year'] = df['date'].map(extract_year)
print(df)

job_list = [{'age': 20, 'job': 'student'},
            {'age': 30, 'job': 'developer'},
            {'age': 30, 'job': 'teacher'}]
df = pd.DataFrame(job_list)
print(df)
df.job = df.job.map({'student': 1, 'developer': 2, 'teacher': 3})
print(df)
df.age = df.age.map(integer_to_string)
print(type(df.age[0]))

x_y = [{'x': 5.5, 'y': -5.6},
       {'x': -5.2, 'y': 5.5},
       {'x': -1.6, 'y': -4.5}]
df = pd.DataFrame(x_y)
print(df)

df = df.applymap(np.around)
print(df)
