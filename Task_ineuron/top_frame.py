from tkinter import *
import win32api
from tkinter import messagebox
import os
from tkinter import ttk
from PyPDF2 import PdfFileMerger, PdfFileReader
import webbrowser as wb
from docx import Document
from docxcompose.composer import Composer

from Task_ineuron.bottom_frame import *
from Task_ineuron.mid_frame import *

global doc_files
global doc_paths
doc_files = []
doc_paths = []
top_frame = LabelFrame()
label_top = Label()
drop_list = StringVar()
search_bar = Entry()
b_whole = Button()
b_specific_directory = Button()
refresh = Button()


def top(root):
    top_frame = LabelFrame(root, height=35, width=800, bg="#1EA1A1")
    label_top = Label(top_frame, text="Search and Merge Software", font="Goldplay 18 bold", bg="#1EA1A1", fg="black")
    label_top.pack()
    top_frame.grid(row=0, column=0, sticky="WE")
    # Frame1
    frame_search = LabelFrame(root, text="", height=50, width=800, bg="#1EA1A1", fg="white")
    frame_search.grid(row=1, column=0, sticky="WE")
    frame_search.pack_propagate(0)

    # Dropdown List
    drop_list = StringVar()
    options = [".pdf"]
    drop_list.set(".pdf")
    dropdown = OptionMenu(frame_search, drop_list, *options)
    dropdown.config(bg="#e55c35")

    search_bar = Entry(frame_search, width=50, borderwidth=5)
    search_bar.insert(0, "C:/Users/user/Desktop/Stellwerk")
    clicked = search_bar.bind('<Button-1>', click)

    b_specific_directory = Button(frame_search, bg="bisque", text="Search", padx=15, pady=20,
                                  command=lambda: search_indirectory(search_bar.get()))
    b_whole = Button(frame_search, text="Search My Computer", padx=15, pady=20, bg='#ff6666',
                     command=lambda: search_pc())
    refresh = Button(frame_search, text="Clear All", bg="bisque", padx=20, pady=20, command=clear_all)
    refresh['state'] = DISABLED

    dropdown.grid(row=0, column=0, padx=20)
    search_bar.grid(row=0, column=1, padx=10)
    b_specific_directory.grid(row=0, column=2, padx=3)
    b_whole.grid(row=0, column=3, padx=3)
    refresh.grid(row=0, column=4, padx=3)


def clear_all():
    global doc_paths
    global doc_files
    if (bool(main_frame.winfo_exists())):
        search_bar.delete(0, END)
        doc_files = []
        doc_paths = []
        main_frame.pack_forget()
        my_canvas.pack_forget()
        second_frame.pack_forget()
        b_specific_directory['state'] = NORMAL
        b_whole['state'] = NORMAL
        drop_list.set(".pdf")
        refresh['state'] = DISABLED
        merge_all = Button(frame_bottom, width=10, bg='bisque', padx=15, pady=20, text='Merge all',
                           command=lambda: merge(drop_list.get()))
        merge_all.grid(row=0, column=3, padx=20)

    else:
        messagebox.showinfo("Information", "No data")


def get_drivenames():
    drives = win32api.GetLogicalDriveStrings()
    drives = drives.split('\000')[:-1]
    return drives


def popup():
    messagebox.showerror("Error Occurred", "Invalid Path. Please Input Correct Path")
    clear_all()


def click(event):
    search_bar.configure(state=NORMAL)
    search_bar.delete(0, END)
    search_bar.unbind('<Button-1>', clicked)


def search_indirectory(x):
    """This function will return a list of all the specific type of Files present in a directory"""
    if os.path.exists(x):
        b_specific_directory['state'] = DISABLED
        refresh['state'] = NORMAL
        b_whole['state'] = DISABLED
        for i in os.listdir(x):
            if i.endswith(".pdf"):
                doc_files.append(i)
                doc_paths.append(x + '/' + i)
        if doc_files:
            frame2(doc_files)
        else:
            messagebox.showinfo("Output", "No such file exist")
            frame2(doc_files)
    else:
        popup()


def search_pc():
    b_specific_directory['state'] = DISABLED
    b_whole['state'] = DISABLED
    refresh['state'] = NORMAL
    drives_list = get_drivenames()
    counter = 0
    for i in drives_list:
        for r, d, f in os.walk(i):
            for file in f:
                filepath = os.path.join(r, file)
                if file.endswith(".pdf"):
                    doc_files.append(file)
                    doc_paths.append(filepath)
                    counter += 1
    print(f"Total Files: {counter} files.")
    frame2(doc_files)
