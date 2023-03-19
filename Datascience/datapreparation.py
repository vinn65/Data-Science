#Missing data refers to data that is not stored for some variables in a given dataset. missing values represented by NaN
#Reasons for missing data - past data was corrupted due to improper maintanance, - Observations are not recorded for certain fields due to some reasons.
#How to handle missing - Many machine learning algorithms if they fail if the dataset contains missing values. 
#some don`t K-nearest and Naive bayes.

#1. Replace missing value with the mean - for numeric. if there are outliers mean will be bad. Deal with outliers first.
#2. Replace with the mode. - incase of categorical features.
#3. Impute the most frequent value. - use SimpleImputer.


#Nominal Encoding - where order of data does not matter. - techs  - one hot encoding, one hot encoding with many catergories, mean encoding.
#Ordinal encodig - where order of data matters. - techs - label and target guided ordinal encoding.

#one hot encoding 
import pandas as pd
import sklearn
from sklearn.preprocessing import LabelEncoder
df = pd.read_csv("airports.csv")
# print(df.head())
# df.tail()
# print(df.columns)
# print(df['state'].value_counts())

# print(pd.get_dummies(df, columns=['state']))

#label encoding

df1 = pd.read_csv('iris.csv')
# print(df1.head())

le = LabelEncoder()
df1['Species'] = le.fit_transform('Species')
print(df1.head())


