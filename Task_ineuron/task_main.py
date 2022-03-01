from tkinter import *
import win32api
from tkinter import messagebox
import os
from tkinter import ttk
from PyPDF2 import PdfFileMerger, PdfFileReader
import webbrowser as wb
from docx import Document
from docxcompose.composer import Composer

root = Tk()
root.title("Merge Inc.")
root.geometry("800x500")
root.resizable(False,False)

global doc_files
global doc_paths
doc_files=[]
doc_paths=[]

global b_specific_directory
def dest_clicked(event):
    dest_bar.configure(state=NORMAL)
    dest_bar.delete(0, END)
    dest_bar.unbind('<Button-1>', clicked_dest)

def click(event):
       search_bar.configure(state=NORMAL)
       search_bar.delete(0, END)
       search_bar.unbind('<Button-1>', clicked)


def get_drivenames():
    drives = win32api.GetLogicalDriveStrings()
    drives = drives.split('\000')[:-1]
    return drives

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


def frame2(files):
    # CreateA Main Frame
    global main_frame
    main_frame = Frame(frame_mid,bg="lightgrey")
    main_frame.pack(fill=BOTH, expand=1)

    # Create a Canvas
    global my_canvas
    my_canvas = Canvas(main_frame,bg="lightgrey")
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)

    # configure the canvas
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

    # Another frame inside Canvas
    global second_frame
    second_frame = Frame(my_canvas, bg="lightgrey")

    # Add that new frame to a window in the canvas
    my_canvas.create_window((0, 0), window=second_frame, anchor="nw")
    for thing in range(len(files)):
        Label(second_frame, text=f'{thing+1}. {files[thing]}', font='Helvetica 12 bold').grid(row=thing, column=0, pady=3, sticky=W)

def popup():
    messagebox.showerror("Error Occurred", "Invalid Path. Please Input Correct Path")
    clear_all()

def search_indirectory(x):
    """This function will return a list of all the specific type of Files present in a directory"""
    if os.path.exists(x):
        b_specific_directory['state']= DISABLED
        refresh['state']= NORMAL
        b_whole['state']=DISABLED
        for i in os.listdir(x):
            if i.endswith(".pdf"):
                doc_files.append(i)
                doc_paths.append(x+'/'+i)
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

def open_file(path_file):
    wb.open_new(path_file)

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

#Label
top_frame = LabelFrame(root, height=35, width=800, bg="#1EA1A1")
label_top= Label(top_frame, text="Search and Merge Software", font="Goldplay 18 bold", bg="#1EA1A1", fg="black")
label_top.pack()
top_frame.grid(row=0, column=0, sticky="WE")
#Frame1
frame_search = LabelFrame(root, text="", height=50, width=800, bg="#1EA1A1", fg="white")
frame_search.grid(row=1, column=0, sticky="WE")
frame_search.pack_propagate(0)

#Dropdown List
drop_list= StringVar()
options= [".pdf"]
drop_list.set(".pdf")
dropdown= OptionMenu(frame_search, drop_list, *options)
dropdown.config(bg="#e55c35")

global search_bar
search_bar = Entry(frame_search, width=50, borderwidth=5)
search_bar.insert(0, "C:/Users/user/Desktop/Stellwerk")
clicked = search_bar.bind('<Button-1>', click)

global b_specific_directory
b_specific_directory= Button(frame_search, bg="bisque", text="Search", padx=15, pady=20, command=lambda: search_indirectory(search_bar.get()))
global b_whole
b_whole = Button(frame_search, text="Search My Computer", padx=15, pady=20, bg='#ff6666',command=lambda: search_pc())
refresh = Button(frame_search, text="Clear All",bg="bisque", padx=20, pady=20,command= clear_all)
refresh['state'] = DISABLED

dropdown.grid(row=0, column=0, padx=20)
search_bar.grid(row=0, column=1, padx=10)
b_specific_directory.grid(row=0, column=2, padx=3)
b_whole.grid(row=0, column=3, padx=3)
refresh.grid(row=0, column=4, padx=3)

# Constructing the second frame, FRAME2
global frame_mid
frame_mid = LabelFrame(root, text="", height=300, width=800, bg="#1EA1A1", padx=15, pady=15)
frame_mid.grid(row=2, column=0)
frame_mid.pack_propagate(0)

# FRAME3
global frame_bottom
frame_bottom = LabelFrame(root, text="", height=50, width=800, bg="#1EA1A1", padx=15, pady=15)
frame_bottom.grid(row=3, column=0, sticky="WE")
frame_bottom.pack_propagate(0)

dest_Label = Label(frame_bottom, text="Destination Folder:", padx=10, width=15, bg="#1EA1A1")
global dest_bar
dest_bar = Entry(frame_bottom, width=50, borderwidth=5)
dest_bar.insert(0, "C:/Users/user/Desktop/Stellwerk")
clicked_dest = dest_bar.bind('<Button-1>', dest_clicked)

merge_all = Button(frame_bottom, width=10, bg='bisque', padx=15, pady=20, text='Merge all', command=lambda: merge(drop_list.get()))
close = Button(frame_bottom, text="Close", padx=20, pady=20, bg='#ff6666', command=root.destroy)

dest_Label.grid(row=0, column=1)
merge_all.grid(row=0, column=3, padx=20)
close.grid(row=0, column=4, padx=20, sticky="E")
dest_bar.grid(row=0, column=2, padx=10)
root.mainloop()
