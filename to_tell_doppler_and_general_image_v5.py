import os
import pydicom
from os import walk
import cv2
import numpy as np


def ensureUtf(s):
  try:
      if type(s) == unicode:
        return s.encode('utf8', 'ignore')
  except: 
    return str(s)

path = "E:\新的要整理的乳房超音波影像(2000~3999)" # 要改!
path = ensureUtf(path)	# utf-8
picture_count = 0
doppler_case_num = 0
general_case_num = 0

doppler_case = []

for root, dirs, files in walk(path):
    for f in files:
        f_path = os.path.join(root, f)
        print(f_path)
        if f_path[-3:] == "dcm":
            picture_count += 1
            try:
                dataset = pydicom.dcmread(f_path)
                ultrasound_color_data_present = dataset[0x0028, 0x0014].value
                _ = dataset[0x0028, 0x0301] # Burned In Annotation     
                
                if ultrasound_color_data_present == 1:
                    doppler_case.append(f_path)
                    doppler_case_num += 1
                else:
                    general_case_num += 1
            except: 
                general_case_num += 1
                continue


# print("------------------------")
# print("都普勒的照片位置:")
# for i in doppler_case:
    # print(i)
    
writepath = 'D:\logodetection\doppler_filepath.txt' # 要改!要記錄都普勒影像的路徑
mode = 'a' if os.path.exists(writepath) else 'w'

with open(writepath, mode) as f:
    for i in doppler_case:
        f.write(i)
        f.write("\n")
    f.write("doppler type: " + str(doppler_case_num) + "\n")
    f.write("general type: " + str(general_case_num) + "\n")
    f.write("total: " + str(picture_count))
f.close()        

print("------------------------")
print("doppler type: ", doppler_case_num)
print("general type: ", general_case_num)
print("total: ", picture_count)