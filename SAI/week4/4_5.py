import pandas as pd
df = pd.read_excel('reception.xlsx')
dino = df[(df.class_n <= 18) & (df.council == 'X')]
blacklist = dino['name'].values
print("화석 명단")
print(blacklist)
clear = df[(df.class_n > 18) | (df.council == 'O')]
clear = clear.reset_index(drop=True, inplace=False)
clear.to_excel('Renew_reception.xlsx')
