from Task_ineuron.bottom_frame import *
from Task_ineuron.top_frame import *
from Task_ineuron.mid_frame import *

from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Merge Inc.")
root.geometry("800x500")
root.resizable(False, False)


# def open_file(path_file):
#     wb.open_new(path_file)


top(root)
mid(root)
bottom(root)
root.mainloop()
