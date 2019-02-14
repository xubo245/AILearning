import tensorflow as tf
import numpy as np
from PIL import Image

def test_write_to_tfrecords(tfrecords_filename):
    # tfrecords_filename = './train.tfrecords'
    writer = tf.python_io.TFRecordWriter(tfrecords_filename)  # 创建.tfrecord文件，准备写入

    for i in range(100):
        img_raw = np.random.random_integers(0, 255, size=(7, 30))  # 创建7*30，取值在0-255之间随机数组
        print(img_raw, i)
        # print(img_raw.shape[0])
        # print(img_raw.shape[1])
        img_raw = img_raw.tostring()
        # print(img_raw.shape[0])
        # print(len(img_raw))
        example = tf.train.Example(features=tf.train.Features(
            feature={
                'label': tf.train.Feature(int64_list=tf.train.Int64List(value=[i])),
                'img_raw': tf.train.Feature(bytes_list=tf.train.BytesList(value=[img_raw]))
            }))
        writer.write(example.SerializeToString())

    writer.close()

if __name__ =='__main__':
    tfrecords_filename = "../data/output/tfrecord/train.tfrecords"
    test_write_to_tfrecords(tfrecords_filename)
    filename_queue = tf.train.string_input_producer([tfrecords_filename], )  # 读入流中
    reader = tf.TFRecordReader()
    _, serialized_example = reader.read(filename_queue)  # 返回文件名和文件
    features = tf.parse_single_example(serialized_example,
                                       features={
                                           'label': tf.FixedLenFeature([], tf.int64),
                                           'img_raw': tf.FixedLenFeature([], tf.string),
                                       })  # 取出包含image和label的feature对象
    image = tf.decode_raw(features['img_raw'], tf.int64)
    print(image)
    image = tf.reshape(image, [7, 30])
    print(image)
    print(image.shape[0])
    print(image.shape[1])
    label = tf.cast(features['label'], tf.int64)
    with tf.Session() as sess:  # 开始一个会话
        init_op = tf.initialize_all_variables()
        sess.run(init_op)
        coord = tf.train.Coordinator()
        threads = tf.train.start_queue_runners(coord=coord)
        for i in range(20):
            example, l = sess.run([image, label])  # 在会话中取出image和label
            img = Image.fromarray(example, 'RGB')  # 这里Image是之前提到的
            img.save('../data/output/tfrecord/' + str(i) + '_''Label_' + str(l) + '.jpg')  # 存下图片
            print("\nread:")
            print(example, l)

        coord.request_stop()
        coord.join(threads)

#refer
#https://blog.csdn.net/happyhorizion/article/details/77894055
#https://blog.csdn.net/qq_30159015/article/details/80070514