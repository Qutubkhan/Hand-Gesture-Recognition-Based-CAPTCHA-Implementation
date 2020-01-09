
#Importing Libraries
import cv2
import numpy as np
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
import webbrowser
import time

#The Current CAPTCHA
global Code

#Load Current CAPTCHA To 'Code'
Read = open("foo.txt","r")
Code = int(Read.read())
Code = int(str(Code)[::-1])

#Flags & Variables
Valid = 1
Divisor = 1
Mod = 10
Cur_Code = 0
Int_Flag = 0
global root

#Timer Variable
start_timer = 0

#Function Definitions
def ProceedClicked():
    root.destroy()
    
def Show_Prompt(Cur_Code):
    global root
    root = Tk()
    root.wm_title("CAPTCHA@HandGestures")
    root.config(background = "#FBFCFC", cursor="dotbox")
    frame = Frame(root, width=200, height=200, bg="#EBF5FB")
    frame.grid(row=0,column=0, padx=20, pady=20)
    font1 = tkFont.Font(family="Instruction", size=8, weight=tkFont.BOLD)
    L1 = Label(frame, text="Please Show The Digit", font=font1, bg="#EBF5FB")
    L1.grid(row=0, column=0, padx=1, pady=1)
    font1 = tkFont.Font(family="Instruction", size=8, weight=tkFont.BOLD)
    L2 = Label(frame, text="That Will Be Displayed In The Next Window", font=font1, bg="#EBF5FB")
    L2.grid(row=1, column=0, padx=1, pady=1)
    font1 = tkFont.Font(family="Instruction", size=10, weight=tkFont.BOLD)
    L3 = Label(frame, text="-SHOW THE ENTIRE PALM", font=font1, bg="#EBF5FB")
    L3.grid(row=2, column=0, padx=1, pady=1)
    L4 = Label(frame, text="INSIDE THE BLACK BOX AND HOLD", font=font1, bg="#EBF5FB")
    L4.grid(row=3, column=0, padx=1, pady=1)
    L5 = Label(frame, text="-SPACE YOUR FINGERS SUFFICIENTLY", font=font1, bg="#EBF5FB")
    L5.grid(row=4, column=0, padx=1, pady=1)
    B1 = Button(frame, text="PROCEED", font=("Trebuchet MS", 14), bg="#52BE80", foreground="#FDFEFE", command=ProceedClicked)
    B1.grid(row=5, column=0, padx=5, pady=5)
    root.mainloop()
    return    
    
#Initializing Webcam Access
cap = cv2.VideoCapture(0)

