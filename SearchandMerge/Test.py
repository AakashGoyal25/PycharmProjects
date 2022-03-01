#pyinstall Test.py
from tkinter import *
import win32api
from tkinter import messagebox
import os
from tkinter import ttk
from PyPDF2 import PdfFileMerger, PdfFileReader
from docx import Document
from docxcompose.composer import Composer
from TopFrame import TopFrame
from BottomFrame import BottomFrame
from MidFrame import MidFrame

global doc_files
global doc_paths
doc_files=[]
doc_paths=[]

global b_specific_directory

#Label

class AppGui:
    def __init__(self, root):
        self.root = root
        self.root.title("Merge Inc.")
        self.root.geometry("800x500")
        self.root.resizable(False, False)
        self.top_frame = TopFrame(self.root)
        self.mid_frame = MidFrame(self.root)
        self.bottom_frame = BottomFrame(self.root)


def main(): #run mianloop
    root = Tk()
    app = AppGui(root)
    root.mainloop()

if __name__ == '__main__':
    main()