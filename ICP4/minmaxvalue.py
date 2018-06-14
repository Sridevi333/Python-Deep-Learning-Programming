#Create a 10x10 array with random values and find the minimum and maximum values in each row
# importing the numpy package

import numpy as np
#generating 100 random numbers
ar=np.random.random((10,10))
#finding maximum and minimum values
maxi=ar.max()
print(maxi)
mini=ar.min()
print(mini)