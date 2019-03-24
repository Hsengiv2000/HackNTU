import tkinter
from tkinter import *
import authentication as au
import MGUI1 as gui
window = tkinter.Tk()
window.title("GUI")
a = tkinter.StringVar()
b= tkinter.StringVar()
mgui = None
def load():
    
    
# creating 2 text labels and input labels

    tkinter.Label(window, text = "Username").grid(row = 0) # this is placed in 0 0
# 'Entry' is used to display the input-field
    tkinter.Entry(window, textvariable = a).grid(row = 0, column = 1) # this is placed in 0 1
   ##print(b)
    tkinter.Label(window, text = "Password").grid(row = 1) # this is placed in 1 0
    tkinter.Entry(window, textvariable = b, show='*').grid(row = 1, column = 1) # this is placed in 1 1
    #security = au.Authentication()
# 'Checkbutton' is used to create the check buttons
    #tkinter.Checkbutton(window, text = "Keep Me Logged In").grid(columnspan = 2) # 'columnspan' tells to take the width of 2 columns
    tkinter.Button(window, text = "Submit", command = grab).grid(row=2 , column = 1)                                                                       # you can also use 'rowspan' in the similar manner
    
    window.mainloop()
def grab():
    
    print(b.get())
    auth = au.Authentication(False,a.get(), b.get())
    
    if auth.Authenticate():
        window.destroy()
        gui.run()
        
    else:
        print("wrong password")
if __name__=="__main__":
    
    load()