import tkMessageBox,Tkinter as tk
from os import listdir
import datetime
import time
Motion_list = listdir(".\\MotionImgDay_"+time.strftime("%d-%m-%Y"))
Entry_list = listdir(".\\EntryInBankImgDay_"+time.strftime("%d-%m-%Y"))
while True:
    Motion_list1 = listdir(".\\MotionImgDay_"+time.strftime("%d-%m-%Y"))
    Entry_list1 = listdir(".\\EntryInBankImgDay_"+time.strftime("%d-%m-%Y"))
    if(len(Motion_list)!=len(Motion_list1)):
        root = tk.Tk()
        root.overrideredirect(1)
        root.withdraw()
        tkMessageBox.showinfo("Update", "Motion Detected")
        Motion_list = listdir(".\\MotionImgDay_"+time.strftime("%d-%m-%Y"))
    if(len(Entry_list)!=len(Entry_list1)):
        root = tk.Tk()
        root.overrideredirect(1)
        root.withdraw()
        tkMessageBox.showinfo("Update", "New Entry in Bank")
        Entry_list = listdir(".\\EntryInBankImgDay_"+time.strftime("%d-%m-%Y"))
