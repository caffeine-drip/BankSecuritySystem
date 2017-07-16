import datetime
import imutils
import time
import cv2
import os
import numpy as np
import glob
import Tkinter as tk
import thread

ii=0
#Cascade files for Face and eye
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
#eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
#body_cascade = cv2.CascadeClassifier('haarcascade_upperbody.xml')
#lear_cascade = cv2.CascadeClassifier('haarcascade_mcs_leftear.xml')
#rear_cascade = cv2.CascadeClassifier('haarcascade_mcs_rightear.xml')

#camera started
camera = cv2.VideoCapture(0)
time.sleep(0.5)

firstFrame = None
if not os.path.exists(".\\MotionImgDay_"+time.strftime("%d-%m-%Y")):
    os.makedirs(".\\MotionImgDay_"+time.strftime("%d-%m-%Y"))
    g=0
else:
    list_of_files = glob.glob(".\\MotionImgDay_"+time.strftime("%d-%m-%Y")+"\\*")
    if list_of_files==[]:
        g=0
    else:
        latest_file = max(list_of_files, key=os.path.getctime)
        g=[latest_file[x] for x in xrange(26,len(latest_file)-4)]
        g=''.join(g)
while True:
    (grabbed, frame) = camera.read()
    text = "No Motion"
    if not grabbed:
        break

    frame0 = imutils.resize(frame, width=500)
    frame = imutils.resize(frame, width=500)
    gray0 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray0, (21, 21), 0)
    if firstFrame is None:
        firstFrame = gray
        continue
    #compute the absolute difference

    frameDelta = cv2.absdiff(firstFrame, gray)
    thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]

    thresh = cv2.dilate(thresh, None, iterations=2)
    (cnts, _) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),(10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 255), 1)
    cv2.putText(frame0, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),(10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 255), 1)

    #contours
    # print len(cnts)
    for c in cnts:
        #update the text and first frame
        (x, y, w, h) = cv2.boundingRect(c)
        if w*h>1000:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        text = "Motion Detected"
    #Face Detection   
    if text == "Motion Detected":
        f=''
        firstFrame = gray
        faces = face_cascade.detectMultiScale(gray0, 1.3, 2)
        for (x,y,w,h) in faces:
            cv2.rectangle(frame0,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray0[y:y+h, x:x+w]
            roi_color = frame0[y:y+h, x:x+w]
            #Eye Detection
            #eyes = eye_cascade.detectMultiScale(roi_gray)
            #for (ex,ey,ew,eh) in eyes:
            #    cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        g=int(g)
        g=g+1
        cv2.imwrite(".\\MotionImgDay_"+time.strftime("%d-%m-%Y")+"\\"+str(g)+".jpg" , frame0)
        #import Notification_Window as Npp
        '''thread.start_new_thread(Notification_Window, ())'''

    ##
    # draw the text and timestamp on the frame
    cv2.putText(frame, "Room Status: {}".format(text), (10, 20),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    # show the frame and record if the user presses a key
    cv2.imshow("Faces Detected", frame0)
    cv2.imshow("Motion Detection", frame)
    #cv2.imshow("Thresh", thresh)
    #cv2.imshow("Frame Delta", frameDelta)
    key = cv2.waitKey(1) & 0xFF

    # if the `q` key is pressed, break from the lop
    if key == ord("q"):
            break

camera.release()
cv2.destroyAllWindows()

