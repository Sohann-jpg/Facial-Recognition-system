from tkinter import * 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2 
import time
import random

class Student:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        ####Variables####
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_level = StringVar()
        self.var_sID = StringVar()
        self.var_sName = StringVar()
        self.var_gender = StringVar()
        self.var_email = StringVar()
        self.var_pName = StringVar()
        self.var_address = StringVar()
        self.var_pNum = StringVar()
        self.var_radio1 = StringVar()
        # ===== Header and background images =====
        img = Image.open(r"App-Images\Header.jpg")
        img = img.resize((1550, 130), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root, image = self.photoimg)
        f_lbl.place(x= -1, y=0)
        # Adding a background image to the application software
        img1 = Image.open(r"App-Images\Background.webp")
        img1 = img1.resize((1550, 710), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        bg_img = Label(self.root, image = self.photoimg1)
        bg_img.place(x = 0, y = 130, width = 1550, height = 710)
        # Adding a text in the application
        title_lbl = Label(bg_img,text = "Student Details", font = ("open sans", 30), bg = "white", fg = "Black")
        title_lbl.place(x = -100, y = 0, width = 1800, height = 40)


        # ===== Work Frames =====
        #Adding a frame
        main_frame = Frame(bg_img, bd = 2, bg = "white")
        main_frame.place(x = 25, y = 50, width = 1230, height = 480)
        # left label frame
        Left_frame = LabelFrame(main_frame, bd = 2, bg = "white", relief = RAISED, font = ("Sans Serif", 12))
        Left_frame.place(x = 10, y = 10, width = 580, height = 450)
    
        # Right label frame
        Right_frame = LabelFrame(main_frame, bd = 2, bg = "white", relief = RAISED, text = "Student Details", font = ("Sans Serif", 12))
        Right_frame.place(x = 630, y = 10, width = 580, height = 450)

        #=====Search Frame=====
        search_frame = LabelFrame(Left_frame, bd = 2, bg = "white", relief = RIDGE, text = "Search", font = ("Sans Serif", 12))
        search_frame.place(x = 5, y = 10, width = 565, height = 70)
        search_label = Label(search_frame, text = "Search By: ", font = ("Sans Serif", 12), bg = "white")
        search_label.grid(row = 0, column = 0, padx = 5,  sticky = W)
        # Entry Fields
        search_entry = ttk.Entry(search_frame, width = 15, font = ("Sans Serif", 12))
        search_entry.grid(row = 0, column = 2, pady = 10, sticky = W)

        # Buttons
        searchbtn = Button(search_frame, text = "Search", width = 15, font = ("Sans Serif", 12), bg = "aqua", fg = "black")
        searchbtn.grid(row = 0, column = 3, padx = 2)

        # ===== Table Frame ====
        table_frame = Frame(Right_frame, bd = 2, bg = "white", relief = RIDGE)
        table_frame.place(x = 5, y = 10, width = 565, height = 400)

        # ===== Scroll bar =====
        Scroll_x = ttk.Scrollbar(table_frame, orient = HORIZONTAL)
        Scroll_y = ttk.Scrollbar(table_frame, orient = VERTICAL)
        # ===== Scroll bar =====

        # ===== Table Contents =====
        self.student_table = ttk.Treeview(table_frame, column = ("Student ID", "Name", "Course"), xscrollcommand = Scroll_x.set, yscrollcommand = Scroll_y.set)
        Scroll_x.pack(side = BOTTOM, fill = X)
        Scroll_y.pack(side = RIGHT, fill = Y)
        Scroll_x.config(command = self.student_table.xview)
        Scroll_y.config(command = self.student_table.yview)
        self.student_table.heading("Student ID", text = "Student ID")
        self.student_table.heading("Name", text = "Name")
        self.student_table.heading("Course", text = "Course")
        self.student_table["show"] = "headings"

        self.student_table.column("Student ID", width = 100)
        self.student_table.column("Name", width = 100)
        self.student_table.column("Course", width = 100)
        self.student_table.pack(fill = BOTH, expand = 1)
        self.student_table.bind("<ButtonRelease>")
        # ===== Table Contents =====

    def search_records(self):
        pass

if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
