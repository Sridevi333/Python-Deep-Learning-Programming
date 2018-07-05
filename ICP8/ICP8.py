# import TensorFlow library
import tensorflow as tf

# constant matrix inputs a, b, c
A = tf.constant([1,5,3,2],shape=[2,2])
B = tf.constant([1,7,4,2],shape=[2,2])
C = tf.constant([3,4,5,9],shape=[2,2])
# function (a^2+b)*c and a, b, and c should be the matrices
# calculating (a^2+b)*c
d = tf.pow(a, 2, name='d')
e = tf.add(d,b,name='e')
f = tf.matmul(e,c,name='output')

# printing the input matrices
with tf.Session() as session:
    print("Matrix a: ")
    print(session.run(a))
    print("Matrix b: ")
    print(session.run(b))
    print("Matrix c: ")
    print(session.run(c))

# printing the output
with tf.Session() as session:
    print("Output Matrix: ")
    print(session.run(f))



