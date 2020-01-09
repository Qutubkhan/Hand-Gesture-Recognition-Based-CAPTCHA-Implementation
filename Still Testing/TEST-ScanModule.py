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
cap = cv2.VideoCapture(0)

#Face Cascade
#face_cascade=cv2.CascadeClassifier('handhaar.xml')
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

#Define Range For Skin Color In HSV
min_YCrCb = numpy.array([10,133,77],numpy.uint8)
max_YCrCb = numpy.array([255,173,127],numpy.uint8)

#Flags & Variables
flag = 0 
face_im = None
face=  None

while flag<5:

    # Take each frame
    ret, img = cap.read()
    cv2.putText(img, 'Kindly Position Your Face In The Box', (20,30), cv2.FONT_HERSHEY_SIMPLEX, 0.75, 1)   
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 2, 5)
    
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        rg=gray[y:y+h, x:x+w]
        face_im=img[y:y+h, x:x+w]
        flag =flag + 1
        
        eyes = eye_cascade.detectMultiScale(rg)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(face_im, (ex, ey), (ex+ew, ey+eh), (0,255, 0),2)


    if face_im!=None:
        cv2.imshow('face',face_im)
    cv2.imshow('img',img)
    face=face_im
    k = cv2.waitKey(5)
    if k == 27:
        break


while(cap.isOpened()):
    #Each Frame
    ret, img = cap.read()
    #Plot Rectangle As ROI
    cv2.rectangle(img, (300,300), (50,50), (0,255,0), 0)
    #Crop ROI
    crop_img = img[50:300, 50:300]
    crop_img = cv2.GaussianBlur(crop_img, (35,35) , 0)

    face = cv2.GaussianBlur(face, (35, 35), 0)
    #Convert To YCrCb
    faceycrcb = cv2.cvtColor(face, cv2.COLOR_BGR2YCR_CB)
    #print(numpy.average(faceycrcb[:,:,0]))
    #print(numpy.average(faceycrcb[:,:,1]))
    #print(numpy.average(faceycrcb[:,:,2]))
    y=int(numpy.average(faceycrcb[:,:,0]))
    cr=int(numpy.average(faceycrcb[:,:,1]))
    cb=int(numpy.average(faceycrcb[:,:,2]))

    #Convert Hand Crop To YCrCb
    handycrcb = cv2.cvtColor(crop_img, cv2.COLOR_BGR2YCR_CB)

    #YCrCb Range Modified
    min_YCrCb = numpy.array([y-20,cr-20,cb-10],numpy.uint8)
    max_YCrCb = numpy.array([200,200,200],numpy.uint8)

    handmask = cv2.inRange(handycrcb, min_YCrCb,max_YCrCb)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (1, 1))
    mask = cv2.erode(handmask, kernel, iterations = 1)
    mask = cv2.dilate(handmask, kernel, iterations = 1)
    mask = cv2.GaussianBlur(handmask, (35,35), 0)

    #handmask = cv2.adaptiveThreshold(handmask,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
    #            cv2.THRESH_BINARY,11,2)

    #_, handmask = cv2.threshold(handmask, 127, 255,
    #                           cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)  


    contours, hierarchy = cv2.findContours(handmask.copy(),cv2.RETR_EXTERNAL, 
            cv2.CHAIN_APPROX_SIMPLE)
    max_area = -1
    ci= -1
    for i in range(len(contours)):
        cnt=contours[i]
        area = cv2.contourArea(cnt)
        if(area>max_area):
            max_area=area
            ci=i
    cnt=contours[ci]
    x,y,w,h = cv2.boundingRect(cnt)
    cv2.rectangle(crop_img,(x,y),(x+w,y+h),(0,0,255),0)
    hull = cv2.convexHull(cnt)
    drawing = numpy.zeros(crop_img.shape,numpy.uint8)
    cv2.drawContours(drawing,[cnt],0,(0,255,0),0)
    cv2.drawContours(drawing,[hull],0,(0,0,255),0)
    hull = cv2.convexHull(cnt,returnPoints = False)
    defects = cv2.convexityDefects(cnt,hull)
    count_defects = 0
    cv2.drawContours(handmask, contours, -1, (0,255,0), 3)
    i=0
    for i in range(defects.shape[0]):
        s,e,f,d = defects[i,0]
        start = tuple(cnt[s][0])
        end = tuple(cnt[e][0])
        far = tuple(cnt[f][0])
        a = math.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
        b = math.sqrt((far[0] - start[0])**2 + (far[1] - start[1])**2)
        c = math.sqrt((end[0] - far[0])**2 + (end[1] - far[1])**2)
        angle = math.acos((b**2 + c**2 - a**2)/(2*b*c)) * 57
        if angle <= 90:
            count_defects += 1
            cv2.circle(crop_img,far,1,[0,0,255],-1)
        #dist = cv2.pointPolygonTest(cnt,far,True)
        cv2.line(crop_img,start,end,[0,255,0],2)
        #cv2.circle(crop_img,far,5,[0,0,255],-1)
    if count_defects == 1:
        cv2.putText(img,"Two", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
    elif count_defects == 2:
        cv2.putText(img, "Three", (5,50), cv2.FONT_HERSHEY_SIMPLEX, 1, 2)
    elif count_defects == 3:
        cv2.putText(img,"Four", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
    elif count_defects == 4:
        cv2.putText(img,"Five", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
    else:
        cv2.putText(img,"Not Recognized", (50,50),\
                    cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
    


    all_img = numpy.hstack((drawing, crop_img))
    cv2.imshow('Contours', all_img)
    #cv2.imshow('mask',handmask)
    #cv2.imshow('cropped image',crop_img)
    #cv2.imshow('captured face',face)
    cv2.imshow('r',img)
    k = cv2.waitKey(10)
    if k == 27:
        break
    
os._exit(0)

