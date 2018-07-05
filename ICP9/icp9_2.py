import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import xlrd
from mpl_toolkits.mplot3d import Axes3D

# providing file location
DATA_FILE = 'data/Smoking.xls'

# read in data from the .xls file
book = xlrd.open_workbook(DATA_FILE, encoding_override="utf-8")
sheet = book.sheet_by_index(0)
data = np.asarray([[sheet.row_values(i)[0],sheet.row_values(i)[1],sheet.row_values(i)[3]] for i in range(1, sheet.nrows)])
n_samples = sheet.nrows - 1

# create placeholders for input X (number of fire) and label Y (number of theft)
X1 = tf.placeholder(tf.float32, name='X1')
X2 = tf.placeholder(tf.float32, name='X2')
Y = tf.placeholder(tf.float32, name='Y')

# create weight and bias, initialized to 0
w1 = tf.Variable(0.0, name='weights')
w2 = tf.Variable(0.0, name='weights2')
b = tf.Variable(0.0, name='bias')

# build model to predict Y
Y_predicted = X1 * w1 + X2 * w2 + b

# use the square error as the loss function
loss = tf.square(Y - Y_predicted, name='loss')
# using gradient descent with learning rate of 0.01 to minimize loss
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.0001).minimize(loss)

with tf.Session() as sess:
    # initialize the necessary variables, in this case, w and b
    sess.run(tf.global_variables_initializer())

    writer = tf.summary.FileWriter('./graphs/', sess.graph)

    # train the model
    for i in range(20):  # train the model 50 epochs
        total_loss = 0
        for x, y, z in data:
            # Session runs train_op and fetch values of loss
            _, l = sess.run([optimizer, loss], feed_dict={X1: x,X2: y, Y: z})
            total_loss += l
        print('Epoch {0}: {1}'.format(i, total_loss / n_samples))

    # close the writer when you're done using it
    writer.close()

    # output the values of w and b
    w1,w2, b = sess.run([w1,w2, b])

# plotting the results
X1,X2, Y = data.T[0], data.T[1],data.T[2]
#plt.plot(X1, Y, 'bo', label='Real data')
#plt.plot(X1, X1 * w1 + X2 * w2 + b, 'r', label='Predicted data')
#plt.legend()
#plt.show()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter3D(X1, X2, Y, cmap='Greens')
plt.show()