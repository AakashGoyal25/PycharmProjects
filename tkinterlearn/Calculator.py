from tkinter import *
root = Tk()

def myclick(number):
    f= e.get() + str(number)
    e.delete(0, END)
    e.insert(0, f)

def add_button():
    global first_num
    first_num = int(e.get())
    e.delete(0, END)
    global operation
    operation = 'add'

def sub_button():
    global first_num
    first_num = int(e.get())
    e.delete(0, END)
    global operation
    operation = 'sub'

def mul_button():
    global first_num
    first_num = int(e.get())
    e.delete(0, END)
    global operation
    operation = 'mul'

def div_button():
    global first_num
    first_num = int(e.get())
    e.delete(0, END)
    global operation
    operation = 'div'

def equal_button():
    second_num= int(e.get())
    e.delete(0, END)
    global first_num
    if operation=='add':
        e.insert(0, str(first_num  + second_num))

    elif operation=='sub':
        e.insert(0, str(first_num - second_num))

    elif operation=='mul':
        e.insert(0, str(first_num * second_num))

    elif operation=='div':
        e.insert(0, str(first_num / second_num))



e= Entry(root, width=42, borderwidth=2)
e.grid(row=0, column= 0, columnspan= 3, padx=5, pady=5)

myButton1 = Button(root, text='1', padx=40, pady=15, command= lambda : myclick(1))
myButton2 = Button(root, text='2', padx=40, pady=15, command= lambda : myclick(2))
myButton3 = Button(root, text='3', padx=40, pady=15, command= lambda : myclick(3))
myButton4 = Button(root, text='4', padx=40, pady=15, command= lambda : myclick(4))
myButton5 = Button(root, text='5', padx=40, pady=15, command= lambda : myclick(5))
myButton6 = Button(root, text='6', padx=40, pady=15, command= lambda : myclick(6))
myButton7 = Button(root, text='7', padx=40, pady=15, command= lambda : myclick(7))
myButton8 = Button(root, text='8', padx=40, pady=15, command= lambda : myclick(8))
myButton9 = Button(root, text='9', padx=40, pady=15, command= lambda : myclick(9))
myButton0 = Button(root, text='0', padx=40, pady=15, command= lambda : myclick(0))
myButton_clear = Button(root, text='Clear', padx=77, pady=15, command= lambda: e.delete(0, END))
myButton_add = Button(root, text='+', padx=39, pady=15, command= add_button)
myButton_sub = Button(root, text='-', padx=40, pady=15, command= sub_button)
myButton_div = Button(root, text='/', padx=40, pady=15, command= div_button)
myButton_mul = Button(root, text='*', padx=40, pady=15, command= mul_button)
myButton_equals= Button(root, text='=', padx=86, pady=15, command= equal_button)

myButton9.grid(row=1, column=2)
myButton8.grid(row=1, column=1)
myButton7.grid(row=1, column=0)
myButton6.grid(row=2, column=2)
myButton5.grid(row=2, column=1)
myButton4.grid(row=2, column=0)
myButton3.grid(row=3, column=2)
myButton2.grid(row=3, column=1)
myButton1.grid(row=3, column=0)
myButton0.grid(row=4, column=0)
myButton_clear.grid(row=4, column= 1, columnspan=2)
myButton_equals.grid(row=5, column= 1, columnspan=2)
myButton_add.grid(row=5, column= 0)
myButton_sub.grid(row=6, column= 0)
myButton_mul.grid(row=6, column= 1)
myButton_div.grid(row=6, column= 2)


root.mainloop()