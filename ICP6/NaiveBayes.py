# import naivebayes from scikit learn
from sklearn.naive_bayes import GaussianNB
# import datasets for iris ans metrics
from sklearn import datasets, metrics
# import the model selection to split the data using 80/20 rule
from sklearn.model_selection import train_test_split

# Loading the dataset
irisdataset = datasets.load_iris()

# getting the data and labels of the dataset
x = irisdataset.data
y = irisdataset.target
# divide training
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# split the data for training and testing
model = GaussianNB()
# fit the naive bayes model to the data
model.fit(x_train, y_train)
# predict the model on the test data
y_pred = model.predict(x_test)
# print the accuracy score of predicted and actual values
print(metrics.accuracy_score(y_test, y_pred))