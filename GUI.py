#!/usr/bin/env python
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
import time

#The Global Code Variable
global Code

#Start Timer
start_time = time.time()
#Function Definitions
def RandomDigit():
    return randint(2,5)

def Randomizer():
    global Code
    Code = (RandomDigit()*1000)+(RandomDigit()*100)+(RandomDigit()*10)+RandomDigit()
    Write = open("foo.txt","w")
    Write.write(str(Code))
    return Code
    
def RefClicked():
    L5.config(text=Randomizer())
    #print "Code Is: ", Code

def SoundClicked():
    engine = pyttsx.init()
    rate = engine.getProperty('rate')
    voices = engine.getProperty('voices')
    engine.setProperty('rate',rate-20)
    engine.setProperty('voice',voices[1].id)
    engine.say(Code)
    engine.runAndWait()
        
def ScanClicked():
    #print time.time()-start_time
    subprocess.Popen("Authenticate.py 1", shell=True)
    #os.exit(0)
    root.destroy()
    
def AboutClicked():
    top = Toplevel()
    top.title("About")
    mes='Hand Gesture CAPTCHA has been developed purely for experimental prototyping and research.\n@ All proprietal rights belong to Prof. A.Murugan, Qutub Khan Vajihi & Atulya Satishkumar of SRM University.'
    msg = Message(top, text=mes)
    msg.pack()
    button = Button(top, text="Dismiss", command=top.destroy)
    button.pack()
    
#Initialize GUI Root Window
root= Tk()
root.wm_title("CAPTCHA@HandGestures")
root.config(background = "#FBFCFC", cursor="dotbox")


#Add Frame
frame = Frame(root, width=500, height=300, bg="#EBF5FB")
frame.grid(row=0,column=0, padx=20, pady=20)

#Add Label1
font1= tkFont.Font(family="Instruction", size=12, weight=tkFont.BOLD)
L1=Label(frame, text="Security Check", font=font1, bg="#EBF5FB")
L1.grid(row=0, column=0, padx=1, pady=1)

#Add Label2
font2= tkFont.Font(family="Courier New", size=9, weight=tkFont.BOLD)
L2=Label(frame, text="Click The SCAN Button To Proceed", font=font2, bg="#EBF5FB")
L2.grid(row=1, column=0, padx=1, pady=1)

#Add Label3
font3= tkFont.Font(family="Courier New", size=9, weight=tkFont.BOLD)
L3=Label(frame, text="Can't Read This?\nClick REFRESH", font=font3, bg="#EBF5FB")
L3.grid(row=2, column=0, padx=1, pady=1)

#Add Label4
font4= tkFont.Font(family="Courier New", size=9, weight=tkFont.BOLD)
L4=Label(frame, text="Or Try Audio CAPTCHA", font=font4, bg="#EBF5FB")
L4.grid(row=3, column=0, padx=1, pady=1)

#Add Code Label
font5= tkFont.Font(family="Lakestreet", size=38, overstrike=0)
L5=Label(frame, text=Randomizer(), font=font5, bg="#FDFEFE")
L5.grid(row=4,column=0, padx=5, pady=5)

#Add Button Space
L6=Label(frame, font=font2, bg="#EBF5FB")
L6.grid(row=5,column=0, padx=10, pady=10)

#Add Button With Image On It
image=r"ref.gif"
img=PhotoImage(file=image)
B1=Button(frame, text="Refresh Code", command=RefClicked, image=img)
B1.image = img
B1.place(x=58, y=198)


#Add Button With Image On It
image=r"sound.gif"
img=PhotoImage(file=image)
B2=Button(frame, text="Read Code", image=img, command=SoundClicked)
B2.image = img
B2.place(x=98, y=197)

#Add Button With Image On It
image=r"questions.gif"
img=PhotoImage(file=image)
B2=Button(frame, text="Read Code", image=img, command=AboutClicked)
B2.image = img
B2.place(x=138, y=198)

#Add Continue To Scan Button
B3=Button(frame, text="Scan", font=("Trebuchet MS",25), width = 5, bg="#52BE80", foreground="#FDFEFE", command=ScanClicked)
B3.grid(row=6, columnspan=1, padx=5, pady=10)

#Start Monitoring & Updating GUI
root.mainloop()
