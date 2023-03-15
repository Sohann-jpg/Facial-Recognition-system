from tkinter import * 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2 

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
        self.var_radio1 = StringVar()


        # ===== Header and background images =====
        img = Image.open(r"App-Images\Header.jpg")
        img = img.resize((1300, 130), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root, image = self.photoimg)
        f_lbl.place(x= -1, y=0)
        # Adding a background image to the application software
        img1 = Image.open(r"App-Images\Background.webp")
        img1 = img1.resize((1530, 710), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        bg_img = Label(self.root, image = self.photoimg1)
        bg_img.place(x = 0, y = 130, width = 1530, height = 710)
        # Adding a text in the application
        title_lbl = Label(bg_img,text = "Student Details", font = ("open sans", 30), bg = "white", fg = "Black")
        title_lbl.place(x = -100, y = 0, width = 1530, height = 40)
        # ===== Header and background images =====

        # ===== Work Frames =====
        #Adding a frame
        main_frame = Frame(bg_img, bd = 2, bg = "white")
        main_frame.place(x = 25, y = 50, width = 1230, height = 480)
        # left label frame
        Left_frame = LabelFrame(main_frame, bd = 2, bg = "white", relief = RAISED, text = "Student Details", font = ("Sans Serif", 12))
        Left_frame.place(x = 10, y = 10, width = 580, height = 450)
    
        # ====== Information section =====
        # Course Info label
        Course_frame = LabelFrame(Left_frame, bd = 2, bg = "white", relief = RIDGE, text = "Current Course", font = ("Sans Serif", 12))
        Course_frame.place(x = 5, y = 10, width = 565, height = 100)
        # Course
        dep_label = Label(Course_frame, text = "Course:", font = ("Sans Serif", 12), bg = "white")
        dep_label.grid(row = 0, column = 0, padx = 5, sticky = W)
        # Course Combo box
        dep_combo = ttk.Combobox(Course_frame, textvariable = self.var_course, font = ("Sans Serif", 12), state = "readonly", width = 15)
        dep_combo["values"] = ("Select Course", "BIT", "BBM", "IMBA")
        dep_combo.current(0)
        dep_combo.grid(row = 0, column = 1, padx = 2, pady = 5, sticky = W)

        # Year
        year_label = Label(Course_frame, text = "Year:", font = ("Sans Serif", 12), bg = "white")
        year_label.grid(row = 0, column = 2, padx = 5, sticky = W)
        # Year Combo box
        year_combo = ttk.Combobox(Course_frame, textvariable = self.var_year, font = ("Sans Serif", 12), state = "readonly", width = 15)
        year_combo["values"] = ("Select Year", "2022-2023", "2023-2024", "2024-2025")
        year_combo.current(0)
        year_combo.grid(row = 0, column = 3, padx = 2, pady = 5, sticky = W)

        # Semester
        semester_label = Label(Course_frame, text = "Semester:", font = ("Sans Serif", 12), bg = "white")
        semester_label.grid(row = 1, column = 0, padx = 5, sticky = W)
        # Semester Combo box
        semester_combo = ttk.Combobox(Course_frame, textvariable = self.var_semester, font = ("Sans Serif", 12), state = "readonly", width = 15)
        semester_combo["values"] = ("Select Semester", "Fall", "Spring")
        semester_combo.current(0)
        semester_combo.grid(row = 1, column = 1, padx = 2, pady = 5, sticky = W)

        # Level
        level_label = Label(Course_frame, text = "Level:", font = ("Sans Serif", 12), bg = "white")
        level_label.grid(row = 1, column = 2, padx = 5, sticky = W)
        # Level Combo box
        level_combo = ttk.Combobox(Course_frame, textvariable = self.var_level, font = ("Sans Serif", 12), state = "readonly", width = 15)
        level_combo["values"] = ("Select Level", "1", "2", "3", "4", "5", "6")
        level_combo.current(0)
        level_combo.grid(row = 1, column = 3, padx = 2, pady = 5, sticky = W)

        #Note: IF the cell is larger than the Widget, the Sticky = W will minimize the problem
        
        # Class Info label
        class_student_frame = LabelFrame(Left_frame, bd = 2, bg = "white", relief = RIDGE, text = "Class Student Information", font = ("Sans Serif", 12))
        class_student_frame.place(x = 5, y = 120, width = 565, height = 300)

        # Student ID
        studentID_label = Label(class_student_frame, text = "Student ID:", font = ("Sans Serif", 12), bg = "white")
        studentID_label.grid(row = 0, column = 0, sticky = W)
        studentID_entry = ttk.Entry(class_student_frame, textvariable= self.var_sID, width = 15, font = ("Sans Serif", 12))
        studentID_entry.grid(row = 0, column = 1, pady = 5, sticky = W)

        # Student Name
        studentName_label = Label(class_student_frame, text = "Student Name:", font = ("Sans Serif", 12), bg = "white")
        studentName_label.grid(row = 1, column = 0, sticky = W)
        studentName_entry = ttk.Entry(class_student_frame, textvariable= self.var_sName, width = 15, font = ("Sans Serif", 12))
        studentName_entry.grid(row = 1, column = 1, pady = 5, sticky = W)

        # Gender
        studentGender_label = Label(class_student_frame, text = "Gender:", font = ("Sans Serif", 12), bg = "white")
        studentGender_label.grid(row = 2, column = 0, sticky = W)
        # Gender Combo box
        gender_combo = ttk.Combobox(class_student_frame, textvariable = self.var_gender, font = ("Sans Serif", 12), state = "readonly", width = 13)
        gender_combo["values"] = ("Male", "Female", "Non-Binary")
        gender_combo.current(0)
        gender_combo.grid(row = 2, column = 1, pady = 3, sticky = W)

        # Email
        studentEmail_label = Label(class_student_frame, text = "Email:", font = ("Sans Serif", 12), bg = "white")
        studentEmail_label.grid(row = 3, column = 0, sticky = W)
        studentEmail_entry = ttk.Entry(class_student_frame, textvariable= self.var_email, width = 15, font = ("Sans Serif", 12))
        studentEmail_entry.grid(row = 3, column = 1, pady = 5, sticky = W)

        # Parents Name
        studentParentsName_label = Label(class_student_frame, text = "Parents Name:", font = ("Sans Serif", 12), bg = "white")
        studentParentsName_label.grid(row = 4, column = 0, sticky = W)
        studentParentsName_entry = ttk.Entry(class_student_frame, textvariable= self.var_pName, width = 15, font = ("Sans Serif", 12))
        studentParentsName_entry.grid(row = 4, column = 1, pady = 5, sticky = W)

        # Address 
        studentAddress_label = Label(class_student_frame, text = "Address:", font = ("Sans Serif", 12), bg = "white")
        studentAddress_label.grid(row = 0, column = 2, padx = 5,  sticky = W)
        studentAddress_entry = ttk.Entry(class_student_frame, textvariable= self.var_address, width = 15, font = ("Sans Serif", 12))
        studentAddress_entry.grid(row = 0, column = 3, padx = 5, sticky = W)

        # Parents Number
        Pn_label = Label(class_student_frame, text = 'Parents Number: ', font = ("Sans Serif", 12), bg = "white")
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
        btn_frame = Frame(class_student_frame, bd = 2, relief = RAISED, bg = "white")
        btn_frame.place(x = 3, y =200, width = 555, height = 37)

        # Save
        savebtn = Button(btn_frame, text = "Save", command = self.add_data, width = 13, font = ("Sans Serif", 12), bg = "aqua", fg = "black")
        savebtn.grid(row = 0, column = 0, padx= 5)

        # Update
        updatebtn = Button(btn_frame, text = "Update", command = self.update_data, width = 13, font = ("Sans Serif", 12), bg = "aqua", fg = "black")
        updatebtn.grid(row = 0, column = 1, padx= 5)

        # Delete 
        deletebtn = Button(btn_frame, text = "Delete", command = self.delete_data, width = 13, font = ("Sans Serif", 12), bg = "aqua", fg = "black")
        deletebtn.grid(row = 0, column = 2, padx= 5)

        # Reset
        resetbtn = Button(btn_frame, text = "Reset", command = self.reset_data, width = 13, font = ("Sans Serif", 12), bg = "aqua", fg = "black")
        resetbtn.grid(row = 0, column = 3, padx= 5)
        # ===== Functional Buttons 1.0 =====

        # ===== Functional Buttons 1.1 =====
        btn_frame1 = Frame(class_student_frame, bd = 2, relief = RAISED, bg = "white")
        btn_frame1.place(x = 3, y =235, width = 555, height = 37)

        # Take Photo
        takephbtn = Button(btn_frame1, command = self.generate_dataset, text = "Take photo sample", width = 29, font = ("Sans Serif", 12), bg = "aqua", fg = "black")
        takephbtn.grid(row = 0, column = 2)
        # Update Photo
        updatephbtn = Button(btn_frame1, text = "Update photo sample", width = 29, font = ("Sans Serif", 12), bg = "aqua", fg = "black")
        updatephbtn.grid(row = 0, column = 3)
         # ===== Functional Buttons 1.1 =====


        # Right label frame
        Right_frame = LabelFrame(main_frame, bd = 2, bg = "white", relief = RAISED, text = "Student Details", font = ("Sans Serif", 12))
        Right_frame.place(x = 630, y = 10, width = 580, height = 450)

        #=====Search Frame=====
        search_frame = LabelFrame(Right_frame, bd = 2, bg = "white", relief = RIDGE, text = "Search", font = ("Sans Serif", 12))
        search_frame.place(x = 5, y = 10, width = 565, height = 70)
        search_label = Label(search_frame, text = "Search By: ", font = ("Sans Serif", 12), bg = "white")
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
        searchbtn = Button(search_frame, text = "Search", width = 10, font = ("Sans Serif", 12), bg = "aqua", fg = "black")
        searchbtn.grid(row = 0, column = 3, padx = 2)
        showallbtn = Button(search_frame, text = "Show All", width = 10, font = ("Sans Serif", 12), bg = "aqua", fg = "black")
        showallbtn.grid(row = 0, column = 4, padx = 2)

        # ===== Table Frame ====
        table_frame = Frame(Right_frame, bd = 2, bg = "white", relief = RIDGE)
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
            messagebox.showerror("Error", "All fields required", parent = self.root)
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
                messagebox.showinfo("success","student details has been added successfully", parent = self.root)            
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent = self.root)

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
            messagebox.showerror("Error", "All fields required", parent = self.root)
        else:
            try:
                Update = messagebox.askyesno("update", "Do you want to update the data?", parent = self.root)
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
                messagebox.showinfo("Success", "Student student successfully updated", parent = self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent = self.root)
