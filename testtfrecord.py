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


    tf.reset_default_graph()
    for filename in filenames:
        with tf.Session() as sess:

            image_data = tf.gfile.FastGFile(filename, "rb").read()
            image_data_decode = tf.image.decode_jpeg(image_data)
            image = image_data_decode.eval()
            image = tf.image.convert_image_dtype(image,dtype=tf.float32)
            image_resize = tf.image.resize_images(image,[height_new,weight_new],0)
            image_new = tf.image.convert_image_dtype(image_resize,dtype=tf.uint8)
            image_new = tf.image.encode_jpeg(image_new)
            filename_resize = filename.split("\\")
            filename_resize = os.path.join(filename_resize[2],filename_resize[3])
            #print(filename_resize)
            image_file = tf.gfile.FastGFile(os.path.join(output_path,filename_resize),"w")
            image_file.write(sess.run(image_new))
            image_file.close()
        tf.get_default_graph().finalize()
        #print(filename_resize)
        #ops = tf.get_default_graph().get_operations()
        #print(len(ops))
        # h, w, c = image.shape
        # assert c==1
        # image = image.reshape(h,w)


