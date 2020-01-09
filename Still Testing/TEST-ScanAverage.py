#Importing Libraries
import cv2
import numpy
import os
import math
import argparse
import glob
from PIL import Image
from Tkinter import *
from random import randint
import tkFont
import subprocess
import pyttsx

#Initialize Webcam Access
cap = cv2.VideoCapture(1)

med = []
while cap.isOpened():

    ret, img = cap.read()
    img=cv2.GaussianBlur(img,(35,35),0)
    
    cv2.rectangle(img,(350,400),(50,100),(0,0,0),3)


    del med[:]
    cv2.rectangle(img, (148,109), (163,124), (0,255,0), 0)
    med.append(img[110:125,149:164])
    cv2.rectangle(img, (199,111), (214,126), (0,255,0), 0)
    med.append(img[112:127,200:215])
    cv2.rectangle(img, (250,107), (265,122), (0,255,0), 0)
    med.append(img[108:123,251:266])
    cv2.rectangle(img, (147,142), (162,157), (0,255,0), 0)
    med.append(img[143:158,148:163])
    cv2.rectangle(img, (195,143), (210,158), (0,255,0), 0)
    med.append(img[144:159,196:211])
    cv2.rectangle(img, (254,144), (269,159), (0,255,0), 0)
    med.append(img[145:160,255:270])
    cv2.rectangle(img, (145,189), (160,204), (0,255,0), 0)
    med.append(img[146:161,190:205])
    cv2.rectangle(img, (200,189), (215,204), (0,255,0), 0)
    med.append(img[190:205,201:216])
    cv2.rectangle(img, (252,185), (267,200), (0,255,0), 0)
    med.append(img[186:201,253:268])
    cv2.rectangle(img, (146,240), (161,255), (0,255,0), 0)
    med.append(img[147:162,241:256])
    cv2.rectangle(img, (197,238), (212,253), (0,255,0), 0)
    med.append(img[198:213,239:254])
    cv2.rectangle(img, (252,236), (267,251), (0,255,0), 0)
    med.append(img[237:252,253:268])
    cv2.rectangle(img, (145,280), (160,295), (0,255,0), 0)
    med.append(img[146:161,281:296])
    cv2.rectangle(img, (194,280), (209,295), (0,255,0), 0)
    med.append(img[195:210,281:296])
    cv2.rectangle(img, (246,280), (261,295), (0,255,0), 0)
    med.append(img[247:262,281:296])
    cv2.rectangle(img, (144,314), (159,329), (0,255,0), 0)
    med.append(img[145:160,315:330])
    cv2.rectangle(img, (196,314), (211,329), (0,255,0), 0)
    med.append(img[197:212,315:330])
    cv2.rectangle(img, (243,313), (258,328), (0,255,0), 0)
    med.append(img[244:259,314:329])
    cv2.rectangle(img, (146,345), (161,360), (0,255,0), 0)
    med.append(img[147:162,346:361])
    cv2.rectangle(img, (197,344), (212,359), (0,255,0), 0)
    med.append(img[198:213,345:360])
    cv2.rectangle(img, (245,344), (260,359), (0,255,0), 0)
    med.append(img[246:261,345:360])
    cv2.rectangle(img, (144,374), (159,389), (0,255,0), 0)
    med.append(img[145:160,375:390])
    cv2.rectangle(img, (192,375), (207,390), (0,255,0), 0)
    med.append(img[193:208,376:391])
    cv2.rectangle(img, (252,376), (267,391), (0,255,0), 0)
    med.append(img[253:268,377:392])
    cv2.rectangle(img, (173,357), (188,372), (0,255,0), 0)
    med.append(img[174:189,358:373])
    cv2.rectangle(img, (177,249), (192,264), (0,255,0), 0)
    med.append(img[178:193,250:265])
    cv2.rectangle(img, (174,144), (189,159), (0,255,0), 0)
    med.append(img[145:160,175:190])
    cv2.rectangle(img, (225,142), (240,157), (0,255,0), 0)
    med.append(img[143:158,226:241])
    cv2.rectangle(img, (227,227), (242,242), (0,255,0), 0)
    med.append(img[228:243,228:243])
    cv2.rectangle(img, (229,327), (244,342), (0,255,0), 0)
    med.append(img[230:245,328:343])
    cv2.rectangle(img, (171,374), (186,389), (0,255,0), 0)
    med.append(img[172:187,375:390])
    cv2.rectangle(img, (219,374), (234,389), (0,255,0), 0)
    med.append(img[220:235,375:390])
    cv2.rectangle(img, (167,105), (182,120), (0,255,0), 0)
    med.append(img[106:121,168:183])
    cv2.rectangle(img, (226,105), (241,120), (0,255,0), 0)
    med.append(img[106:121,227:242])
    

    crop_img = img[103:397, 53:347]
    cv2.imshow('ff',crop_img)   
    
    

    #cv2.imshow('all',all_img)
    
    cv2.imshow('h',img)

    k = cv2.waitKey(5)
    if k == 27:
        break
cv2.destroyAllWindows()

#print len(med)


def hsv(med):
    h= int(numpy.average(med[:,:,0]))
    s= int(numpy.average(med[:,:,1]))
    v= int(numpy.average(med[:,:,2]))
    min=numpy.array([h-50,s-50,v-50],dtype = "uint8")
    max=numpy.array([h+50,s+50,v+50], dtype = "uint8")
    return min, max;


while True:

    ret, img = cap.read()
    img=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    img=cv2.GaussianBlur(img,(35,35),0)

    mask = []
    #print(h0, s0, v0)
    #min0 = numpy.array([0, 30, 30],dtype = "uint8")

    for i in xrange(33) : 
        min, max = hsv(med[i])
        mask.append(cv2.inRange(img,min,max))

    res = mask[0]
    for i in xrange(33) :
        res = res + mask[i]

    res = cv2.medianBlur(res, 5)
    kernel = numpy.ones((5,5),numpy.uint8)
    res = cv2.dilate(res,kernel,iterations = 1)
    res = cv2.morphologyEx(res, cv2.MORPH_OPEN, kernel)
    res = cv2.morphologyEx(res, cv2.MORPH_CLOSE, kernel)
    
    cv2.imshow('res',res)
    del mask[:]
    k = cv2.waitKey(5)
    if k == 27:
        break
os._exit(0)
