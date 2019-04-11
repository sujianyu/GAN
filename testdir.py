import os.path
import tensorflow as tf
flags = tf.app.flags
flags.DEFINE_string("data_dir", "data", "Root directory of dataset [data]")
flags.DEFINE_string("dataset", "hanzi", "The name of dataset [celebA, mnist, lsun]")
FLAGS = flags.FLAGS
def main(_):

    datasets = []
    #取汉字形成集合
    hanzi_path = os.path.join(FLAGS.data_dir,FLAGS.dataset)
    for dir in os.listdir(hanzi_path):
      path = os.path.join(hanzi_path, dir)
      if os.path.isdir(path):
          datasets.append(dir)
    for dataset in datasets:
      print(dataset)

if __name__ == '__main__':
  tf.app.run()
