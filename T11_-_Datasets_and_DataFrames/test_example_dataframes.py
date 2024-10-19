
import numpy as np
import pandas as pd
import ssl

# Disable SSL certificate verification
ssl._create_default_https_context = ssl._create_unverified_context

#Fetch iris data from Github
url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv'
df = pd.read_csv(url)

#Loading iris data from sci-kit learn, 
#Also uncomment the line above, from sklearn import datasets
#iris = datasets.load_iris()
#df = pd.DataFrame(iris.data, columns=iris.feature_names)

#If you download the csv file 
# file_name = 'iris.csv'
# df = pd.read_csv(file_name)

# print(df.head())
# print(df.tail())
# print(df.shape)
# print(df.info())
# print(df.describe())

# #Selecting columns
# print(df.columns)

# #Using specific columns
# df_selected = df[['species','petal_length','petal_width']]

# print(df['species'])
# #Filtering rows by flower species
# df_setosa = df[df['species']=='setosa']

#Create new colum
# df['petal_area (cm^2)'] = df['petal_length'] * df['petal_width']
# print(df.head())

# #Renaming/dropping columns
# df = df.rename(columns={'petal_area (cm^2)' : 'petal_ar (cm^2)'})
# print(df.head())

# #Statistics
# print(df['petal_ar (cm^2)'].mean())
# print(df['species'].nunique()) #nunique = tells you number of unique sepcies

# #Grouping and finding SD for all 3 species
# print(df.groupby('species')['petal_length'].std())

#Aggregating
print(df.groupby('species').agg(mean_petal_length=('petal_length','mean'), 
                                max_sepal_length=('sepal_length','max')))