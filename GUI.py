# Q1:- Write a python program using tkinter interface to write Hello World and a exit button that closes the interface.
'''
from tkinter import *
root=Tk()
root.geometry("500x500")
root.title("ASHISH")
def Hello():
    print("Hello")
bl=Button(root,command=Hello,text="prt")
bl.grid(column0, row=0)
b2=Button(root, command=quit,text="Exit")
b2.grid(column=1, row=0)

'''

##############################


# Q2:- Write a python program to in the same interface as above and create a action when the button is click it will display some text.

'''
from tkinter import *
new=Tk()
new.geometry("500x500")
new.title("MESSAGE")
def Rajat():
    print("hey")
f1=Frame(new,height=250,width=200,bg="sky blue")
f1.pack(side=TOP)
e1=Entry(f1,font=("italic",15),bd=18,bg="green",justify="right")
e1.grid(row=0,column=0)
btn1=Button(f1,padx=30,pady=25,bd=8,command=Rajat,fg="brown",font=("italic",10),text="prt").grid(row=1,column=0)

'''

################################


# Q3:- Create a frame using tkinter with any label text and two buttons.One to exit and other to change the label to some other text.

'''
from tkinter import *
hlo=Tk()
hlo.geometry("800x600")
hlo.title("print")
def Python():
    print("Python")
f1=Frame(hlo,height=400,width=400,bg="cyan")
f1.pack()
lb1=Label(f1,font=("ALGERIAN",30,"bold"),bg="Light Pink",text="Program")
lb1.pack()
f2=Frame(hlo,height=500,width=400,bg="Light green")
f2.pack()
b1=Button(f2,padx=15,pady=10,bd=6,command=Python,fg="Light Blue",font=("italic",10),text="prt").grid(row=1,column=0)
b2=Button(f2,padx=15,pady=10,bd=6,command=quit,fg="Light Green",font=("italic",10),text="QUIT").grid(row=1,column=1)
'''


###############################


# Q4:- Write a python program using tkinter interface to take an input in the GUI program and print it.

'''
from tkinter import *
root=Tk()
root.geometry("800x800")
root.title("GUI")
lbl = Label(root, text="Hello")
lbl.grid(column=0, row=0)
txt = Entry(root,width=10)
txt.grid(column=1, row=0)
def clicked():
    res = "Welcome to " + txt.get()
    lbl.configure(text= res)
btn = Button(root, text="Click Me", command=clicked)
btn.grid(column=2, row=0)
root.mainloop()
'''

######################## END
