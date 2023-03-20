import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

data_set = pd.read_csv("salary_data.csv")

# print(data_set.head())
x = data_set.iloc[:,:-1].values,
y = data_set.iloc[:,1].values

# print(x)
# print(y)

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# import numpy as np 
# import pandas as pd
# import matplotlib.pyplot as plt

data_set = pd.read_csv("salary_data.csv")

x = data_set.iloc[:,:-1].values
y = data_set.iloc[:,1].values

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, train_size=0.8)

reg = LinearRegression()

reg.fit(x_train, y_train)

y_pred = reg.predict(x_test)
x_pred = reg.predict(x_train)

plt.scatter(x_test, y_test, color="green")
plt.plot(x_test, y_pred, color='red')
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.title("Salary vs. Years of Experience (Testing Set)")
plt.show()

plt.scatter(x_train, y_train, color="green")
plt.plot(x_train, x_pred, color='red')
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.title("Salary vs. Years of Experience (Training Set)")
plt.show()

