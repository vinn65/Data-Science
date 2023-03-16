#based on supervised learning 
#Assumes similarity between  new case data and available cases and puts the new case into the category.
#Stores all available data and classifiers a new data point based oon the similarity
#It is a non-parametric algo thus does not make any assumptions on underlying data.
#It is a lazy learner. - does not learn from the training set immediately.
#

import numpy as np
import matplotlib.pyplot as mtp
import pandas as pd


data_set = pd.read_csv("User_Data.csv")

x = data_set.iloc[:,[2,3]].values
y = data_set.iloc[:,4].values

