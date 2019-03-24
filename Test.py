import tkinter
from tkinter import *
from tkinter import simpledialog
import CustomButton

main = Tk()
main.geometry("400x750")
main.resizable(0, 0)
main.configure(background='#262626')
main.title("Main Page")

photo1=PhotoImage(file="binoculars.png")
photo3=PhotoImage(file="edit.png")
photo2=PhotoImage(file="coach.png")
photo4=PhotoImage(file="speaker.png")

my_button = Button(main, text='       PREDICT  ', image=photo1, compound=LEFT, font=('Helvetica', 36), cursor='hand2')
my_button.config(width='400', padx = 0, pady =0, bd=0, highlightthickness=0)

my_button2 = Button(main, text='         TRAIN     ', image=photo2, compound=LEFT, font=('Helvetica', 36), cursor='hand2')
my_button2.config(width='400', padx = 0, pady =0, bd=0, highlightthickness=0)

my_button3 = Button(main, text='   WRITE DATA', image=photo3, compound=LEFT, font=('Helvetica', 36), cursor='hand2')
my_button3.config(width='400', padx = 0, pady =0, bd=0, highlightthickness=0)

my_button4 = Button(main, text='         AUDIO     ', image=photo4, compound=LEFT, font=('Helvetica', 36), cursor='hand2')
my_button4.config(width='400', padx = 0, pady =0, bd=0, highlightthickness=0)

my_button.place(x=0, y=0, width=400, height= 182)
my_button2.place(x=0, y=190, width=400, height= 181)
my_button3.place(x=0, y=380, width=400, height= 181)
my_button4.place(x=0, y=570, width=400, height= 182)

main.mainloop()
