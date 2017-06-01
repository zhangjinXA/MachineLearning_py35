import numpy as np
import tensorflow as tf

X = tf.placeholder(dtype='float64')
Y = tf.placeholder(dtype='float64')
Z = tf.reduce_all(X)
sess = tf.Session()
sess.run(tf.initialize_all_variables())
Zx = sess.run(Z,feed_dict={X:np.ones([100])})
print(Zx)

print(X)
