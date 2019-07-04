import tkMessageBox,Tkinter as tk
root = tk.Tk()
root.overrideredirect(1)
root.withdraw()
tkMessageBox.showinfo("Say Hello", "Hello World")
