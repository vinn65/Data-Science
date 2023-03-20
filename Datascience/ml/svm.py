import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

df = pd.read_csv("User_data.csv")


x = df[['Age','Estimated salary']]
y = df['Purchased']

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,train_size=0.8)


clf = SVC(kernel='linear')
clf.fit(x_train,y_train)

y_pred = clf.predict(x_test)

# print(y_pred)

accuracy_score(y_test,y_pred)
# print(accuracy_score)
