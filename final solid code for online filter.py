#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import cv2
import matplotlib.pyplot as plt

class solidfilter:
    def __init__(self, barcode, im_dir):
        self.barcode = barcode
        self.im_dire = im_dir
        
    def fetch_images(self):
        #filter pic
        cv_img = plt.imread('C:/Users/asus/Desktop/'+ self.barcode +'.jpg')
        cv_img = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        cv_img = cv_img.copy()
        cv_img = cv_img.astype("uint8")
        
        #user or default picture
        user_img = plt.imread(self.im_dire)
        user_img = user_img.copy()
        user_img = user_img.astype("uint8")
        
        #resize
        height = 3128
        width = 2952
        user_img = cv2.resize(user_img, dsize=(height,width))
        cv_img = cv2.resize(cv_img, dsize=(height,width))  
        
        
        #contrast of user pic
        contrast = 40
        img_con = user_img * (contrast/127 + 1 ) - contrast
        img_con = np.clip(img_con, 0, 255)
        img_con = img_con.astype("uint8")
        
        img_blend = cv_img*0.4 + img_con* 0.6
        img_blend = np.clip(img_blend, 0, 255)
        img_blend = img_blend.astype("uint8")
        self.img_blended = img_blend

def trigger():
    barcode = input("please enter sunglsses barcode: ")   
    im_dir = input("please enter image name: ")
    im_dir = "C:/Users/asus/Desktop/"+im_dir+".JPG"
    
    service = solidfilter(barcode=barcode, im_dir=im_dir)
    service.fetch_images()
    result = service.img_blended
    
trigger()

