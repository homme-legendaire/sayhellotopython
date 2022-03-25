import pandas as pd
df = pd.read_excel('reception.xlsx')
dino = df[(df.class_n <= 18) & (df.council == 'X')]
fossil = dino.values
fossil = fossil.tolist()
clear = df[(df.class_n > 18) | (df.council == 'O')]
clear.reset_index(drop=True, inplace=False)
df.to_excel('Renew_reception.xlsx')
