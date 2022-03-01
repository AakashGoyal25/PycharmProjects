from tkinter import *
import win32api
from tkinter import messagebox
import os
from tkinter import ttk
from PyPDF2 import PdfFileMerger, PdfFileReader
from Task_ineuron.top_frame import *
import webbrowser as wb
from docx import Document
from docxcompose.composer import Composer
frame_bottom= LabelFrame()
dest_label=Label()
dest_bar=Entry()

def bottom(root):

    frame_bottom = LabelFrame(root, text="", height=50, width=800, bg="#1EA1A1", padx=15, pady=15)
    frame_bottom.grid(row=3, column=0, sticky="WE")
    frame_bottom.pack_propagate(0)

    dest_Label = Label(frame_bottom, text="Destination Folder:", padx=10, width=15, bg="#1EA1A1")

    dest_bar = Entry(frame_bottom, width=50, borderwidth=5)
    dest_bar.insert(0, "C:/Users/user/Desktop/Stellwerk")
    clicked_dest = dest_bar.bind('<Button-1>', dest_clicked)

    merge_all = Button(frame_bottom, width=10, bg='bisque', padx=15, pady=20, text='Merge all',
                       command=lambda: merge(drop_list.get()))
    close = Button(frame_bottom, text="Close", padx=20, pady=20, bg='#ff6666', command=root.destroy)

    dest_Label.grid(row=0, column=1)
    merge_all.grid(row=0, column=3, padx=20)
    close.grid(row=0, column=4, padx=20, sticky="E")
    dest_bar.grid(row=0, column=2, padx=10)

def dest_clicked(event):
    dest_bar.configure(state=NORMAL)
    dest_bar.delete(0, END)
    dest_bar.unbind('<Button-1>', clicked_dest)

def merge(ext):
    path_d= dest_bar.get().replace(str('\\'), "/") + "/" +"mergedfilesoutput.pdf"
    if len(dest_bar.get())!=0:
        if doc_files:
            if(ext=='.pdf'):
                mergedObject = PdfFileMerger()
                print(doc_paths)
                for i in doc_paths:
                    print(i)
                    mergedObject.append(PdfFileReader(i, 'rb'))
                mergedObject.write(path_d)
                open = Button(frame_bottom, width=10, bg='bisque', padx=15, pady=20, text='Open file', command=lambda: open_file(path_d))
                open.grid(row=0, column=3, padx=20)
                print(doc_paths)
            else:
                messagebox.showerror("Error", "Error Occurred")
        else:
            messagebox.showerror("Error", "No files")
    else:
        messagebox.showerror("Error", "Please put destination path")