import pandas as pd

file_name = 'balance.txt'
df = pd.read_csv(file_name)
print(df.info())

df.groupby('Age')
