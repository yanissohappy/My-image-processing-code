import traceback
import cv2
import numpy as np
import os
import pydicom 

inputdir = ''
outdir = ''

file_list = [f for f in os.listdir(inputdir)]

for f in file_list:  
    if f[-3:] == "dcm":
        ds = pydicom.read_file(inputdir + '/' + f) 
        img = ds.pixel_array # get image array
        cv2.imwrite(outdir + '/' + f.replace('.dcm','.png'),img) 
