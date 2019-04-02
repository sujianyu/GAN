import tensorflow as tf
import matplotlib.pyplot as plt
import os
data_dir = "data"
data_set = "hanzi"
weight_new = 255
height_new = 255

output_path = os.path.join(data_dir,data_set + "_resize")
if not tf.gfile.Exists(output_path):
    tf.gfile.MakeDirs(output_path)

directors = []
image_path = os.path.join(data_dir,data_set)
for dir in os.listdir(image_path):

    #在新文件夹中创建标签目录
    dir_new = os.path.join(output_path,dir)
    if not tf.gfile.Exists(dir_new):
        tf.gfile.MakeDirs(dir_new)
    path = os.path.join(image_path,dir)
    if os.path.isdir(path):
        directors.append(path)


filenames = []
for dir in directors:
    for filename in os.listdir(dir):
        path = os.path.join(dir,filename)
        if os.path.isfile(path):
            filenames.append(path)
print(filenames)

with tf.Session() as sess:

    for filename in filenames:

        image_data = tf.gfile.FastGFile(filename, "rb").read()
        image_data_decode = tf.image.decode_jpeg(image_data)
        image = sess.run(image_data_decode)
        h, w, c = image.shape
        assert c==1
        image = image.reshape(h,w)


