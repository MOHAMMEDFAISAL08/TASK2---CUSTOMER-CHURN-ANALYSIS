import pandas as pd
df=pd.read_csv('data/customer_churn_10000.csv')
print(df.head())
print(df.isnull().sum())
