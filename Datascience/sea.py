import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

#boxplot
df = sns.load_dataset("tips")
df.boxplot(by = 'day', column = ['total_bill'],grid=False) # works in jupyter notebook.
plt.show()      

titanic1 = sns.load_dataset("titanic")
print(titanic1.head())

age1 = titanic1['age'].dropna()
sns.distplot(age1,bins=30,kde=False)
plt.show()

data = sns.load_dataset("mpg")
sns.regplot(x='mpg',y='acceleration',data=data)
plt.show()