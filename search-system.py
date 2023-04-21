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

        # back_button = Button(bg_img, text = "Back", font = ("Helvetica", 10), bd = 2, relief = RIDGE, width = 13, bg = "#117c9d", fg = "black")
        # back_button.place(x = 1010, y = 0, width = 120, height = 40)
        # ===== Header and background images =====
        # Right label frame
        Right_frame = LabelFrame(self.root, bd = 2, bg = "white", relief = RAISED, text = "Student Details", font = ("Sans Serif", 12))
        Right_frame.place(x = 0, y = 175, width = 1540, height = 655)

        #=====Search Frame=====
        search_frame = LabelFrame(Right_frame, bd = 2, bg = "white", relief = RIDGE, text = "Search", font = ("Sans Serif", 12))
        search_frame.place(x = 5, y = 10, width = 1520, height = 70)
        search_label = Label(search_frame, text = "Search By: ", font = ("Sans Serif", 12), bg = "white")
        search_label.grid(row = 0, column = 0, padx = 5,  sticky = W)

        # Combo Boxes
        search_combo = ttk.Combobox(search_frame, font = ("Sans Serif", 12), state = "readonly", width = 10)
        search_combo["values"] = ("Select", "Name", "ID", "Email")
        search_combo.current(0)
        search_combo.grid(row = 0, column = 1, padx = 2, pady = 5, sticky = W)

        # Entry Fields
        search_entry = ttk.Entry(search_frame, width = 15, font = ("Sans Serif", 12))
        search_entry.grid(row = 0, column = 3, pady = 5, sticky = W)

        # Buttons
        searchbtn = Button(search_frame, text = "Search", width = 10, font = ("Sans Serif", 12), bg = "aqua", fg = "black")
        searchbtn.grid(row = 0, column = 4, padx = 2)
        showallbtn = Button(search_frame, text = "Show All", width = 10, font = ("Sans Serif", 12), bg = "aqua", fg = "black")
        showallbtn.grid(row = 0, column = 5, padx = 2)

if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
