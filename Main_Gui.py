# -*- coding: utf-8 -*-
##Entry Module
#(1)Entry_window_for_bank.py -> (2)Entry_in_BAnk_Img_Store.py
##Motion Detection
#(1)Motion_detect.py



from Tkinter import *
import os
import threading 
import time

def b():
    def callback():
        os.system("python Motion_detect.py")
    w1=threading.Thread( name='my_servic2e',target=callback)
    w1.start()

def c():
    def callback1():
        os.system("python Entry_window_for_bank.py")
    w2=threading.Thread( name='my_servic3e',target=callback1)
    w2.start()

def d():
    def callback2():
        os.system("python Motion_Detect_Galery.py")
    w3=threading.Thread( name='my_servic4e',target=callback2)
    w3.start()

def e():
    def callback3():
        os.system("python Entry_in_bank_Gallery.py")
    w4=threading.Thread( name='my_servic5e',target=callback3)
    w4.start()
    
def f():
    def callback4():
        os.system("python Image_Face_Obj_Detection.py")
    w5=threading.Thread( name='my_servic6e',target=callback4)
    w5.start()
    

def a():
    master = Tk()
    master.minsize(306, 300)
    master.title("Overwatch Security System")

    nE=Label(master,text=("---------------------------------------------------------------------"))
    nE.pack()
    n=Label(master,text=" Ж Ж Ж Ж Ж |  The Main Security System Wnidow  | Ж Ж Ж Ж Ж ")
    n.pack()
    n1=Label(master,text=" Ж Ж Ж Ж Ж |         Various Modules Available         | Ж Ж Ж Ж Ж ")
    n1.pack()
    nE=Label(master,text=("---------------------------------------------------------------------"))
    nE.pack()
    
    n2=Label(master,text="___________________________________________")
    n2.pack()
    n2=Label(master,text="Modules")
    n2.pack()
    n2=Label(master,text="___________________________________________")
    n2.pack()
    n2=Label(master,text="")
    n2.pack()
    
    bE=Label(master,text=("To Check Unauthorized access in any Places"))
    bE.pack()
    b0 = Button(master, text="Motion Detection",command= b)
    b0.pack()
    n2=Label(master,text="")
    n2.pack()

    b1E=Label(master,text=("To Know exactly who enterd in the Bank"))
    b1E.pack()
    b1 = Button(master, text="Entry in Bank", command=c)
    b1.pack()
    n2=Label(master,text="")
    n2.pack()
    
    b4E=Label(master,text=("To Detect Criminal faces and Guns"))
    b4E.pack()
    b4 = Button(master, text="Face and Object Detection", command=f)
    b4.pack()
    n2=Label(master,text="")
    n2.pack()
    
    n2=Label(master,text="___________________________________________")
    n2.pack()
    n2=Label(master,text="Viewing options")
    n2.pack()
    n2=Label(master,text="___________________________________________")
    n2.pack()

    n2=Label(master,text="")
    n2.pack()
    
    b2E=Label(master,text=("To Know What Moved"))
    b2E.pack()
    b2 = Button(master, text="MotionDetect Images", command=d)
    b2.pack()
    n2=Label(master,text="")
    n2.pack()

    b3E=Label(master,text=("To Know who enterd in the Bank"))
    b3E.pack()
    b3 = Button(master, text="BankEntry Images", command=e)
    b3.pack()
    n2=Label(master,text="")
    n2.pack()


    
    mainloop()
w=threading.Thread( name='my_service',target=a )

w.start()





