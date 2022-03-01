from tkinter import *
import win32api
from tkinter import messagebox
import os
from SearchandMerge.MidFrame import MidFrame as md

class TopFrame:

    def __init__(self, root ):
        self.root = root
        self.top_frame = LabelFrame(self.root, height=35, width=800, bg="#C6B4EF")
        self.label_top = Label(self.top_frame, text="Search and Merge Software", font="Goldplay 18 bold", bg="#C6B4EF")
        self.label_top.pack()
        self.top_frame.grid(row=0, column=0, sticky="WE")
        # Frame1
        self.frame_search = LabelFrame(self.root, text="", height=50, width=800, bg="#C6B4EF", fg="white")
        self.frame_search.grid(row=1, column=0, sticky="WE")
        self.frame_search.pack_propagate(0)
        self.doc_files = []
        self.doc_paths = []
        self.counter = 0
        # Dropdown List
        self.drop_list = StringVar()
        self.options = [".docx", ".pdf", ".txt", ".xlsx", ".exe", ".mp4", ".f"]
        self.drop_list.set(".docx")
        self.dropdown = OptionMenu(self.frame_search, self.drop_list, *self.options)
        self.dropdown.config(bg="#e55c35")

        self.search_bar = Entry(self.frame_search, width=50, borderwidth=5)
        self.search_bar.insert(0, "C:/Users/user/Desktop/Stellwerk")
        self.clicked = self.search_bar.bind('<Button-1>', self.click)

        #global b_specific_directory
        self.b_specific_directory = Button(self.frame_search, bg="#54FFCE", text="Search", padx=15, pady=20,
                                      command=lambda: self.search_indirectory(self.search_bar.get()))
        #global b_whole
        self.b_whole = Button(self.frame_search, text="Search My Computer", padx=15, pady=20, bg='#ff6666',
                             command=lambda: self.search_pc())
        self.refresh = Button(self.frame_search, text="Clear All", bg="#54FFCE", padx=20, pady=20, command= self.clear_all)
        self.refresh['state'] = DISABLED

        self.dropdown.grid(row=0, column=0, padx=20)
        self.search_bar.grid(row=0, column=1, padx=10)
        self.b_specific_directory.grid(row=0, column=2, padx=3)
        self.b_whole.grid(row=0, column=3, padx=3)
        self.refresh.grid(row=0, column=4, padx=3)

    def popup(self):
        messagebox.showerror("Error Occurred", "Invalid Path. Please Input Correct Path")
        self.clear_all()


    def click(self, event):
        self.search_bar.configure(state=NORMAL)
        self.search_bar.delete(0, END)
        self.search_bar.unbind('<Button-1>', self.clicked)

    def clear_all(self):

        if (bool(md.main_frame.winfo_exists())):
            self.search_bar.delete(0, END)
            self.doc_files = []
            self.doc_paths = []
            md.main_frame.pack_forget()
            md.my_canvas.pack_forget()
            md.second_frame.pack_forget()
            self.b_specific_directory['state'] = NORMAL
            self.b_whole['state'] = NORMAL
            self.drop_list.set(".docx")
            self.refresh['state'] = DISABLED

        else:
            messagebox.showinfo("Information", "No data")

    def get_drivenames(self):
        self.drives = win32api.GetLogicalDriveStrings()
        self.drives = self.drives.split('\000')[:-1]
        return self.drives

    def search_indirectory(self, x):
        """This function will return a list of all the specific type of Files present in a directory"""
        if os.path.exists(x):
            self.b_specific_directory['state'] = DISABLED
            self.refresh['state'] = NORMAL
            self.b_whole['state'] = DISABLED
            for i in os.listdir(x):
                if i.endswith(self.drop_list.get()):
                    self.doc_files.append(i)

                    self.doc_paths.append(x + '/' + i)
                    print(self.doc_files, " ", self.doc_paths)
            if self.doc_files:
                print("2")
                md.frame2(self.root, len(self.doc_files))
            else:
                messagebox.showinfo("Output", "No such file exist")
                md.frame2(self.doc_files)
        else:
            self.popup()

    def search_pc(self):
        self.b_specific_directory['state'] = DISABLED
        self.b_whole['state'] = DISABLED
        self.refresh['state'] = NORMAL

        for i in self.get_drivenames():
            for r, d, f in os.walk(i):
                for file in f:
                    filepath = os.path.join(r, file)
                    if file.endswith(self.drop_list.get()):
                        self.doc_files.append(file)
                        self.doc_paths.append(filepath)
                        self.counter += 1
        print(f"Total Files: {self.counter} files.")
        md.frame2(self.doc_files)


