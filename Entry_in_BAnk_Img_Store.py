from Tkinter import *
import imutils
import time
import datetime
import numpy as np
import cv2
import glob
import os

if not os.path.exists(".\\EntryInBankImgDay_"+time.strftime("%d-%m-%Y")):
    os.makedirs(".\\EntryInBankImgDay_"+time.strftime("%d-%m-%Y"))
    g=0
else:
    list_of_files = glob.glob(".\\EntryInBankImgDay_"+time.strftime("%d-%m-%Y")+"\\*")
    if list_of_files==[]:
        g=0
    else:
        latest_file = max(list_of_files, key=os.path.getctime)
        g=[latest_file[x] for x in xrange(31,latest_file.index("#"))]
        g=''.join(g)

#####################
def Store():
    global g
    m = Tk()
    m.minsize(306, 300)
    m.title("Entry Window")

    def Fun():
        global s,p,g
        nameEE=Label(m,text=("_________________________________________"))
        nameEE.grid(row=2,column=1)
        s = nameE.get()
        p = butpass.get()
        #checking Validity
        if p.isdigit()==False or len(p)!=12:
            m.destroy()
            Store()
        else:
            #print s,p
            g=int(g)
            g=g+1
            cv2.imwrite(".\\EntryInBankImgDay_"+time.strftime("%d-%m-%Y")+"\\"+str(g)+"# " +s+ " Adhar "+p+".jpg" , roi_color)
            m.destroy()
    #Enter Name and Adhar card no
    name=Label(m,text="Name")
    password=Label(m,text="Adhar No")
    nameE=Entry(m)
    nameEE=Label(m,text=("_________________________________________"))
    #calling Function Fun to enter the data and image in database
    namepass=Button(m,text="Enter",command=Fun)
    butpass=Entry(m)
    
    nameEeeE=Label(m,text=("The Overwatch"))
    nameEeeE.grid(row=6,column=1)
    Warnin=Label(m,text=("Note : \nThe Adhar Number Should be of 12 digits"))
    Warnin.grid(row=6,column=1)
    name.grid(row=0,column=0)
    password.grid(row=1,column=0)
    nameE.grid(row=0,column=1)
    namepass.grid(row=0,column=2)
    butpass.grid(row=1,column=1)
    nameEE.grid(row=2,column=1)

    m.mainloop()


#####################
#Defined Cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#camera Started
cam = cv2.VideoCapture(0)
time.sleep(0.5)
while True:
    ret,frame = cam.read()


    img = frame
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #Face Detection 
    faces = face_cascade.detectMultiScale(gray, 1.3, 2)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x-6,y-6),(x+w+16,y+h+16),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y-6:y+h+16, x-6:x+w+16]
        roi_color = imutils.resize(roi_color, width=400)
        cv2.putText(roi_color,datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),(10,roi_color.shape[0]-20),cv2.FONT_HERSHEY_SIMPLEX,0.35,(0, 0, 255),1)
    # if faces Found Show Face and call the Store GUI
    if faces!=():
        print"-------"
        cv2.imshow('ismg',roi_color)
        Store()
        break

cam.release()
cv2.destroyAllWindows()