#Start Main Looping
while(Valid<=4) :
    Cur_Code = (Code/Divisor)%Mod
    if Valid == 1:
        Show_Prompt(Cur_Code)
    Int_Flag = 0
    Auth_Count = 10
    if Cur_Code==2 :
        Auth_Count = 20
    #Start Timer
    start_timer = time.time()
    if cap.isOpened() == False :
        print "Please Connect A Webcam"
        os._exit(0)
    while(cap.isOpened() and Int_Flag<=Auth_Count):
        #Read Image To img 
        ret, img = cap.read()
        #Digit Box
        cv2.rectangle(img, (472,188), (510,295), (255,255,255),90)
        #Label Box
        cv2.rectangle(img, (148,25), (524,49), (255,255,255),23)
        #Digit In Box
        cv2.putText(img,str(Cur_Code), (430,305), cv2.FONT_HERSHEY_DUPLEX, 6, 9)
        #Highlight ROI
        cv2.rectangle(img,(350,390),(50,90),(0,0,0),3)
        #Crop ROI
        crop_img = img[93:387, 53:347]
        #Greyscale ROI
        grey = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
        #Apply Gaussian Blur To ROI
        value = (51, 51)
        blurred = cv2.GaussianBlur(grey, value, 0)
        #Threshold The Blurred ROI
        _, thresh1 = cv2.threshold(blurred, 127, 255,
                                   cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
        '''
        For Dark Background Don't Invert Threshold
        _, thresh1 = cv2.threshold(grey, 127, 255,
                                   cv2.THRESH_BINARY)
        '''
        #Display Threshold
        #cv2.imshow('Threshold', thresh1)
        #Apply Contours To Thresholded Region
        contours, hierarchy = cv2.findContours(thresh1.copy(),cv2.RETR_TREE, 
                cv2.CHAIN_APPROX_NONE)
        #Declare Variables
        max_area = -1
        ci= -1
        defects = None
        #Find Largest Contour In The ROI
        for i in range(len(contours)):
            cnt=contours[i]
            #cv2.drawContours(crop_img,[cnt],0,(0,255,0),0)
            area = cv2.contourArea(cnt)
            if(area>max_area):
                max_area=area
                ci=i
        if(ci!=-1):
            #cnt Is Largest Contour
            cnt=contours[ci]
            #Co-ordinates Of cnt
            x,y,w,h = cv2.boundingRect(cnt)
            #Draw Rectangle Over cnt
            cv2.rectangle(crop_img,(x,y),(x+w,y+h),(0,0,255),0)
            #Find Convex Hull Over cnt
            hull = cv2.convexHull(cnt)
            #Define Blank Frame
            drawing = np.zeros(crop_img.shape,np.uint8)
            #Draw Contours Over drawing
            cv2.drawContours(drawing,[cnt],0,(0,255,0),0)
            cv2.drawContours(drawing,[hull],0,(0,0,255),0)
            #Find Convex Hull Without ReturnPoints
            hull = cv2.convexHull(cnt,returnPoints = False)
            #Find All Convexity Defects
            defects = cv2.convexityDefects(cnt,hull)
            count_defects = 0
            cv2.drawContours(thresh1, contours, -1, (0,255,0), 3)
            i=0
        if(defects!=None):
            for i in range(defects.shape[0]):
                s,e,f,d = defects[i,0]
                start = tuple(cnt[s][0])
                end = tuple(cnt[e][0])
                far = tuple(cnt[f][0])
                a = math.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
                b = math.sqrt((far[0] - start[0])**2 + (far[1] - start[1])**2)
                c = math.sqrt((end[0] - far[0])**2 + (end[1] - far[1])**2)
                #Law Of Cosines & Conversion To Degree(From Radians)
                temp = (b*b + c*c - a*a)/(2*b*c)
                angle = math.acos(temp) * 57
                if angle >=1 and angle <= 90:
                    #print angle
                    count_defects += 1
                    #cv2.circle(crop_img,start,5,[100,100,255],-1)
                    #cv2.circle(crop_img,end,5,[200,200,255],-1)
                    cv2.circle(crop_img,far,5,[0,0,255],-1)
                    cv2.line(crop_img,start,end,[0,255,0],2)
                    #cv2.line(crop_img,far,end,[0,255,0],2)
                    #cv2.line(crop_img,start,far,[0,255,0],2)
            if count_defects == Cur_Code-1:
                cv2.putText(img,str(Int_Flag), (326,382), cv2.FONT_HERSHEY_PLAIN, 1, 2)
                Int_Flag = Int_Flag + 1
                cv2.putText(img,"Correct", (277,45), cv2.FONT_HERSHEY_DUPLEX, 1, 5)
            else:
                cv2.putText(img,"Not Recognized", (210,45),\
                            cv2.FONT_HERSHEY_DUPLEX, 1, 5)

        cv2.imshow('Gesture Recognition', img)
        cv2.imshow('Blurred',blurred)
        cv2.imshow('Thresholded',thresh1)
        all_img = np.hstack((drawing, crop_img))
        cv2.imshow('Contours', all_img)
        k = cv2.waitKey(10)

    #print time.time()-start_timer
    cv2.destroyAllWindows()
    Divisor = Divisor * 10
    Valid = Valid + 1
    k = cv2.waitKey(10)

if Valid == 5 :
    webbrowser.open('file:///C:/Python27/PROJECT/Project/templates/final.html')
os._exit(0)
        
    



