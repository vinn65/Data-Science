#based on supervised learning 
#Assumes similarity between  new case data and available cases and puts the new case into the category.
#Stores all available data and classifiers a new data point based oon the similarity
#It is a non-parametric algo thus does not make any assumptions on underlying data.
#It is a lazy learner. - does not learn from the training set immediately.
#

import numpy as np
import matplotlib.pyplot as mtp
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from matplotlib.colors import ListedColormap

data_set = pd.read_csv("User_Data.csv")

x = data_set.iloc[:,[2,3]].values
y = data_set.iloc[:,4].values

x_train, x_test, y_train, y_test = train_test_split(x, y,test_size=0.2,train_size=0.8,random_state=0)


#feature scaling
st_x = StandardScaler()
x_train = st_x.fit_transform(x_train)
x_test = st_x.transform(x_test)

# print(data_set.head())

classifier = KNeighborsClassifier(n_neighbors=5, metric="minkowski",p=2)
classifier.fit(x_train,y_train)

y_pred  = classifier.predict(x_test)

cm = confusion_matrix(y_test,y_pred)

# print(cm)

x_set, y_set = x_train, y_train

#visualization of training set
x1,x2 = nm.meshgrid(nm)






