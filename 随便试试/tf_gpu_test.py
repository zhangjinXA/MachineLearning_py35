import tensorflow as tf
import six

a = tf.Variable(100)
b = tf.Variable(200)

c = a + b
sess = tf.InteractiveSession()

sess.run(tf.global_variables_initializer())
print(sess.run(c))