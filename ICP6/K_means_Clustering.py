# importing the required packages
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
# read the data from pandas
data = pd.read_csv("sample_stocks.csv")
X = data.iloc[:,0]
y = data.iloc[:,1]
# Make a 2D array to give input to kmeans
X = np.vstack((X,y)).T
sse={}
for k in range(1,11):
    # use the KMeans
    kmeans = KMeans(n_clusters=k)
    # fit the model to the array X
    kmeans.fit(X)
    # Scatter plot the datapoints with different colors assigned to various clusters
    plt.scatter(X[:, 0], X[:, 1], c=kmeans.labels_, cmap='rainbow')
    # Scatter plot the centroids with black color
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], color='black')
    # show the plot using matplotlib package
    plt.show()
    # calculate the sum of squares for every cluster using the kmeans.inertia_
    sse[k] = kmeans.inertia_  #

# plot to choose the best k by using sum of squares b/w each member of cluster and its centroid.
print(sse)
# plot the sse and k values using matplotlib
plt.plot(sse.keys(), sse.values())

