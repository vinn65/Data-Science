import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
df = pd.read_csv("User_data.csv")

x = df[['Age','Estimatedsalary']]
y = [['Purchased']]

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,train_size=0.8)


clf = DecisionTreeClassifier(criterion='entropy')
clf.fit(x_train,y_train)

y_pred = clf.predict(x_test)

print(accuracy_score(y_test,y_pred))

