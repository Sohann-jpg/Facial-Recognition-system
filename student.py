from tkinter import * 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector

# Making a class that initiates the backend application of the project
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

        img = Image.open(r"C:\Users\sohan\Desktop\College\FYP\Facial_Recognition_System\App-Images\Header.jpg")
        img = img.resize((1300, 130), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root, image = self.photoimg)
        f_lbl.place(x= -1, y=0)

        # Adding a background image to the application software
        img1 = Image.open(r"C:\Users\sohan\Desktop\College\FYP\Facial_Recognition_System\App-Images\Background.webp")
        img1 = img1.resize((1530, 710), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        bg_img = Label(self.root, image = self.photoimg1)
        bg_img.place(x = 0, y = 130, width = 1530, height = 710)

        # Adding a text in the application
        title_lbl = Label(bg_img,text = "Student Details", font = ("open sans", 30), bg = "white", fg = "Black")
        title_lbl.place(x = -100, y = 0, width = 1530, height = 40)

        #Adding a frame
        main_frame = Frame(bg_img, bd = 2, bg = "white")
        main_frame.place(x = 25, y = 50, width = 1230, height = 480)

        # left label frame
        Left_frame = LabelFrame(main_frame, bd = 2, bg = "white", relief = RAISED, text = "Student Details", font = ("Sans Serif", 12))
        Left_frame.place(x = 10, y = 10, width = 580, height = 450)

        # Information section
        # Course Info label
        Course_frame = LabelFrame(Left_frame, bd = 2, bg = "white", relief = RIDGE, text = "Current Course", font = ("Sans Serif", 12))
        Course_frame.place(x = 5, y = 10, width = 565, height = 100)

        #Course
        dep_label = Label(Course_frame, text = "Course:", font = ("Sans Serif", 12), bg = "white")
        dep_label.grid(row = 0, column = 0, padx = 5, sticky = W)

        dep_combo = ttk.Combobox(Course_frame, textvariable = self.var_course, font = ("Sans Serif", 12), state = "readonly", width = 15)
        dep_combo["values"] = ("Select Course", "BIT", "BBM", "IMBA")
        dep_combo.current(0)
        dep_combo.grid(row = 0, column = 1, padx = 2, pady = 5, sticky = W)

        #Year
        year_label = Label(Course_frame, text = "Year:", font = ("Sans Serif", 12), bg = "white")
        year_label.grid(row = 0, column = 2, padx = 5, sticky = W)

        year_combo = ttk.Combobox(Course_frame, textvariable = self.var_year, font = ("Sans Serif", 12), state = "readonly", width = 15)
        year_combo["values"] = ("Select Year", "2022-2023", "2023-2024", "2024-2025")
        year_combo.current(0)
        year_combo.grid(row = 0, column = 3, padx = 2, pady = 5, sticky = W)

        #Semester
        semester_label = Label(Course_frame, text = "Semester:", font = ("Sans Serif", 12), bg = "white")
        semester_label.grid(row = 1, column = 0, padx = 5, sticky = W)

        semester_combo = ttk.Combobox(Course_frame, textvariable = self.var_semester, font = ("Sans Serif", 12), state = "readonly", width = 15)
        semester_combo["values"] = ("Select Semester", "Fall", "Spring")
        semester_combo.current(0)
        semester_combo.grid(row = 1, column = 1, padx = 2, pady = 5, sticky = W)

        #Level
        level_label = Label(Course_frame, text = "Level:", font = ("Sans Serif", 12), bg = "white")
        level_label.grid(row = 1, column = 2, padx = 5, sticky = W)

        level_combo = ttk.Combobox(Course_frame, textvariable = self.var_level, font = ("Sans Serif", 12), state = "readonly", width = 15)
        level_combo["values"] = ("Select Level", "1", "2", "3", "4", "5", "6")
        level_combo.current(0)
        level_combo.grid(row = 1, column = 3, padx = 2, pady = 5, sticky = W)

        #Note: IF the cell is larger than the Widget, the Sticky = W will minimize the problem


        # Class Info label
        class_student_frame = LabelFrame(Left_frame, bd = 2, bg = "white", relief = RIDGE, text = "Class Student Information", font = ("Sans Serif", 12))
        class_student_frame.place(x = 5, y = 120, width = 565, height = 300)

        #Student ID ############
        studentID_label = Label(class_student_frame, text = "Student ID:", font = ("Sans Serif", 12), bg = "white")
        studentID_label.grid(row = 0, column = 0, sticky = W)
        studentID_entry = ttk.Entry(class_student_frame, textvariable= self.var_sID, width = 15, font = ("Sans Serif", 12))
        studentID_entry.grid(row = 0, column = 1, pady = 5, sticky = W)

        # Student Name
        studentName_label = Label(class_student_frame, text = "Student Name:", font = ("Sans Serif", 12), bg = "white")
        studentName_label.grid(row = 1, column = 0, sticky = W)
        studentName_entry = ttk.Entry(class_student_frame, textvariable= self.var_sName, width = 15, font = ("Sans Serif", 12))
        studentName_entry.grid(row = 1, column = 1, pady = 5, sticky = W)

        #Gender ############
        studentGender_label = Label(class_student_frame, text = "Gender:", font = ("Sans Serif", 12), bg = "white")
        studentGender_label.grid(row = 2, column = 0, sticky = W)
        studentGender_entry = ttk.Entry(class_student_frame, textvariable= self.var_gender, width = 15, font = ("Sans Serif", 12))
        studentGender_entry.grid(row = 2, column = 1, pady = 5, sticky = W)

        #Email ##############
        studentEmail_label = Label(class_student_frame, text = "Email:", font = ("Sans Serif", 12), bg = "white")
        studentEmail_label.grid(row = 3, column = 0, sticky = W)
        studentEmail_entry = ttk.Entry(class_student_frame, textvariable= self.var_email, width = 15, font = ("Sans Serif", 12))
        studentEmail_entry.grid(row = 3, column = 1, pady = 5, sticky = W)

        # Parents Name ############
        studentParentsName_label = Label(class_student_frame, text = "Parents Name:", font = ("Sans Serif", 12), bg = "white")
        studentParentsName_label.grid(row = 4, column = 0, sticky = W)
        studentParentsName_entry = ttk.Entry(class_student_frame, textvariable= self.var_pName, width = 15, font = ("Sans Serif", 12))
        studentParentsName_entry.grid(row = 4, column = 1, pady = 5, sticky = W)

        #Address 
        studentAddress_label = Label(class_student_frame, text = "Address:", font = ("Sans Serif", 12), bg = "white")
        studentAddress_label.grid(row = 0, column = 2, padx = 5,  sticky = W)
        studentAddress_entry = ttk.Entry(class_student_frame, textvariable= self.var_address, width = 15, font = ("Sans Serif", 12))
        studentAddress_entry.grid(row = 0, column = 3, padx = 5, sticky = W)

        #Parents Number
        Pn_label = Label(class_student_frame, text = 'Parents Number: ', font = ("Sans Serif", 12), bg = "white")
        Pn_label.grid(row = 1, column = 2, padx = 5,  sticky = W)
        Pn_entry = ttk.Entry(class_student_frame, textvariable= self.var_pNum, width = 15, font = ("Sans Serif", 12))
        Pn_entry.grid(row = 1, column = 3, padx = 5, sticky = W)


        #Radio Buttons
        self.var_radio1 = StringVar()
        rbtn1 = ttk.Radiobutton(class_student_frame, textvariable= self.var_radio1, text = "Take Photo Sample", value = "Yes")
        rbtn1.grid(row = 6, column = 0)

        self.var_radio2 = StringVar()
        rbtn2 = ttk.Radiobutton(class_student_frame, textvariable= self.var_radio2, text = "No Photo Sample")
        rbtn2.grid(row = 6, column = 1)

        # Buttons Frame
        btn_frame = Frame(class_student_frame, bd = 2, relief = RAISED, bg = "white")
        btn_frame.place(x = 3, y =200, width = 555, height = 37)

        savebtn = Button(btn_frame, text = "Save", command = self.add_data, width = 13, font = ("Sans Serif", 12), bg = "aqua", fg = "black")
        savebtn.grid(row = 0, column = 0, padx= 5)

        updatebtn = Button(btn_frame, text = "Update", width = 13, font = ("Sans Serif", 12), bg = "aqua", fg = "black")
        updatebtn.grid(row = 0, column = 1, padx= 5)

        deletebtn = Button(btn_frame, text = "Delete", width = 13, font = ("Sans Serif", 12), bg = "aqua", fg = "black")
        deletebtn.grid(row = 0, column = 2, padx= 5)

        resetbtn = Button(btn_frame, text = "Reset", width = 13, font = ("Sans Serif", 12), bg = "aqua", fg = "black")
        resetbtn.grid(row = 0, column = 3, padx= 5)

        btn_frame1 = Frame(class_student_frame, bd = 2, relief = RAISED, bg = "white")
        btn_frame1.place(x = 3, y =235, width = 555, height = 37)


        takephbtn = Button(btn_frame1, text = "Take photo sample", width = 29, font = ("Sans Serif", 12), bg = "aqua", fg = "black")
        takephbtn.grid(row = 0, column = 2)

        updatephbtn = Button(btn_frame1, text = "Update photo sample", width = 29, font = ("Sans Serif", 12), bg = "aqua", fg = "black")
        updatephbtn.grid(row = 0, column = 3)


        ############ Right label frame ############
        Right_frame = LabelFrame(main_frame, bd = 2, bg = "white", relief = RAISED, text = "Student Details", font = ("Sans Serif", 12))
        Right_frame.place(x = 630, y = 10, width = 580, height = 450)
        #=====Search Frame=====
        search_frame = LabelFrame(Right_frame, bd = 2, bg = "white", relief = RIDGE, text = "Search", font = ("Sans Serif", 12))
        search_frame.place(x = 5, y = 10, width = 565, height = 70)
        search_label = Label(search_frame, text = "Search By: ", font = ("Sans Serif", 12), bg = "white")
        search_label.grid(row = 0, column = 0, padx = 5,  sticky = W)
        ### Combo Boxes
        search_combo = ttk.Combobox(search_frame, font = ("Sans Serif", 12), state = "readonly", width = 10)
        search_combo["values"] = ("Select", "Name", "ID", "Email")
        search_combo.current(0)
        search_combo.grid(row = 0, column = 1, padx = 2, pady = 5, sticky = W)
        ### Entry Fields
        search_entry = ttk.Entry(search_frame, width = 15, font = ("Sans Serif", 12))
        search_entry.grid(row = 0, column = 2, pady = 5, sticky = W)
        ### Buttons
        searchbtn = Button(search_frame, text = "Search", width = 10, font = ("Sans Serif", 12), bg = "aqua", fg = "black")
        searchbtn.grid(row = 0, column = 3, padx = 2)
        showallbtn = Button(search_frame, text = "Show All", width = 10, font = ("Sans Serif", 12), bg = "aqua", fg = "black")
        showallbtn.grid(row = 0, column = 4, padx = 2)

        # ===== Table Frame ====
        table_frame = LabelFrame(Right_frame, bd = 2, bg = "white", relief = RIDGE)
        table_frame.place(x = 5, y = 120, width = 565, height = 300)
    
        Scroll_x = ttk.Scrollbar(table_frame, orient = HORIZONTAL)
        Scroll_y = ttk.Scrollbar(table_frame, orient = VERTICAL)
        self.student_table = ttk.Treeview(table_frame, column = ("Student ID", "Student Name", "Email", "Address", "Parents Name", "Parents Number"), xscrollcommand = Scroll_x.set, yscrollcommand = Scroll_y.set)
        Scroll_x.pack(side = BOTTOM, fill = X)
        Scroll_y.pack(side = RIGHT, fill = Y)
        Scroll_x.config(command = self.student_table.xview)
        Scroll_y.config(command = self.student_table.yview)
        self.student_table.heading("Student ID", text = "Student ID")
        self.student_table.heading("Student Name", text = "Student Name")
        self.student_table.heading("Email", text = "Email")
        self.student_table.heading("Address", text = "Address")
        self.student_table.heading("Parents Name", text = "Parents Name")
        self.student_table.heading("Parents Number", text = "Parents Number")
        self.student_table["show"] = "headings"

        self.student_table.column("Student ID", width = 100)
        self.student_table.column("Student Name", width = 100)
        self.student_table.column("Email", width = 100)
        self.student_table.column("Address", width = 100)
        self.student_table.column("Parents Name", width = 100)
        self.student_table.column("Parents Number", width = 100)

        self.student_table.pack(fill = BOTH, expand = 1)

        #### Function Declaration #####
    def add_data(self):
        if self.var_course.get() == "Select Course" or self.var_sName.get() == "" or self.var_sID.get() == "":
            messagebox.showerror("Error", "All fields required", parent = self.root)
        else:
            pass







if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()