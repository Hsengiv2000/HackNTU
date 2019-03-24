import tkinter
from tkinter import *
from tkinter import simpledialog
import FaceRecognizerlegit as fr
import trainner as tr
import main as mr
import sound1 as s1
import FaceCropper2 as fc
#import tkMessageBox
import firecode as fl


def add(event = None):
    application_window = main
    answer = simpledialog.askstring("Audio", "Input Audio File", parent=application_window)
    answer1 = simpledialog.askstring("Audio", "which word to look for", parent=application_window)
    
    if answer != '':
        #change here
        #words = s1.speechToText(answer)
        x = s1.countWordsInFile(answer, answer1)
        #print("audio to text:: \n")
        #print(words)
        print("the number of times " , answer1, " appears: ", x)
        
    else:
        add()
        
def add4(event = None):
    application_window = main
    answer = simpledialog.askstring("Audio", "load, save, run", parent=application_window)
   
    if answer == "save":
        fl.readfile()
    if answer == "load":
        fl.writefile()
    elif answer =="run":
        trn = tr.Trainner()
        trn.run()
    else:
        add4()
        
        
   

def add2(event = None):
    application_window = main
    answer = simpledialog.askstring("Take Data", "Input ID", parent=application_window)
    answer2 = simpledialog.askstring("Take Data", "Name of path space size, leave empty for camera", parent=application_window)
    
   

    if answer != '' and answer.isdigit() and answer2 == '':
        FC = fr.FaceCropper(answer)
    
        
        FC.run()
    elif answer !='' and answer.isdigit():
        
        FC2 = fc.FaceCropper2(answer, answer2.split()[0] , answer2.split()[1])
        FC2.run()
    else:
        add2()

def add3():
    p = mr.Predicter()
    p.run()
def run():
    main = Tk()
    main.geometry("400x750")
    main.resizable(0, 0)
    main.configure(background='#262626')
    main.title("Main Page")
    predict = Button(main,justify = CENTER)
    train = Button(main,justify = CENTER)
    takedata = Button(main,justify = CENTER)
    audio = Button(main,justify = CENTER)

    predict.config( width=50, height=11, background='white', text='PREDICT' , command =  add3)
    train.config(width=50, height=12, background='white', text='TRAIN',command=add4)
    takedata.config(width=50, height=12, background='white', text='TAKE DATA', command=add2)
    audio.config(width=50, height=11, background='white', text='AUDIO', command=add)

    predict.pack()
    train.pack()
    takedata.pack()
    audio.pack()


    main.mainloop()