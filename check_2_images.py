import os, sys
from os import listdir
from shutil import copyfile
import cv2
import numpy as np

image_path = ".\\image"
mask_path = ".\\label"

for full_file_name in listdir(image_path):
    file = full_file_name[:-8]
    print(full_file_name, file)
    image = cv2.imread(image_path + "\\" + file + "_ori.bmp")
    # I just resized the image to a quarter of its original size

    grey = cv2.imread(mask_path + "\\" + file + "_mask.bmp")
    # Make the grey scale image have three channels

    try:
        numpy_horizontal = np.hstack((image, grey))
        numpy_horizontal = cv2.resize(numpy_horizontal, (0, 0), None, .5, .5)
        cv2.imshow(file, numpy_horizontal)
        
        cv2.waitKey()
        cv2.destroyAllWindows()         
    except:
        print(file)


