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
        self.var_search_records = StringVar()
        self.var_search_criteria = StringVar()

        
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

          # Course
        search_label = Label(search_frame, text="Search By:", font=("Sans Serif", 12), bg="white")
        search_label.grid(row=0, column=0, padx=5, sticky=W)

        search_entry = ttk.Combobox(search_frame, font=("Sans Serif", 12), state="readonly", width=15, textvariable=self.var_search_criteria)
        search_entry["values"] = ("Select Field", "ID", "Name")
        search_entry.current(0)
        search_entry.grid(row=0, column=2, padx=2, pady=5, sticky=W)

        search_records_entry = ttk.Entry(search_frame, textvariable=self.var_search_records, width=15, font=("Sans Serif", 12))
        search_records_entry.grid(row=0, column=3, pady=5, sticky=W)


        # Buttons
        searchbtn = Button(search_frame, text = "Search", command = self.search_records, width = 15, font = ("Sans Serif", 12), bg = "#117c9d", fg = "black")
        searchbtn.grid(row = 0, column = 4, padx = 2)

         # Reset
        resetbtn = Button(Left_frame, text = "Reset", command = self.reset_treeview, width = 29, font = ("Sans Serif", 12), bg = "#117c9d", fg = "black")
        resetbtn.place(x = 150, y = 415)
        # ===== Functional Buttons 1.0 =====

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
        search_criteria = self.var_search_criteria.get()
        search_value = self.var_search_records.get()
        
        # Validate search value
        if not search_value:
            messagebox.showerror("Error", "Please enter a search value")
            return

        conn = mysql.connector.connect(host="localhost", username="root", password="PunnSxG@2806", database="face_recognition")
        my_cursor = conn.cursor()

        query = ""
        if search_criteria == "ID":
            query = "SELECT * FROM attendance WHERE student_ID LIKE %s"
        elif search_criteria == "Name":
            query = "SELECT * FROM attendance WHERE name LIKE %s"

        if query:
            my_cursor.execute(query, (search_value, ))
            records = my_cursor.fetchall()

            if records:
                self.student_table.delete(*self.student_table.get_children())
                for record in records:
                    self.student_table.insert("", END, values=record)

                count = len(records)
                messagebox.showinfo("Result", f"The student is present for {count} days")
            else:
                messagebox.showinfo("Result", "No records found")

        conn.close()

# Reset Treeview

    def reset_treeview(self):
        for record in self.student_table.get_children():
            self.student_table.delete(record)

if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
