from os import close
from tkinter import *
from tkinter.font import names
import pyttsx3
from tkinter import filedialog
    
def g():
    t=text.get(1.0,END)
    tt=pyttsx3.init()
    tt.setProperty("rete",110)
    tt.say(t)
    tt.runAndWait()
    list_box.insert(END,text.get(1.0,END))

    
def h():
    Message(W).pack()
    #ww = Toplevel ( ) #ساخت صفحه جدید
    #wwe=filedialog.asksaveasfilename()
    wwe=filedialog.askopenfilename()
    
    #filedialog.askdirectory()
    #filedialog.asksaveasfilename()
    #filedialog.asksaveasfile()
    #filedialog.askopenfiles()
    file=open(wwe, "r")
 
    t=file.read()
    tt=pyttsx3.init()
    tt.setProperty("rete",110)
    tt.say(t)
    tt.runAndWait()
    input()
    file.close()
def hh():
    
    wws=filedialog.asksaveasfilename()
    file=open(wws, "w")
    t=file.write(text.get(1.0,END))
    file.close()

def hhhhb():
    wws=filedialog.askopenfilename()
    file=open(wws, "w")
    t=file.write(text.get(1.0,END))
    file.close()
 


    
    


W=Tk()
W.title("read word ")
W.iconbitmap('ringtones.ico')
menubar = Menu(W)
#
menubar.add_command(label='open', command=h)  
menubar.add_command(label='save', command=hh) 
# Delete then write
menubar.add_command(label='Delete then write', command=hhhhb) 
text = Text(W,fg='green')

text.pack()

b=Button(W,text='read',fg='green',command=g,).pack()
#creating the loop for the program
list_box = Listbox(W,fg='Gray')
list_box.pack()
W.config(menu=menubar)


W.mainloop()

    
 
