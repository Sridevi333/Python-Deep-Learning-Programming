import numpy as np # imported the numpy library
import matplotlib.pyplot as plt  # imported the matplotlib libraray
x=np.array([0,1,2,3,4,5,6,7,8,9])  # logic for plotting the regerssion model using numpy .
y=np.array([1,3,2,5,7,8,8,9,10,12])
meanx=np.mean(x)
meany=np.mean(y)
num=np.sum((x-meanx)*(y-meany))
den=np.sum(pow((x-meanx),2))
# Calculating slope
slope=num/den
# Calculating intercept
intercept=meany-(slope*meanx)
print("slope",slope)
print("intercept",intercept)
#Equation for linear regression
val=(slope*x)+intercept
plt.plot(x,y)
plt.plot(x,val)
plt.show()