import pandas as pd, matplotlib.pyplot as plt
df=pd.read_csv('data/customer_churn_10000.csv')
print(df.describe())
df['Churn'].value_counts().plot(kind='bar')
plt.savefig('reports/churn_distribution.png')
