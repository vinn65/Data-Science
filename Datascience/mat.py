import matplotlib.pyplot as plt
import numpy as np

x = np.array([0,6])
y = np.array([0,80])

plt.plot(x,y)
plt.show()

#different types of plot
#1.line chart
points = np.array([4,7,2,10,13])
plt.plot(points) #/.show, linestyle ="dotted/dashed"

#2. Bar chart
x = np.array(["x","y","z","w"])
y = np.array([23,56,67,45,3])
plt.show()

#3. scatter
x1 = np.array([20,25,11,4,6,9])
y1 = np.array([2,7,15,8,10,12])
plt.scatter(x1,y1)
plt.show()

#4. pie
# p = np.array([30,20,40,10])
# plt.pie(p)
# plt.show(p)

#5.HIstogram

h1 = np.random.normal(170,10,250)
plt.hist(h1)
