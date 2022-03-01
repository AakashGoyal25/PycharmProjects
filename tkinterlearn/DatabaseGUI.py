import sqlite3
from tkinter import *
import os
from PIL import ImageTk, Image

root=Tk()
root.geometry("330x300")
img_bg = PhotoImage(file="C:/Users/user/Desktop/bg_db.png")
label_bg = Label(root,image=img_bg)
label_bg.place(x=0, y=0)

def creation():
    conn = sqlite3.connect("DatabaseGui.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE address 
           (first_name text,
           last_name text,
           address text, 
           city text,
           zipcode integer
           )""")
    conn.commit()
    conn.close()

def submit():
    conn= sqlite3.connect("DatabaseGui.db")
    c=conn.cursor()
    c.execute("INSERT INTO address VALUES(:f_name, :last_name, :address, :pincode, :city )",
                {
                    'f_name': f_entry.get(),
                    'last_name': l_entry.get(),
                    'address': address_entry.get(),
                    'pincode': pincode_entry.get(),
                    'city':city_entry.get()
                 })
    conn.commit()
    conn.close()

    f_entry.delete(0, END)
    l_entry.delete(0, END)
    address_entry.delete(0, END)
    pincode_entry.delete(0, END)
    city_entry.delete(0, END)

def show():
    global oid_entry
    f_entry.delete(0, END)
    l_entry.delete(0, END)
    address_entry.delete(0, END)
    pincode_entry.delete(0, END)
    city_entry.delete(0, END)
    oid_entry.delete(0, END)
    conn = sqlite3.connect("DatabaseGui.db")
    c = conn.cursor()
    c.execute(" SELECT *, oid FROM address")
    record =c.fetchall()
    print(record)

    for i, j in enumerate(record):
        print(j[5])
        f_entry.insert(0,j[0])
        l_entry.insert(0,j[1])
        address_entry.insert(0,j[2])
        pincode_entry.insert(0,j[3])
        city_entry.insert(0,j[4])
        oid_entry.insert(0,j[5])
        show_btn = Button(root, text="Show", command=show, bg='Green')


    conn.commit()
    conn.close()

def update():
    global oid_entry
    global f_entry
    global l_entry
    global address_entry
    global pincode_entry
    global city_entry
    global f_entry_up
    global l_entry_up
    global address_entry_up
    global pincode_entry_up
    global city_entry_up
    global top

    top= Toplevel()
    label_bg = Label(top, image=img_bg)
    label_bg.place(x=0, y=0)
    top.title("Update Record")
    f_label_up = Label(top, text=" First Name: ")
    f_label_up.grid(row=0, column=0)
    l_label_up = Label(top, text=" Last Name: ")
    l_label_up.grid(row=1, column=0)
    address_label_up = Label(top, text=" Address: ")
    address_label_up.grid(row=2, column=0)
    pincode_label_up = Label(top, text=" Pincode: ")
    pincode_label_up.grid(row=3, column=0)
    city_label_up = Label(top, text=" City: ")
    city_label_up.grid(row=4, column=0)

    # Entry(TextBox)
    f_entry_up = Entry(top, width=40)
    f_entry_up.grid(row=0, column=1)
    l_entry_up = Entry(top, width=40)
    l_entry_up.grid(row=1, column=1)
    address_entry_up = Entry(top, width=40)
    address_entry_up.grid(row=2, column=1)
    pincode_entry_up = Entry(top, width=40)
    pincode_entry_up.grid(row=3, column=1)
    city_entry_up = Entry(top, width=40)
    city_entry_up.grid(row=4, column=1)
    top.geometry('350x300')
    f_entry_up.insert(0, f_entry.get())
    l_entry_up.insert(0, l_entry.get())
    address_entry_up.insert(0, address_entry.get())
    pincode_entry_up.insert(0, pincode_entry.get())
    city_entry_up.insert(0, city_entry.get())

    save_btn= Button(top, text="Save Record", command= lambda : save(top, oid_entry.get()), bg='yellow').grid(row=5, column=0, columnspan=2, padx=5,
                                                                               pady=5, ipadx=136)
    f_entry.delete(0, END)
    l_entry.delete(0, END)
    address_entry.delete(0, END)
    pincode_entry.delete(0, END)
    city_entry.delete(0, END)
    # oid_entry.delete(0, END)

def save(top_inher,id):
    global oid_entry
    global f_entry
    global l_entry
    global address_entry
    global pincode_entry
    global city_entry
    global f_entry_up
    global l_entry_up
    global address_entry_up
    global pincode_entry_up
    global city_entry_up
    # oid_entry1=id
    conn = sqlite3.connect("DatabaseGui.db")
    c = conn.cursor()

    # for i, j in enumerate(record):
    # print(j[5])

    c.execute("""UPDATE address SET
            first_name = :f_name,
            last_name = :last_name,
            address = :address ,
            city = :city,
            zipcode = :pincode

            WHERE oid= :oid""",
              {
                  'f_name': f_entry_up.get(),
                  'last_name': l_entry_up.get(),
                  'address': address_entry_up.get(),
                  'city': city_entry_up.get(),
                  'pincode': pincode_entry_up.get(),
                  'oid': oid_entry.get()
              })
    # //record =c.fetchall()
    # //print(record)
    conn.commit()
    conn.close()
    top_inher.destroy()


#Labels
f_label = Label(root, text=" First Name: ")
f_label.grid(row=0, column=0)
l_label = Label(root, text=" Last Name: ")
l_label.grid(row=1, column=0)
address_label = Label(root, text=" Address: ")
address_label.grid(row=2, column=0)
pincode_label = Label(root, text=" Pincode: ")
pincode_label.grid(row=3, column=0)
city_label = Label(root, text=" City: ")
city_label.grid(row=4, column=0)

#Entry(TextBox)
f_entry = Entry(root, width=40)
f_entry.grid(row=0, column=1)
l_entry = Entry(root, width=40)
l_entry.grid(row=1, column=1)
address_entry = Entry(root, width=40)
address_entry.grid(row=2, column=1)
pincode_entry =  Entry(root, width=40)
pincode_entry.grid(row=3, column=1)
city_entry =  Entry(root, width=40)
city_entry.grid(row=4, column=1)

submit_btn=Button(root, text="Submit", command=submit,  bg= 'Green').grid(row= 5, column=0, columnspan=2,padx=5, pady=5, ipadx=135)
show_btn=Button(root, text="Show", command=show,  bg= 'Green').grid(row= 6, column=0, columnspan=2,padx=5, pady=5, ipadx=140)
update_btn=Button(root, text="Update", command=update,  bg= 'Yellow').grid(row= 7, column=0, columnspan=2,padx=5, pady=5, ipadx=136)
oid_entry= Entry(root, width=40)
oid_entry.grid(row=8, column=1)


root.mainloop()