# ===== Update =====


# ===== Delete =====
    def delete_data(self):
        if self.var_sID.get() == "":
            messagebox.showerror("Error", "Student ID required", parent = self.root)
        else:
            try:
                delete = messagebox.askyesno("Student Delete Page", "Do you really want to delete this entry?", parent = self.root)
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
                messagebox.showinfo("Delete", "Successfully deleted entry", parent = self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent = self.root)
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
# === This section of the code uses OpenCV to capture video from the device's camera and detect faces in the frames 
# using the pre-trained Haar cascade classifier "haarcascade_frontalface_default.xml". 
# The detected faces are then cropped from the frames and resized to 450x450 pixels. 
# The cropped and resized images are then saved to the "data" folder with filenames in the format "user.id.img_id.jpg".
#  The code continues to capture and save images until the user presses the enter key or 100 images have been captured. 
#  A message box is displayed at the end of the process to confirm that the dataset has been generated successfully. 
#  If an exception occurs, an error message box is displayed with the specific error message. ===

##### Loading haarcascade library from openCV and 
# ===== Generating dataset and taking photo Sample =====
    def generate_dataset(self):
        if self.var_course.get() == "Select Course" or self.var_sName.get() == "" or self.var_sID.get() == "":
            messagebox.showerror("Error", "All fields required", parent = self.root)
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
                                                                                                                                                                                                                                self.var_sID.get() == id+1
                                                                                                                                                                                                                            ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    #### Scaling factor = 1.3
                    ### Minimun neighbor = 5
                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y+h, x:x+w]
                        return face_cropped
                    
                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+= 1
                        face = cv2.resize(face_cropped(my_frame), (450,450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = "Data/user." + str(id) + "." +str(img_id) + ".jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)
                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Success", "Generatimg Dataset Successful")
            except EXCEPTION as es:
                messagebox.showerror("Error", f"Due to:{str(es)}", parent = self.root)

if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
