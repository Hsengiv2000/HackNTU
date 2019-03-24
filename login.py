import tkinter
from tkinter import *
import authentication as au
import access as ac
from PIL import Image, ImageTk
import MGUI1 as gui

root = tkinter.Toplevel()
a = tkinter.StringVar()
b= tkinter.StringVar()
mgui = None
class LoginFrame(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.label_username = Label(self, text="Username:", font=('default', 20))
        self.label_password = Label(self, text="Password:", font=('default', 20))

        self.entry_username = Entry(self, textvariable = a, font=('default', 20))
        self.entry_password = Entry(self, textvariable = b,show="*", font=('default', 20))

        self.label_username.grid(row=0, sticky=E)
        self.label_password.grid(row=1, sticky=E)
        self.entry_username.grid(row=0, column=1,)
        self.entry_password.grid(row=1, column=1, pady=10)

        self.logbtn = Button(self, text="Login", command=grab)
        self.logbtn.config(height=2, width=20, font=('default', 20))
        self.logbtn.grid(columnspan=2)
        self.logbtn = Button(self, text="Sign Up", command=grab2)
        self.logbtn.config(height=2, width=20, font=('default', 20))
        self.logbtn.grid(columnspan=2)

        self.pack()

    
def grab2():
    print("Registering User")
    try:
        ac.writeData(a.get() , b.get())
        print("Process Done")
    except:
        
        print("Error- Try Again Later")
        raise
def grab():
    try:
        if(ac.authenticate(a.get(), b.get())):
            root.destroy()
            gui.run()
        else:
            print("Sorry, Wrong username or password")
    except:
        print("An error occured")    
        raise        
    '''print(b.get())
    auth = au.Authentication(False,a.get(), b.get())
    
    if auth.Authenticate():
        window.destroy()
        gui.run()
        
    else:
        print("wrong password")
'''
def load():
    
    root.geometry("400x750")
    root.resizable(0, 0)
    root.title("Login")
    canvas = Canvas(root, width = 300, height = 300)
    canvas2 = Canvas(root, width =400, height = 110)
    canvas2.pack()
    canvas.pack()
    img = ImageTk.PhotoImage(Image.open("policeman.png"))
    canvas.create_image(20,20, anchor=NW, image=img)
    lf = LoginFrame(root)
    root.mainloop()
if __name__=="__main__":
    
    load()