from PIL import Image
import os
import os
import platform

system = platform.system()
if system == "Linux":
    split = "/"
elif system == "Windows":
    split = "\\"
data_dir = "data"
data_set = "hanzi"
weight_new = 255
height_new = 255

output_path = os.path.join(data_dir,data_set + "_resize")
if not os.path.isdir(output_path):
    os.mkdir(output_path)

directors = []
image_path = os.path.join(data_dir,data_set)
for dir in os.listdir(image_path):
    #在新文件夹中创建标签目录
    dir_new = os.path.join(output_path,dir)
    if not os.path.isdir(dir_new):
        os.mkdir(dir_new)
    path = os.path.join(image_path,dir)
    if os.path.isdir(path):
        directors.append(path)

filenames = []
def convertjpg(jpgfile,resizefile,width=255,height=255):
    img = Image.open(jpgfile)
    try:
        new_img = img.resize((width,height),Image.BILINEAR)
        new_img.save(resizefile)
    except Exception as e:
        print(e)

for dir in directors:
    for filename in os.listdir(dir):
        path = os.path.join(dir,filename)
        if os.path.isfile(path):
            filenames.append(path)
for filename in filenames:
    filename_resize = filename.split(split)
    filename_resize = os.path.join(filename_resize[2], filename_resize[3])
    resizefile = os.path.join(output_path,filename_resize)
    #print(resizefile)
    convertjpg(filename,resizefile)