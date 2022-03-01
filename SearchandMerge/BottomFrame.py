from tkinter import *
import win32api
from tkinter import messagebox
import os
from tkinter import ttk
from PyPDF2 import PdfFileMerger, PdfFileReader
from docx import Document
from docxcompose.composer import Composer

from SearchandMerge.TopFrame import TopFrame as tf

class BottomFrame:
    def __init__(self, root):
        self.root=root
        # FRAME3
        self.frame_bottom = LabelFrame(self.root, text="", height=50, width=800, bg="#C6B4EF", padx=15, pady=15)
        self.frame_bottom.grid(row=3, column=0, sticky="WE")
        self.frame_bottom.pack_propagate(0)
        self.dest_Label = Label(self.frame_bottom, text="Destination Folder:", padx=10, width=15, bg="#C6B4EF")
        self.dest_bar = Entry(self.frame_bottom, width=50, borderwidth=5)
        self.dest_bar.insert(0, "C:/Users/user/Desktop/Stellwerk")
        self.clicked_dest = self.dest_bar.bind('<Button-1>', self.dest_clicked)

        self.merge_all = Button(self.frame_bottom, width=10, bg='#ff6666', padx=15, pady=20, text='Merge all',
                           command=lambda: self.merge(tf.drop_list.get()))
        self.close = Button(self.frame_bottom, text="Close", padx=20, pady=20, bg='#ff6666', command=root.destroy)

        self.dest_Label.grid(row=0, column=1)
        self.merge_all.grid(row=0, column=3, padx=20)
        self.close.grid(row=0, column=4, padx=20, sticky="E")
        self.dest_bar.grid(row=0, column=2, padx=10)

    def dest_clicked(self,event):
        self.dest_bar.configure(state=NORMAL)
        self.dest_bar.delete(0, END)
        self.dest_bar.unbind('<Button-1>', self.clicked_dest)

    def merge(self, ext):
        if len(tf.dest_bar.get()) != 0:
            if tf.doc_files:
                if (ext == '.pdf'):
                    self.mergedObject = PdfFileMerger()
                    print(tf.doc_paths)
                    for i in tf.doc_paths:
                        print(i)
                        self.mergedObject.append(PdfFileReader(i, 'rb'))
                    self.mergedObject.write(self.dest_bar.get().replace(str('\\'), "/") + "/" + "mergedfilesoutput.pdf")
                    print(tf.doc_paths)

                elif (ext == '.docx'):
                    print(tf.doc_paths[0])
                    self.composed = self.dest_bar.get().replace(str('\\'), "/") + "/" + "mergedfilesoutput.docx"
                    self.result = Document(tf.doc_paths[0])
                    self.result.add_page_break()
                    self.composer = Composer(self.result)
                    print(tf.doc_files)
                    print(tf.doc_paths)
                    for i in range(1, len(tf.doc_paths)):
                        self.doc = Document(tf.doc_paths[i])
                        if i != len(tf.doc_paths) - 1:
                            self.doc.add_page_break()
                        self.composer.append(self.doc)
                    self.composer.save(self.composed)
                elif (ext == '.txt'):
                    self.output = self.dest_bar.get().replace(str('\\'), "/") + "/" + "mergedfilesoutput.txt"
                    self.f1 = open(self.output, "wb")
                    for i in tf.doc_paths:
                        self.f = open(i, "rb")
                        self.f1.write(self.f.read())
                        self.f1.write(b"\n")
                        self.f.close()
                    self.f1.close()
                else:
                    messagebox.showerror("Error", "Error Occurred")
            else:
                messagebox.showerror("Error", "No files")
        else:
            messagebox.showerror("Error", "Please put destination path")