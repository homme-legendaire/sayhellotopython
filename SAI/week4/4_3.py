from random import randint
import pandas as pd
voter_list = []
for i in range(100):
    a = randint(1, 100)
    if a <= 10:
        voter_list.append([i+1, 'O'])
    else:
        voter_list.append([i+1, ''])
column_name = ['번호', '여부']
df = pd.DataFrame.from_records(voter_list, columns=column_name)
print(df.set_index('번호'))
