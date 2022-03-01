from tkinter import *
from tkinter import ttk

root= Tk()

#Labels
# mlabel1= Label(root, text= "Hello").pack()
# mlabel2= Label(root, text= "Hello bhaiya").pack()
#mlabel1.grid(row=0, column=2)
#mlabel2.grid(row=1, column=0)

#Buttons
# def myclick():
#     mlabel= Label(root, text= "Clicked")
#     mlabel.pack()
# myButton= Button(root, text="Click Me", padx=50, pady=50, command= myclick, fg= "green", bg= "Yellow").pack()


#Creating Input Field

# e= Entry(root, width= 50, borderwidth= 5, fg= "black", bg="yellow")
# e.insert(0, "Enter your Name:")
# e.pack()
#
# def myclick():
#     hello="Hello "+e.get()
#     mylabel= Label(root, text= hello)
#     mylabel.pack()
#
# mybutton= Button(root, text = "Click Me", command= myclick)
# mybutton.pack()

# Sliders
# def slide_value():
#     my_label= Label(root, text= "Vertical: " + str(vertical.get())).pack()
#     my_label = Label(root, text="Horizontal: " + str(horizon.get())).pack()
#     root.geometry('400x400')
#
# vertical= Scale(root, from_=0, to=100)
# vertical.pack()
#
# horizon= Scale(root, from_=0, to=100, orient= HORIZONTAL)
# horizon.pack()
# my_btn= Button(root, text="Click Me", command=slide_value).pack()

#CHECKBOXES
# var= StringVar()
#
# def check():
#     my_label = Label(root, text=str(var.get())).pack()
#
# c= Checkbutton(root, text="Check this", variable=var, onvalue="ON", offvalue="Off")
# c.deselect()
# c.pack()
#
# my_btn= Button(root, text=" Click me", command=check).pack()

#DROPDOWN MENUS
# def show():
#      my_label = Label(root, text=str(clicked.get())).pack()
#
# options=["Monday", "Tuesday", "Wednesday", "Thursday", 'Friday',"Saturday"]
# clicked= StringVar()
# clicked.set(options[0])
# c=OptionMenu(root, clicked, *options)
#
# my_btn= Button(root, text=" Click me", command=show).pack()
# c.pack()
label = Label(root, text = 'Hello, World!')
print(label['text']) # output is: Hello, World!
root.mainloop()