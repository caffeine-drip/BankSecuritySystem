import os
import cv2
import time
import datetime
import threading
from Tkinter import *
import imutils
import glob


cam = cv2.VideoCapture(0)
#def b():
#    def callback():
#        os.system("python Entry_in_BAnk_Img_Store.py")
#    w1=threading.Thread( name='my_servic2e',target=callback)
#    w1.start()
while True:
    ret,frame = cam.read()
    text="Enter"
    cv2.putText(frame, "Need Entry press : {}".format(text), (10, 20),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),(10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)
    cv2.imshow('img',frame)
                        
    key = cv2.waitKey(10)
    if key == 13:
        break

cam.release()
cv2.destroyAllWindows()
os.system("python Entry_in_BAnk_Img_Store.py")
