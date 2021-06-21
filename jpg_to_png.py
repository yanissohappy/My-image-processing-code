import cv2
import os, sys
from os import listdir
from shutil import copyfile

def getExtension(file_path):
    return file_path.split(".")[-1]

for file_image in listdir("."):
    if getExtension(file_image) != "png":
        # print(file_image[:-4])
        try:
            image = cv2.imread("." + "\\" + file_image)
            cv2.imwrite("." + "\\" + file_image[:-4] + ".png", image)
        except:
            print(file_image)
