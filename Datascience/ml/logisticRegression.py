import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix


df = pd.read_csv("User_Data.csv")

x = df.iloc[:[2,3]].values()
y = df.iloc[:,4].values()


x_train, x_test, y_train, y_test = train_test_split(x,y,train_size=0.2, test_size=0.8)

st_x = StandardScaler()

x_train = st_x.fit_transform(x_train)
x_test = st_x.transform(x_test)

clf = LogisticRegression()

clf.fit(x_train,y_train)

y_pred = clf.predict(x_test)

print(y_pred)

confusion_matrix(y_pred,y_test)

