import pandas as pd
l1 = [{'name': 'John', 'job': "teacher"},
      {'name': 'Nate', 'job': "student"},
      {'name': 'Fred', 'job': "developer"}]

l2 = [{'name': 'Ed', 'job': "dentist"},
      {'name': 'Jack', 'job': "farmer"},
      {'name': 'Ted', 'job': "designer"}]

df1 = pd.DataFrame(l1, columns=['name', 'job'])
df2 = pd.DataFrame(l2, columns=['name', 'job'])
result = pd.concat([df1, df2], ignore_index=True)
print(result)
result = pd.concat([df1, df2], axis=1, ignore_index=True)
print(result)
