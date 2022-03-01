from tkinter import *
import os
from PIL import ImageTk, Image

root = Tk()
root.title("Image Viewer")
root.iconbitmap("C:/Users/user/Downloads/Aka ico/aka.ico")

l=[]
for i in os.listdir('C:/Users/user/Desktop/Mpics'):
   l.append('C:/Users/user/Desktop/Mpics/'+i)
print(l)

curr=0
status= Label(root, text= "Image "+ str(curr+1) +" of "+ str(len(l)), bd=1, relief= SUNKEN)
my_img = ImageTk.PhotoImage(Image.open(l[curr]))
my_label = Label(root, image= my_img)
my_label.grid(row=0, column=0, columnspan=3)

def back(x):
    global my_label
    global button_back
    global button_for
    global my_img
    global curr
    curr=x
    my_label.grid_forget()

    my_img = ImageTk.PhotoImage(Image.open(l[curr]))
    my_label = Label(image=my_img)
    my_label.grid(row=0, column=0, columnspan=3)
    button_back = Button(root, text='<<', command=lambda: back(curr - 1))
    button_back.grid(row=1, column=0)
    button_for = Button(root, text='>>', command=lambda: forward(curr + 1))
    button_for.grid(row=1, column=2)
    if curr == 0:
        button_back = Button(root, text="<<", state= DISABLED)
        button_back.grid(row=1, column=0)

    status= Label(root, text= "Image "+ str(curr+1) +" of "+ str(len(l)), bd=1, relief= SUNKEN)
    status.grid(row=2, column=0, columnspan=3, sticky= W+E)

def forward(x):
    global my_label
    global button_back
    global button_for
    global my_img
    global curr
    curr=x
    my_label.grid_forget()

    my_img = ImageTk.PhotoImage(Image.open(l[curr]))
    my_label= Label(image= my_img)
    my_label.grid(row=0, column=0, columnspan=3)
    button_for= Button(root, text='>>', command= lambda: forward(curr+1))
    button_for.grid(row=1, column=2)
    button_back = Button(root, text='<<', command=lambda: back(curr - 1))
    button_back.grid(row=1, column=0)

    if x==len(l)-1:
        button_for = Button(root, text=">>", state=DISABLED)
        button_for.grid(row=1, column=2)

    status= Label(root, text= "Image "+ str(curr+1) +" of "+ str(len(l)), bd=1, relief= SUNKEN)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)

button_back= Button(root, text='<<', command= back, state=DISABLED)
button_exit= Button(root, text='Quit', command= root.quit)
button_for= Button(root, text='>>', command= lambda: forward(1))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_for.grid(row=1, column=2)
status.grid(row=2, column=0, columnspan=3, sticky=W + E)
root.mainloop()