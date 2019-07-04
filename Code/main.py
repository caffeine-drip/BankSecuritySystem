import os
import threading
import time
def a():
    os.system("python Main_Gui.py")
def b():
    os.system("python update_Check.py")

w=threading.Thread( name='my_service',target=a )
w2=threading.Thread( name='my_servic2e',target=b)

w.start()
w2.start()
