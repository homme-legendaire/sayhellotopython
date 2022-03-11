import numpy as np

data = np.genfromtxt('wine.random.csv' , skip_header = 1 , delimiter = ',' , dtype = float)
ph = data[401:500,8]
alcohol = data[401:500,10]
result = data[401:500,12]
print(ph)
print(alcohol)
print(result)