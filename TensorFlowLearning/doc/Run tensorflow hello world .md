Run tensorflow hello world 
## Env
	 pycharm idea
	 mac
## Code
	import tensorflow as tf
	
	tf.enable_eager_execution()
	print(tf.add(1, 2))
	print(tf.add(12, 23))
	hello = tf.constant('Hello, TensorFlow!')
	print(hello.numpy())


## history
	
	/usr/local/bin/python3.6 /Users/xubo/Desktop/xubo/git/AILearning/TensorFlowLearning/src/tensorflowHelloWorld.py
	2019-02-14 11:53:19.778397: I tensorflow/core/platform/cpu_feature_guard.cc:141] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
	tf.Tensor(3, shape=(), dtype=int32)
	tf.Tensor(35, shape=(), dtype=int32)
	b'Hello, TensorFlow!'
	
	Process finished with exit code 0
