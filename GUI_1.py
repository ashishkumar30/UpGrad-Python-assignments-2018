# Q1:- Create a dict with name and mobile number.Define a GUI interface using tkinter and pack the label

'''

from tkinter import *
d={'Rajat':9896,'Ashish':9990,'Param':9593,'Naveen':8453,'Vedant':9846,'Sahil':8595,'Ayush':9512,'Pritam':9568}
root=Tk()
s=Scrollbar(root)
s.pack(side=RIGHT,fill=Y)
l=Listbox(root,yscrollcommand=s.set)
for key in d.values():
    l.insert(END,'Result is : '+str(key))
l.pack(side=LEFT,fill=BOTH)
s.config(command=l.yview())
root.mainloop()

'''

##########################


# Q2:- In the same tkinter file as created above, create a function to insert items into the dictionary.


'''
from tkinter import *
d={'Rajat':9896,'Ashish':9990,'Param':9593,'Naveen':8453,'Vedant':9846,'Sahil':8595,'Ayush':9512,'Pritam':9568}
def insert():
    k=e1.get()
    v=e2.get()
    d[k]=v
    l.insert(END,k)
    print(d)
    
root=Tk()
e1=Entry(root)
e1.pack()
e2=Entry(root)
e2.pack()
b=Button(root,text="insert",command=insert)
b.pack()
s=Scrollbar(root)
s.pack(side=RIGHT,fill=Y)
l=Listbox(root,yscrollcommand=s.set)
for key in d.values():
    l.insert(END,'Result is : '+str(key))
l.pack(side=LEFT,fill=BOTH)
s.config(command=l.yview())
root.mainloop()

'''


###################
