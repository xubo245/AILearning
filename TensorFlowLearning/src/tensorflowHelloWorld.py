import tensorflow as tf

tf.enable_eager_execution()
print(tf.add(1, 2))
print(tf.add(12, 23))
hello = tf.constant('Hello, TensorFlow!')
print(hello.numpy())


