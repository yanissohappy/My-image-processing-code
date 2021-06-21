import os
import pydicom
from os import walk


def ensureUtf(s):
  try:
      if type(s) == unicode:
        return s.encode('utf8', 'ignore')
  except: 
    return str(s)

path = "E:\超音波影像" 
path = ensureUtf(path)	# utf-8
picture_count = 0
circle_logo_num = 0
breast_logo_num = 0

for root, dirs, files in walk(path):
    for f in files:
        f_path = os.path.join(root, f)
        print(f_path)
        if f_path[-3:] == "dcm":
            picture_count += 1
            try:
                dataset = pydicom.dcmread(f_path)
                processing_function = dataset[0x18, 0x5020] # 如果沒有辦法 assign，就會直接跳到 except，代表抓到的是圓 logo
                # print(processing_function)
                breast_logo_num += 1 # 如果上面可以 assign，則代表分到了 breast logo     
            except: 
                # print("HA!是圓球啦")
                circle_logo_num += 1 
                continue

print("------------------------")
print("breast type: ", breast_logo_num)
print("circle type: ", circle_logo_num)
print("total: ", picture_count)

