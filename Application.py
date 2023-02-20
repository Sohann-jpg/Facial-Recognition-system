import tkinter as tk
from tkinter import ttk
from tkinter import * 
import tkinter
from PIL import Image,ImageTk
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
import mysql.connector
import cv2 
from tkinter import messagebox
import numpy as np
import os
import csv
from tkinter import filedialog
from time import strftime
from datetime import datetime

class Main(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # Add the widgets for the Student page here
        # ===== Header and background images =====
        # Adding a header image to the application software
        img = Image.open(r"App-Images\Header.jpg")
        img = img.resize((1300, 130), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = tk.Label(self, image = self.photoimg)
        f_lbl.place(x= -1, y=0)
        # Adding a background image to the application software
        img1 = Image.open(r"App-Images\Background.webp")
        img1 = img1.resize((1530, 710), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        bg_img = tk.Label(self, image = self.photoimg1)
        bg_img.place(x = 0, y = 130, width = 1530, height = 710)
        # Adding a text in the application
        title_lbl = tk.Label(bg_img,text = "Hello there! Welcome", font = ("open sans", 30), 
        bg = "white", fg = "Black")
        title_lbl.place(x = -100, y = 0, width = 1530, height = 40)
        # ===== Header and background images =====

        # ===== Menu Section =====
        # Student button
        img2 = Image.open(r"App-Images\Student.png")
        img2 = img2.resize((220, 220), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        b1 = tk.Button(bg_img, image = self.photoimg2)
        b1.place(x = 80, y = 50, width = 220, height = 180)
        # Text: Student Details
        b1_1 = tk.Button(bg_img, text = "Student Details", cursor = "hand2", command = lambda: controller.show_frame(Student), 
        font = ("open sans", 15), bg = "#117c9d", fg = "Black")
        b1_1.place(x = 80, y = 230, width = 220, height = 40)

        # Face detection button
        img3 = Image.open(r"App-Images\Face-recognition.jpg")
        img3 = img3.resize((220, 220), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        b2 = tk.Button(bg_img, image = self.photoimg3)
        b2.place(x = 350, y = 50, width = 220, height = 180)
        # Text: Face Recognition
        b2_2 = tk.Button(bg_img, text = "Face Recognition", command = lambda: controller.show_frame(Face_Recognition), cursor = "hand2", font = ("open sans", 15), 
        bg = "#117c9d", fg = "Black")
        b2_2.place(x = 350, y = 230, width = 220, height = 40)

        # Attendance Button
        img4 = Image.open(r"App-Images\Attendance.jpg")
        img4 = img4.resize((220, 220), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        b3 = tk.Button(bg_img, image = self.photoimg4)
        b3.place(x = 620, y = 50, width = 220, height = 180)
        # Text: Attendance
        b3_3 = tk.Button(bg_img, text = "Attendance", cursor = "hand2", command = lambda: controller.show_frame(Attendance), font = ("open sans", 15), bg = "#117c9d", 
        fg = "Black")
        b3_3.place(x = 620, y = 230, width = 220, height = 40)

        # Train data button
        img6 = Image.open(r"App-Images\Train-data.jpg")
        img6 = img6.resize((220, 220), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        b5 = tk.Button(bg_img, image = self.photoimg6)
        b5.place(x = 890, y = 50, width = 220, height = 180)

        # Text: Train Data
        b5_5 = tk.Button(bg_img, text = "Train Data", cursor = "hand2", command = lambda: controller.show_frame(Train), 
        font = ("open sans", 15), bg = "#117c9d", fg = "Black")
        b5_5.place(x = 890, y = 230, width = 220, height = 40)

        # Photos button
        img7 = Image.open(r"App-Images\Photos.jpg")
        img7 = img7.resize((220, 220), Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)
        b6 = tk.Button(bg_img, image = self.photoimg7)
        b6.place(x = 350, y = 300, width = 220, height = 180)
        # Text: Photos
        b6_6 = tk.Button(bg_img, text = "Photos", cursor = "hand2", command = self.open_img, 
        font = ("open sans", 15), bg = "#117c9d", fg = "Black")
        b6_6.place(x = 350, y = 480, width = 220, height = 40)
        
        img9 = Image.open(r"App-Images\Exit.jpg")
        img9 = img9.resize((220, 220), Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)
        b8 = tk.Button(bg_img, image = self.photoimg9)
        b8.place(x = 620, y = 300, width = 220, height = 180)

        # Text: Exit
        b8_8 = tk.Button(bg_img, text = "Exit", cursor = "hand2", font = ("open sans", 15), 
        bg = "#117c9d", fg = "Black")
        b8_8.place(x = 620, y = 480, width = 220, height = 40)
        # ===== Menu Section =====
        
    def open_img(self):
        os.startfile("Data")
############################# End of Main Page #####################################################

class Student(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # Add the widgets for the Train page here
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
        img = img.resize((1300, 130), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = tk.Label(self, image = self.photoimg)
        f_lbl.place(x= -1, y=0)
        # Adding a background image to the application software
        img1 = Image.open(r"App-Images\Background.webp")
        img1 = img1.resize((1530, 710), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        bg_img = tk.Label(self, image = self.photoimg1)
        bg_img.place(x = 0, y = 130, width = 1530, height = 710)
        # Adding a text in the application
        title_lbl = tk.Label(bg_img,text = "Student Details", font = ("open sans", 30), bg = "white", fg = "Black")
        title_lbl.place(x = -100, y = 0, width = 1530, height = 40)

        back_button = tk.Button(bg_img, text = "Back", command = lambda: controller.show_frame(Main), font = ("Helvetica", 10), bd = 2, relief = RIDGE, width = 13, bg = "#117c9d", fg = "black")
        back_button.place(x = 1010, y = 0, width = 120, height = 40)
        # ===== Header and background images =====

        # ===== Work Frames =====
        #Adding a frame
        main_frame = tk.Frame(bg_img, bd = 2, bg = "white")
        main_frame.place(x = 25, y = 50, width = 1230, height = 480)
        # left label frame
        Left_frame = tk.LabelFrame(main_frame, bd = 2, bg = "white", relief = RAISED, text = "Student Details", font = ("Sans Serif", 12))
        Left_frame.place(x = 10, y = 10, width = 580, height = 450)
    
        # ====== Information section =====
        # Course Info label
        Course_frame = tk.LabelFrame(Left_frame, bd = 2, bg = "white", relief = RIDGE, text = "Current Course", font = ("Sans Serif", 12))
        Course_frame.place(x = 5, y = 10, width = 565, height = 100)
        # Course
        dep_label = tk.Label(Course_frame, text = "Course:", font = ("Sans Serif", 12), bg = "white")
        dep_label.grid(row = 0, column = 0, padx = 5, sticky = W)
        # Course Combo box
        dep_combo = ttk.Combobox(Course_frame, textvariable = self.var_course, font = ("Sans Serif", 12), state = "readonly", width = 15)
        dep_combo["values"] = ("Select Course", "BIT", "BBM", "IMBA")
        dep_combo.current(0)
        dep_combo.grid(row = 0, column = 1, padx = 2, pady = 5, sticky = W)

        # Year
        year_label = tk.Label(Course_frame, text = "Year:", font = ("Sans Serif", 12), bg = "white")
        year_label.grid(row = 0, column = 2, padx = 5, sticky = W)
        # Year Combo box
        year_combo = ttk.Combobox(Course_frame, textvariable = self.var_year, font = ("Sans Serif", 12), state = "readonly", width = 15)
        year_combo["values"] = ("Select Year", "2022-2023", "2023-2024", "2024-2025")
        year_combo.current(0)
        year_combo.grid(row = 0, column = 3, padx = 2, pady = 5, sticky = W)

        # Semester
        semester_label = tk.Label(Course_frame, text = "Semester:", font = ("Sans Serif", 12), bg = "white")
        semester_label.grid(row = 1, column = 0, padx = 5, sticky = W)
        # Semester Combo box
        semester_combo = ttk.Combobox(Course_frame, textvariable = self.var_semester, font = ("Sans Serif", 12), state = "readonly", width = 15)
        semester_combo["values"] = ("Select Semester", "Fall", "Spring")
        semester_combo.current(0)
        semester_combo.grid(row = 1, column = 1, padx = 2, pady = 5, sticky = W)

        # Level
        level_label = tk.Label(Course_frame, text = "Level:", font = ("Sans Serif", 12), bg = "white")
        level_label.grid(row = 1, column = 2, padx = 5, sticky = W)
        # Level Combo box
        level_combo = ttk.Combobox(Course_frame, textvariable = self.var_level, font = ("Sans Serif", 12), state = "readonly", width = 15)
        level_combo["values"] = ("Select Level", "1", "2", "3", "4", "5", "6")
        level_combo.current(0)
        level_combo.grid(row = 1, column = 3, padx = 2, pady = 5, sticky = W)

        #Note: IF the cell is larger than the Widget, the Sticky = W will minimize the problem
        
        # Class Info label
        class_student_frame = tk.LabelFrame(Left_frame, bd = 2, bg = "white", relief = RIDGE, text = "Class Student Information", font = ("Sans Serif", 12))
        class_student_frame.place(x = 5, y = 120, width = 565, height = 300)

        # Student ID
        studentID_label = tk.Label(class_student_frame, text = "Student ID:", font = ("Sans Serif", 12), bg = "white")
        studentID_label.grid(row = 0, column = 0, sticky = W)
        studentID_entry = ttk.Entry(class_student_frame, textvariable= self.var_sID, width = 15, font = ("Sans Serif", 12))
        studentID_entry.grid(row = 0, column = 1, pady = 5, sticky = W)

        # Student Name
        studentName_label = tk.Label(class_student_frame, text = "Student Name:", font = ("Sans Serif", 12), bg = "white")
        studentName_label.grid(row = 1, column = 0, sticky = W)
        studentName_entry = ttk.Entry(class_student_frame, textvariable= self.var_sName, width = 15, font = ("Sans Serif", 12))
        studentName_entry.grid(row = 1, column = 1, pady = 5, sticky = W)

        # Gender
        studentGender_label = tk.Label(class_student_frame, text = "Gender:", font = ("Sans Serif", 12), bg = "white")
        studentGender_label.grid(row = 2, column = 0, sticky = W)
        # Gender Combo box
        gender_combo = ttk.Combobox(class_student_frame, textvariable = self.var_gender, font = ("Sans Serif", 12), state = "readonly", width = 13)
        gender_combo["values"] = ("Male", "Female", "Non-Binary")
        gender_combo.current(0)
        gender_combo.grid(row = 2, column = 1, pady = 3, sticky = W)

        # Email
        studentEmail_label = tk.Label(class_student_frame, text = "Email:", font = ("Sans Serif", 12), bg = "white")
        studentEmail_label.grid(row = 3, column = 0, sticky = W)
        studentEmail_entry = ttk.Entry(class_student_frame, textvariable= self.var_email, width = 15, font = ("Sans Serif", 12))
        studentEmail_entry.grid(row = 3, column = 1, pady = 5, sticky = W)

        # Parents Name
        studentParentsName_label = tk.Label(class_student_frame, text = "Parents Name:", font = ("Sans Serif", 12), bg = "white")
        studentParentsName_label.grid(row = 4, column = 0, sticky = W)
        studentParentsName_entry = ttk.Entry(class_student_frame, textvariable= self.var_pName, width = 15, font = ("Sans Serif", 12))
        studentParentsName_entry.grid(row = 4, column = 1, pady = 5, sticky = W)

        # Address 
        studentAddress_label = tk.Label(class_student_frame, text = "Address:", font = ("Sans Serif", 12), bg = "white")
        studentAddress_label.grid(row = 0, column = 2, padx = 5,  sticky = W)
        studentAddress_entry = ttk.Entry(class_student_frame, textvariable= self.var_address, width = 15, font = ("Sans Serif", 12))
        studentAddress_entry.grid(row = 0, column = 3, padx = 5, sticky = W)

        # Parents Number
        Pn_label = tk.Label(class_student_frame, text = 'Parents Number: ', font = ("Sans Serif", 12), bg = "white")
        Pn_label.grid(row = 1, column = 2, padx = 5,  sticky = W)
        Pn_entry = ttk.Entry(class_student_frame, textvariable= self.var_pNum, width = 15, font = ("Sans Serif", 12))
        Pn_entry.grid(row = 1, column = 3, padx = 5, sticky = W)


        # ===== Radio Buttons =====
        self.var_radio1 = StringVar()
        rbtn1 = ttk.Radiobutton(class_student_frame, variable= self.var_radio1, text = "Take Photo Sample", value = "Yes")
        rbtn1.grid(row = 6, column = 0)
        rbtn2 = ttk.Radiobutton(class_student_frame, variable= self.var_radio1, text = "No Photo Sample")
        rbtn2.grid(row = 6, column = 1)
        # ===== Radio Buttons =====

        # ===== Functional Buttons 1.0 =====
        # Buttons Frame
        btn_frame = tk.Frame(class_student_frame, bd = 2, relief = RAISED, bg = "white")
        btn_frame.place(x = 3, y =200, width = 555, height = 37)

        # Save
        savebtn = tk.Button(btn_frame, text = "Save", command = self.add_data, width = 13, font = ("Sans Serif", 12), bg = "#117c9d", fg = "black")
        savebtn.grid(row = 0, column = 0, padx= 5)

        # Update
        updatebtn = tk.Button(btn_frame, text = "Update", command = self.update_data, width = 13, font = ("Sans Serif", 12), bg = "#117c9d", fg = "black")
        updatebtn.grid(row = 0, column = 1, padx= 5)

        # Delete 
        deletebtn = tk.Button(btn_frame, text = "Delete", command = self.delete_data, width = 13, font = ("Sans Serif", 12), bg = "#117c9d", fg = "black")
        deletebtn.grid(row = 0, column = 2, padx= 5)

        # Reset
        resetbtn = tk.Button(btn_frame, text = "Reset", command = self.reset_data, width = 13, font = ("Sans Serif", 12), bg = "#117c9d", fg = "black")
        resetbtn.grid(row = 0, column = 3, padx= 5)
        # ===== Functional Buttons 1.0 =====

        # ===== Functional Buttons 1.1 =====
        btn_frame1 = tk.Frame(class_student_frame, bd = 2, relief = RAISED, bg = "white")
        btn_frame1.place(x = 3, y =235, width = 555, height = 37)

        # Take Photo
        takephbtn = tk.Button(btn_frame1, command = self.generate_dataset, text = "Take photo sample", width = 29, font = ("Sans Serif", 12), bg = "#117c9d", fg = "black")
        takephbtn.grid(row = 0, column = 2)
        # Update Photo
        updatephbtn = tk.Button(btn_frame1, text = "Update photo sample", width = 29, font = ("Sans Serif", 12), bg = "#117c9d", fg = "black")
        updatephbtn.grid(row = 0, column = 3)
         # ===== Functional Buttons 1.1 =====


        # Right label frame
        Right_frame = tk.LabelFrame(main_frame, bd = 2, bg = "white", relief = RAISED, text = "Student Details", font = ("Sans Serif", 12))
        Right_frame.place(x = 630, y = 10, width = 580, height = 450)

        #=====Search Frame=====
        search_frame = tk.LabelFrame(Right_frame, bd = 2, bg = "white", relief = RIDGE, text = "Search", font = ("Sans Serif", 12))
        search_frame.place(x = 5, y = 10, width = 565, height = 70)
        search_label = tk.Label(search_frame, text = "Search By: ", font = ("Sans Serif", 12), bg = "white")
        search_label.grid(row = 0, column = 0, padx = 5,  sticky = W)

        # Combo Boxes
        search_combo = ttk.Combobox(search_frame, font = ("Sans Serif", 12), state = "readonly", width = 10)
        search_combo["values"] = ("Select", "Name", "ID", "Email")
        search_combo.current(0)
        search_combo.grid(row = 0, column = 1, padx = 2, pady = 5, sticky = W)

        # Entry Fields
        search_entry = ttk.Entry(search_frame, width = 15, font = ("Sans Serif", 12))
        search_entry.grid(row = 0, column = 2, pady = 5, sticky = W)

        # Buttons
        searchbtn = tk.Button(search_frame, text = "Search", width = 10, font = ("Sans Serif", 12), bg = "#117c9d", fg = "black")
        searchbtn.grid(row = 0, column = 3, padx = 2)
        showallbtn = tk.Button(search_frame, text = "Show All", width = 10, font = ("Sans Serif", 12), bg = "#117c9d", fg = "black")
        showallbtn.grid(row = 0, column = 4, padx = 2)

        # ===== Table Frame ====
        table_frame = tk.Frame(Right_frame, bd = 2, bg = "white", relief = RIDGE)
        table_frame.place(x = 5, y = 120, width = 565, height = 300)

        # ===== Scroll bar =====
        Scroll_x = ttk.Scrollbar(table_frame, orient = HORIZONTAL)
        Scroll_y = ttk.Scrollbar(table_frame, orient = VERTICAL)
        # ===== Scroll bar =====

        # ===== Table Contents =====
        self.student_table = ttk.Treeview(table_frame, column = ("Course", "Year", "Semester", "Level", "Student ID", "Student Name", "Gender", "Email", "Parents Name", "Address", "Parents Number", "Photo"), xscrollcommand = Scroll_x.set, yscrollcommand = Scroll_y.set)
        Scroll_x.pack(side = BOTTOM, fill = X)
        Scroll_y.pack(side = RIGHT, fill = Y)
        Scroll_x.config(command = self.student_table.xview)
        Scroll_y.config(command = self.student_table.yview)
        self.student_table.heading("Course", text = "Course")
        self.student_table.heading("Year", text = "Year")
        self.student_table.heading("Semester", text = "Semester")
        self.student_table.heading("Level", text = "Level")
        self.student_table.heading("Student ID", text = "Student ID")
        self.student_table.heading("Student Name", text = "Student Name")
        self.student_table.heading("Gender", text = "Gender")
        self.student_table.heading("Email", text = "Email")
        self.student_table.heading("Parents Name", text = "Parents Name")
        self.student_table.heading("Address", text = "Address")
        self.student_table.heading("Parents Number", text = "Parents Number")
        self.student_table.heading("Photo", text = "Photo Sample Status")
        self.student_table["show"] = "headings"

        self.student_table.column("Course", width = 100)
        self.student_table.column("Year", width = 100)
        self.student_table.column("Semester", width = 100)
        self.student_table.column("Level", width = 100)
        self.student_table.column("Student ID", width = 100)
        self.student_table.column("Student Name", width = 100)
        self.student_table.column("Gender", width = 100)
        self.student_table.column("Email", width = 100)
        self.student_table.column("Parents Name", width = 100)
        self.student_table.column("Address", width = 100)
        self.student_table.column("Parents Number", width = 100)
        self.student_table.column("Photo", width = 100)
        self.student_table.pack(fill = BOTH, expand = 1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()
        # ===== Table Contents =====
         
                
        #### Function Declaration #####
    def add_data(self):
        if self.var_course.get() == "Select Course" or self.var_sName.get() == "" or self.var_sID.get() == "":
            messagebox.showerror("Error", "All fields required", parent = self)
        else:
            try:
                conn = mysql.connector.connect(host = "localhost", username = "root", password = "PunnSxG@2806", database = "face_recognition")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                    self.var_course.get(),
                                                                                                    self.var_year.get(),
                                                                                                    self.var_semester.get(),
                                                                                                    self.var_level.get(),
                                                                                                    self.var_sID.get(),
                                                                                                    self.var_sName.get(),
                                                                                                    self.var_gender.get(),
                                                                                                    self.var_email.get(),
                                                                                                    self.var_pName.get(),
                                                                                                    self.var_address.get(),
                                                                                                    self.var_pNum.get(),
                                                                                                    self.var_radio1.get()                                                                                       
                                                                                                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success","student details has been added successfully", parent = self)            
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent = self)

#### Fetching data into the application table ###
    def fetch_data(self):
        conn = mysql.connector.connect(host = "localhost", username = "root", password = "PunnSxG@2806", database = "face_recognition")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()
        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values = i)
            conn.commit()
        conn.close()

### Get cursor ###
    def get_cursor(self, event = ""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]
        self.var_course.set(data[0])
        self.var_year.set(data[1])
        self.var_semester.set(data[2])
        self.var_level.set(data[3])
        self.var_sID.set(data[4])
        self.var_sName.set(data[5])
        self.var_gender.set(data[6])
        self.var_email.set(data[7])
        self.var_pName.set(data[8])
        self.var_address.set(data[9])
        self.var_pNum.set(data[10])
        self.var_radio1.set(data[11])

# ===== Update =====
    def update_data(self):
        if self.var_course.get() == "Select Course" or self.var_sName.get() == "" or self.var_sID.get() == "":
            messagebox.showerror("Error", "All fields required", parent = self)
        else:
            try:
                Update = messagebox.askyesno("update", "Do you want to update the data?", parent = self)
                if Update > 0:
                    conn = mysql.connector.connect(host = "localhost", username = "root", password = "PunnSxG@2806", database = "face_recognition")
                    my_cursor = conn.cursor()
                    my_cursor.execute("Update student set course = %s, year = %s, semester = %s, level = %s, student_name = %s, gender = %s, email = %s, parents_name = %s, address = %s, parents_number = %s, photo_sample = %s where student_id = %s",(
                                                                                                                                                                                                                                self.var_course.get(),
                                                                                                                                                                                                                                self.var_year.get(),
                                                                                                                                                                                                                                self.var_semester.get(),
                                                                                                                                                                                                                                self.var_level.get(),                                                                                                                                                                                                                     
                                                                                                                                                                                                                                self.var_sName.get(),
                                                                                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                                                                                self.var_pName.get(),
                                                                                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                                                                                self.var_pNum.get(),
                                                                                                                                                                                                                                self.var_radio1.get(),                                                                                                                                                                                                                           
                                                                                                                                                                                                                                self.var_sID.get()
                                                                                                                                                                                                                              ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success", "Student student successfully updated", parent = self)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent = self)
# ===== Update =====


# ===== Delete =====
    def delete_data(self):
        if self.var_sID.get() == "":
            messagebox.showerror("Error", "Student ID required", parent = self)
        else:
            try:
                delete = messagebox.askyesno("Student Delete Page", "Do you really want to delete this entry?", parent = self)
                if delete > 0:
                    conn = mysql.connector.connect(host = "localhost", username = "root", password = "PunnSxG@2806", database = "face_recognition")
                    my_cursor = conn.cursor()
                    sql = "delete from details where student_id = %s"
                    val = (self.var_sID.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete", "Successfully deleted entry", parent = self)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent = self)
# ===== Delete =====

# ===== Reset =====
    def reset_data(self):
        self.var_course.set("Select Course")
        self.var_semester.set("Select Semester")
        self.var_year.set("Select Year")
        self.var_level.set("Select Level")
        self.var_sID.set("")
        self.var_sName.set("")
        self.var_gender.set("Select Gender")
        self.var_email.set("")
        self.var_pName.set("")
        self.var_address.set("")
        self.var_pNum.set("")
        self.var_radio1.set("")
# ===== Reset =====


# ===This function updates MySQL database with student information. 
# The function first checks if certain fields (course, student name, and student ID) are filled out, 
# and if not, it displays an error message. Then, it attempts to connect to MySQL database called "face_recognition" 
# using the specified host, username, and password. It creates a cursor and executes a query to select all entries from the "details" table.
# It then loops through the results to increase a variable "id" by 1. 
# Finally, it uses the cursor to execute an update query to update the "details" table with the student information from the various variables
# (course, year, semester, level, student name, gender, email, parents name, address, parents number, and photo sample) 
# using the student ID as the primary key. ===

# ===== Generating dataset and taking photo Sample =====
    def generate_dataset(self):
        if self.var_course.get() == "Select Course" or self.var_sName.get() == "" or self.var_sID.get() == "":
            messagebox.showerror("Error", "All fields required", parent = self)
        else:
            try:
                conn = mysql.connector.connect(host = "localhost", username = "root", password = "PunnSxG@2806", database = "face_recognition")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id += 1
                my_cursor.execute("Update student set course = %s, year = %s, semester = %s, level = %s, student_name = %s, gender = %s, email = %s, parents_name = %s, address = %s, parents_number = %s, photo_sample = %s where student_id = %s",(
                                                                                                                                                                                                                                self.var_course.get(),
                                                                                                                                                                                                                                self.var_year.get(),
                                                                                                                                                                                                                                self.var_semester.get(),
                                                                                                                                                                                                                                self.var_level.get(),                                                                                                                                                                                                                     
                                                                                                                                                                                                                                self.var_sName.get(),
                                                                                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                                                                                self.var_pName.get(),
                                                                                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                                                                                self.var_pNum.get(),
                                                                                                                                                                                                                                self.var_radio1.get(),                                                                                                                                                                                                                           
                                                                                                                                                                                                                                self.var_sID.get() == +1
                                                                                                                                                                                                                            ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

# === This section of the code uses OpenCV to capture video from the device's camera and detect faces in the frames 
# using the pre-trained Haar cascade classifier "haarcascade_frontalface_default.xml". 
# The detected faces are then cropped from the frames and resized to 450x450 pixels. 
# The cropped and resized images are then saved to the "data" folder with filenames in the format "user.id.img_id.jpg".
#  The code continues to capture and save images until the user presses the enter key or 100 images have been captured. 
#  A message box is displayed at the end of the process to confirm that the dataset has been generated successfully. 
#  If an exception occurs, an error message box is displayed with the specific error message. ===

##### Loading haarcascade library from openCV and 
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    #### Scaling factor = 1.3
                    ### Minimun neighnor = 5
                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y+h, x:x+w]
                        return face_cropped
                cap = cv2.VideoCapture(0)
                img_id = 0 
                while True:
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = "Data/user." + str(id) + "." + str(img_id) + ".jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (50,50), cv2.FONT_HERSHEY_COMPLEX, 2, (0,255,230), 2)
                        cv2.imshow("Cropped Face", face)
                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating dataset completed successfully")
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent = self)

    def close(self):
        self.destroy()
        return   
############################# End of Student Page #####################################################

class Train(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # Add the widgets for the Train page here
        img = Image.open(r"App-Images\Header.jpg")
        img = img.resize((1300, 130), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self, image = self.photoimg)
        f_lbl.place(x= -1, y=0)

        # Adding a background image to the application software
        img1 = Image.open(r"App-Images\Background.webp")
        img1 = img1.resize((1530, 710), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        bg_img = Label(self, image = self.photoimg1)
        bg_img.place(x = 0, y = 130, width = 1530, height = 710)

        # Adding a text in the application
        title_lbl = Label(bg_img,text = "Train Data", font = ("open sans", 30), bg = "white", fg = "Black")
        title_lbl.place(x = -100, y = 0, width = 1530, height = 40)

        back_button = tk.Button(bg_img, text = "Back", command = lambda: controller.show_frame(Main), font = ("Helvetica", 10), bd = 2, relief = RIDGE, width = 13, bg = "#117c9d", fg = "black")
        back_button.place(x = 1010, y = 0, width = 120, height = 40)
        # Train data button
        img6 = Image.open(r"App-Images\Train-data.jpg")
        img6 = img6.resize((220, 220), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        b5 = Button(bg_img, image = self.photoimg6)
        b5.place(x = 550, y = 50, width = 220, height = 180)
        # Text: Train Data
        b5_5 = Button(bg_img, text = "Train Data", cursor = "hand2", command = self.train_classifier, font = ("open sans", 15), bg = "#117c9d", fg = "Black")
        b5_5.place(x = 550, y = 230, width = 220, height = 40)

    def train_classifier(self):
        data_dir = ("Data")
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]
        faces = []
        IDs = []
        for image in path:
            img = Image.open(image).convert('L')        # Grayscale image
            imageNP = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])
            faces.append(imageNP)
            IDs.append(id)
            cv2.imshow("Training", imageNP)
            cv2.waitKey(1) == 13
        IDs = np.array(IDs)
 
    # ===== Training the classifier =====
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, IDs)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training dataset completed")
############################# End of Train Page #####################################################

class Attendance(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # Add the widgets for the Attendance page here
        self.var_atten_id = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_date = StringVar() 
        self.var_atten_time = StringVar()
        self.var_atten_course = StringVar()
        self.var_atten_status = StringVar()

    # ===== Header and background images =====
        img = Image.open(r"App-Images\Header.jpg")
        img = img.resize((1300, 130), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self, image = self.photoimg)
        f_lbl.place(x= -1, y=0)
        # Adding a background image to the application software
        img1 = Image.open(r"App-Images\Background.webp")
        img1 = img1.resize((1530, 710), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        bg_img = Label(self, image = self.photoimg1)
        bg_img.place(x = 0, y = 130, width = 1530, height = 710)
        
        # Adding a text in the application
        title_lbl = Label(bg_img,text = "Attendance Management System", font = ("open sans", 30), bg = "white", fg = "Black")
        title_lbl.place(x = -100, y = 0, width = 1530, height = 40)
        back_button = tk.Button(bg_img, text = "Back", command = lambda: controller.show_frame(Main), font = ("Helvetica", 10), bd = 2, relief = RIDGE, width = 13, bg = "#117c9d", fg = "black")
        back_button.place(x = 1010, y = 0, width = 120, height = 40)
    # ===== Header and background images =====


    # ===== Work Frames =====
        #Adding a frame
        main_frame = Frame(bg_img, bd = 2, bg = "white")
        main_frame.place(x = 25, y = 50, width = 1230, height = 480)
        # left label frame
        Left_frame = LabelFrame(main_frame, bd = 2, bg = "white", relief = RAISED, text = "Student Attendance Details", font = ("Sans Serif", 12))
        Left_frame.place(x = 10, y = 10, width = 580, height = 450)

        inside_left_frame = Frame(Left_frame, bd = 2, relief = RIDGE, bg = "white")
        inside_left_frame.place(x = 5, y = 0, width = 560, height = 420)
        
        # ===== Lables and Entry Fields
        # Attendance
        AttendanceID_label = Label(inside_left_frame, text = "Attendance ID:", font = ("Sans Serif", 12), bg = "white")
        AttendanceID_label.grid(row = 0, column = 0, sticky = W)
        AttendanceID_entry = ttk.Entry(inside_left_frame, width = 15, textvariable = self.var_atten_id, font = ("Sans Serif", 12))
        AttendanceID_entry.grid(row = 0, column = 1, pady = 5, sticky = W)

        # Name
        Name_label = Label(inside_left_frame, text = "Name:", font = ("Sans Serif", 12), bg = "white")
        Name_label.grid(row = 0, column = 2, sticky = W)
        Name_entry = ttk.Entry(inside_left_frame, width = 15, textvariable = self.var_atten_name, font = ("Sans Serif", 12))
        Name_entry.grid(row = 0, column = 3, pady = 5, sticky = W)

        # Date
        Date_label = Label(inside_left_frame, text = "Date:", font = ("Sans Serif", 12), bg = "white")
        Date_label.grid(row = 1, column = 0, sticky = W)
        Date_entry = ttk.Entry(inside_left_frame, width = 15, textvariable = self.var_atten_date, font = ("Sans Serif", 12))
        Date_entry.grid(row = 1, column = 1, pady = 5, sticky = W)

        # Time
        Time_label = Label(inside_left_frame, text = "Time:", font = ("Sans Serif", 12), bg = "white")
        Time_label.grid(row = 1, column = 2, sticky = W)
        Time_entry = ttk.Entry(inside_left_frame, textvariable = self.var_atten_time, width = 15, font = ("Sans Serif", 12))
        Time_entry.grid(row = 1, column = 3, pady = 5, sticky = W)

        # Course 
        Course_label = Label(inside_left_frame, text = "Course:", font = ("Sans Serif", 12), bg = "white")
        Course_label.grid(row = 2, column = 2, sticky = W)
        Course_entry = ttk.Entry(inside_left_frame, width = 15, textvariable = self.var_atten_course, font = ("Sans Serif", 12))
        Course_entry.grid(row = 2, column = 3, pady = 5, sticky = W)

        # Attendance Combo
        Attendance_label = Label(inside_left_frame, text = "Attendance Status:", font = ("Sans Serif", 12), bg = "white")
        Attendance_label.grid(row = 2, column = 0, sticky = W)
        self.atten_status = ttk.Combobox(inside_left_frame, textvariable = self.var_atten_status, font = ("Sans Serif", 12), state = "readonly", width = 13)
        self.atten_status["values"] = ("Stauts", "Present", "Absent")
        self.atten_status.grid(row = 2, column = 1)
        self.atten_status.current(0)

        # ===== Functional Buttons 1.0 =====
        # Buttons Frame
        btn_frame = Frame(inside_left_frame, bd = 2, relief = RAISED, bg = "white")
        btn_frame.place(x = 1, y = 372, width = 555, height = 37)

        # Import
        importbtn = Button(btn_frame, text = "Import CSV", command = self.importCSV, width = 18, font = ("Sans Serif", 12), bg = "#117c9d", fg = "black")
        importbtn.grid(row = 0, column = 0, padx= 5)

        # Export
        exportbtn = Button(btn_frame, text = "Export CSV", command = self.exportCSV, width = 18, font = ("Sans Serif", 12), bg = "#117c9d", fg = "black")
        exportbtn.grid(row = 0, column = 1, padx= 5)

        # Reset
        resetbtn = Button(btn_frame, text = "Reset", width = 18, command = self.reset_data, font = ("Sans Serif", 12), bg = "#117c9d", fg = "black")
        resetbtn.grid(row = 0, column = 3, padx= 5)
        # ===== Functional Buttons 1.0 =====
        
        # Right label frame
        Right_frame = LabelFrame(main_frame, bd = 2, bg = "white", relief = RAISED, text = "Attendance Details", font = ("Sans Serif", 12))
        Right_frame.place(x = 630, y = 10, width = 580, height = 450)
        
        table_frame = Frame(Right_frame, bd = 2, relief = RAISED, bg = "white")
        table_frame.place(x = 5, y = 5, width = 565, height = 380)

        # ===== Scroll Bar and Table =====
        Scroll_x = ttk.Scrollbar(table_frame, orient = HORIZONTAL)
        Scroll_y = ttk.Scrollbar(table_frame, orient = VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame, column = ("ID", "Name", "Date", "Time", "Course", "Attendance Status"), xscrollcommand = Scroll_x.set, yscrollcommand = Scroll_y.set)

        Scroll_x.pack(side = BOTTOM, fill = X)
        Scroll_y.pack(side = RIGHT, fill = Y)

        Scroll_x.config(command = self.AttendanceReportTable.xview)
        Scroll_y.config(command = self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("ID", text = "Attendance ID")
        self.AttendanceReportTable.heading("Name", text = "Name")
        self.AttendanceReportTable.heading("Date", text= "Date")
        self.AttendanceReportTable.heading("Time", text = "Time")
        self.AttendanceReportTable.heading("Course", text = "Course")
        self.AttendanceReportTable.heading("Attendance Status", text = "Attendance Status")

        self.AttendanceReportTable["show"] = "headings"
        
        self.AttendanceReportTable.column("ID", width = 100)
        self.AttendanceReportTable.column("Name", width = 100)
        self.AttendanceReportTable.column("Time", width = 100)
        self.AttendanceReportTable.column("Date", width = 100)
        self.AttendanceReportTable.column("Course", width = 100)
        self.AttendanceReportTable.column("Attendance Status", width = 100)

        self.AttendanceReportTable.pack(fill = BOTH, expand = 1)
        self.AttendanceReportTable.bind("<ButtonRelease>", self.get_cursor)

        # ===== Fetching Data =====
    def fetch_data(self, rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("", END, values = i)
        # importCSV
    def importCSV(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir = os.getcwd(), title = "Open CSV", filetypes = (("CSV FILE", "*.csv"), ("All File", "*.*")), parent = self)
        with open(fln) as myfile:
            csvread = csv.reader(myfile, delimiter = ",")
            for i in csvread:
                mydata.append(i)
            self.fetch_data(mydata)   
        # export CSV
    def exportCSV(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("Error", "No data to export", parent = self)
                return False
            fln = filedialog.asksaveasfilename(initialdir = os.getcwd(), title = "Open CSV", filetypes = (("CSV FILE", "*.csv"), ("All File", "*.*")), parent = self)
            with open(fln, mode = "w", newline = "") as myfile:
                exp_write = csv.writer(myfile, delimiter = ",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Success", "Data exported successfully to " + os.path.basename(fln))
        except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent = self)

    def get_cursor(self, event = ""):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        rows = content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_name.set(rows[1])
        self.var_atten_date.set(rows[2])
        self.var_atten_time.set(rows[3])
        self.var_atten_course.set(rows[4])
        self.var_atten_status.set(rows[5])

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_name.set("")
        self.var_atten_date.set("")
        self.var_atten_time.set("")
        self.var_atten_course.set("")
        self.var_atten_status.set("")
        # ===== Fetching Data =====
############################# End of Attendance Page #####################################################

class Face_Recognition(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # Add the widgets for the Face Recognition page here
        img = Image.open(r"App-Images\Header.jpg")
        img = img.resize((1300, 130), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self, image = self.photoimg)
        f_lbl.place(x= -1, y=0)

        # Adding a background image to the application software
        img1 = Image.open(r"App-Images\Background.webp")
        img1 = img1.resize((1530, 710), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        bg_img = Label(self, image = self.photoimg1)
        bg_img.place(x = 0, y = 130, width = 1530, height = 710)
        
        # Adding a text in the application
        title_lbl = Label(bg_img,text = "Face Recognition", font = ("open sans", 30), bg = "white", fg = "Black")
        title_lbl.place(x = -100, y = 0, width = 1530, height = 40)
        back_button = tk.Button(bg_img, text = "Back", command = lambda: controller.show_frame(Main), font = ("Helvetica", 10), bd = 2, relief = RIDGE, width = 13, bg = "#117c9d", fg = "black")
        back_button.place(x = 1010, y = 0, width = 120, height = 40)

        # Face recognition button
        img6 = Image.open(r"App-Images\Face-recognition.jpg")
        img6 = img6.resize((220, 220), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        b5 = Button(bg_img, image = self.photoimg6)
        b5.place(x = 550, y = 50, width = 220, height = 180)
        # Text: Face Recognition
        b5_5 = Button(bg_img, text = "Face Recognition", cursor = "hand2", command = self.face_recog, font = ("open sans", 15), bg = "#117c9d", fg = "Black")
        b5_5.place(x = 550, y = 230, width = 220, height = 40)
    

    # ===== For Attendance =====
    def mark_attendance(self, n, i, c):
        with open("Attendance Report.csv", "r+", newline = "\n") as f:
            myDataList = f.readlines()
            name_list = []
            for line in myDataList:
                entry = line.split((", "))
                name_list.append(entry[0])
            if((n not in name_list) and (i not in name_list) and (c not in name_list)):
                now = datetime.now()
                d1 = now.strftime("%d/ %m/ %Y")
                dtString = now.strftime("%H: %M: %S")
                f.writelines(f"\n{n}, {i}, {c}, {dtString}, {d1}, Present")
     # ===== For Attendance =====

    
    # ===== Face Recognition Function =====
    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
            
            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y),(x + w, y +h),(0,255,0),3)
                id, predict = clf.predict(gray_image[y:y + h, x: x + w])
                confidence = int((100 * (1-predict / 300)))
                
                conn = mysql.connector.connect(host = "localhost", username = "root", password = "PunnSxG@2806", database = "face_recognition")
                my_cursor = conn.cursor()

                my_cursor.execute("select student_name from student where student_id = " + str(id))
                n = my_cursor.fetchone()
                n = "," . join(n)
                
                my_cursor.execute("select student_id from student where student_id = " + str(id))
                i = my_cursor.fetchone()
                i = "," . join(i)

                my_cursor.execute("select course from student where student_id = " + str(id))
                c = my_cursor.fetchone()
                c = "," . join(c)

                if confidence > 77 :
                    cv2.putText(img, f"ID:{i}"(x, y - 55), cv2.FONT_ITALIC, 0.8, (255,255,255), 2)
                    cv2.putText(img, f"Name:{n}"(x, y - 30), cv2.FONT_ITALIC, 0.8, (255,255,255), 2)
                    cv2.putText(img, f"Course:{c}"(x, y - 5), cv2.FONT_ITALIC, 0.8, (255,255,255), 2)
                    self.mark_attendance(n, i, c)
                    #Anti-spoofing code
                    if(self.is_live(gray_image[y:y + h, x: x + w])):
                        cv2.putText(img, "Live", (x, y - 80), cv2.FONT_ITALIC, 0.8, (255,255,255), 2)
                        self.mark_attendance(n, i, c)
                    else:
                         cv2.putText(img, "Fake", (x, y - 80), cv2.FONT_ITALIC, 0.8, (255,255,255), 2)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y +h), (0,0,255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 55), cv2.FONT_ITALIC, 0.8, (255,255,255), 2)
                coord = [x, y, w, h]
            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 255, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")   
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        # video_cap = cv2.VideoCapture(url)
        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to face recognition", img)
            
            if cv2.waitKey(1) == 13:
                break
        video_cap.release()
        cv2.destroyAllWindows()
############################# End of Face Recognition Page #####################################################

class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        window = tk.Frame(self)
        window.pack()

        window.grid_rowconfigure(0, minsize = 790)
        window.grid_columnconfigure(0, minsize = 1530)

        self.frames = {}
        for F in (Main, Student, Train, Attendance, Face_Recognition):
            frame = F(window, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")
        self.show_frame(Main)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()

app = Application()
app.mainloop()