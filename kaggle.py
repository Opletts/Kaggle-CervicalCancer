import matplotlib.pyplot as plt
import os
import numpy as np
import cv2

for i in os.listdir('/home/opletts/Stuff/test'):

    img = cv2.imread('/home/opletts/Stuff/test/'+i)
    img = cv2.resize(img, (360, 480))
    #img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)    
    img_cpy = img.copy()
    
    img_cpy = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    img_cpy[np.where(img_cpy[:,:,2] < 160)] = [0, 0, 0]
    img_cpy[np.where(img_cpy[:,:,2] >= 160)] = [255, 255, 255]

    img_cpy = cv2.cvtColor(img_cpy, cv2.COLOR_BGR2GRAY)

    im2, contours, hierarchy = cv2.findContours(img_cpy,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    
    #cv2.drawContours(img, contours, -1, (0,255,0), 3)
    m = 0
    c = 0
    for i in range(len(contours)):
        cnt = contours[i]
        area = cv2.contourArea(cnt)
        if(m<area):
            m = area
            c = cnt


    x,y,w,h = cv2.boundingRect(c)
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)   
    
    cv2.imshow('og', img)
    
    #img = img[y:y+h, x:x+w]    

    #img = cv2.resize(img, (244,244))    

    #cv2.imshow('roi', img_cpy)
    cv2.imshow('roi', img)
    cv2.waitKey(0)