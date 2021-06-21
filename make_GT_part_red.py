import numpy as np
import cv2
import glob

def generate_GT():
    count = 0
    print('-----------------------Generate GT Images-----------------------')
    for img in glob.glob("/Users/carrie/Desktop/covid_dataset/original_dataset/image/*.png"):
        ori_img = cv2.imread('/Users/carrie/Desktop/covid_dataset/original_dataset/image/'+str(count)+'.png')
        mask = cv2.imread('/Users/carrie/Desktop/covid_dataset/original_dataset/mask/'+str(count)+'.png')

        Conv_hsv_Gray = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
        _, mask = cv2.threshold(Conv_hsv_Gray, thresh=180, maxval=255, type=cv2.THRESH_BINARY)
        red_mask = np.copy(ori_img)
        red_mask[mask == 255] = [0, 0, 255]

        cv2.imwrite('/Users/carrie/Desktop/covid_dataset/original_dataset/GT/'+str(count)+'.png', red_mask)
        count += 1


generate_GT()
