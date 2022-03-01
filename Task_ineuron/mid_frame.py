from tkinter import *
from tkinter import ttk

main_frame = Frame()
frame_mid = LabelFrame()
my_canvas= Canvas()
second_frame=Frame()

def mid(root):
    frame_mid = LabelFrame(root, text="", height=300, width=800, bg="#1EA1A1", padx=15, pady=15)
    frame_mid.grid(row=2, column=0)
    frame_mid.pack_propagate(0)

def frame2(files):
    main_frame = Frame(frame_mid,bg="lightgrey")
    main_frame.pack(fill=BOTH, expand=1)

    # Create a Canvas
    my_canvas = Canvas(main_frame,bg="lightgrey")
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)

    # configure the canvas
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

    # Another frame inside Canvas
    second_frame = Frame(my_canvas, bg="lightgrey")

    # Add that new frame to a window in the canvas
    my_canvas.create_window((0, 0), window=second_frame, anchor="nw")
    for thing in range(len(files)):
        Label(second_frame, text=f'{thing+1}. {files[thing]}', font='Helvetica 12 bold').grid(row=thing, column=0, pady=3, sticky=W)
