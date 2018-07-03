import tensorflow as tf # imported the tensor flow package
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
# creating a session and 3 matrices
session = tf.Session()
A = tf.constant([1,5,3,2],shape=[2,2])
B = tf.constant([1,7,4,2],shape=[2,2])
C = tf.constant([3,4,5,9],shape=[2,2])
# function (a^2+b)*c and a, b, and c should be the matrices
#Calculating the power of A
D = tf.pow(A,2)
#Adding the result from above with B
E = tf.add(D,B)
#Multiplying the above result with C
F = tf.multiply(E,C)
print(session.run(F))