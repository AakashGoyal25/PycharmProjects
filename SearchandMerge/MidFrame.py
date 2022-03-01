from tkinter import *
from tkinter import ttk
from SearchandMerge.TopFrame import TopFrame as tf

class MidFrame:

    def __init__(self, root):
        self.root=root
        # Constructing the second frame, FRAME2
        self.frame_mid = LabelFrame(self.root, text="", height=300, width=800, bg="#C6B4EF", padx=15, pady=15)
        self.frame_mid.grid(row=2, column=0)
        self.frame_mid.pack_propagate(0)
        self.main_frame = Frame(self.frame_mid, bg="lightgrey")

        self.my_canvas = Canvas(self.main_frame, bg="lightgrey")
        self.my_scrollbar = ttk.Scrollbar(self.main_frame, orient=VERTICAL, command=self.my_canvas.yview)
        self.second_frame = Frame(self.my_canvas, bg="lightgrey")

    def frame2(self, files):

        # Create a Canvas
        self.main_frame.pack(fill=BOTH, expand=1)
        self.my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
        self.my_scrollbar.pack(side=RIGHT, fill=Y)

        # configure the canvas
        self.my_canvas.configure(yscrollcommand=self.my_scrollbar.set)
        self.my_canvas.bind('<Configure>', lambda e: self.my_canvas.configure(scrollregion=self.my_canvas.bbox("all")))

        # Another frame inside Canvas


        # Add that new frame to a window in the canvas
        self.my_canvas.create_window((0, 0), window=self.second_frame, anchor="nw")
        for thing in range(files):
            Label(self.second_frame, text=f'{thing + 1}. {tf.doc_files[thing]}', font='Helvetica 12 bold').grid(row=thing,
                                                                                                        column=0,
                                                                                                        pady=3,
                                                                                                        sticky=W)
