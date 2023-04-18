from tkinter import * 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from tkcalendar import DateEntry
import mysql.connector
# Making a class that initiates the backend application of the project
class Student:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        ####Variables####
        self.var_sID = StringVar()
        self.var_date = StringVar()
        self.var_time = StringVar()
        self.var_name = StringVar()
        self.var_course = StringVar()
        self.var_attenstats = StringVar()

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
        # ====== Information section =====
        # Course Info label
        # Class Info label
        class_student_frame = LabelFrame(main_frame, bd = 2, bg = "white", relief = RIDGE, text = "Class Student Information", font = ("Sans Serif", 12))
        class_student_frame.place(x = 5, y = 0, width = 600, height = 460)

        # Student ID
        studentID_label = Label(class_student_frame, text = "Student ID:", font = ("Sans Serif", 12), bg = "white")
        studentID_label.grid(row = 0, column = 0, sticky = W)
        studentID_entry = ttk.Entry(class_student_frame, textvariable= self.var_sID, width = 15, font = ("Sans Serif", 12))
        studentID_entry.grid(row = 0, column = 1, pady = 5, sticky = W)

        # TIme
        Time_label = Label(class_student_frame, text = "Time:", font = ("Sans Serif", 12), bg = "white")
        Time_label.grid(row = 1, column = 0, sticky = W)
        Time_entry = ttk.Entry(class_student_frame, textvariable= self.var_time, width = 15, font = ("Sans Serif", 12))
        Time_entry.grid(row = 1, column = 1, pady = 5, sticky = W)

        # name
        name_label = Label(class_student_frame, text = "Name:", font = ("Sans Serif", 12), bg = "white")
        name_label.grid(row = 2, column = 0, sticky = W)
        name_entry = ttk.Entry(class_student_frame, textvariable= self.var_name, width = 15, font = ("Sans Serif", 12))
        name_entry.grid(row = 2, column = 1, pady = 5, sticky = W)

        # course
        course_label = Label(class_student_frame, text = "Course:", font = ("Sans Serif", 12), bg = "white")
        course_label.grid(row = 4, column = 0, sticky = W)
        # course Combo box
        course_combo = ttk.Combobox(class_student_frame, textvariable = self.var_course, font = ("Sans Serif", 12), state = "readonly", width = 13)
        course_combo["values"] = ("Select Course", "BIT", "BIM", "BBM")
        course_combo.current(0)
        course_combo.grid(row = 4, column = 1, pady = 5, sticky = W)

        #Attendance Status
        attendance_label = Label(class_student_frame, text = "Attendance Satus:", font = ("Sans Serif", 12), bg = "white")
        attendance_label.grid(row = 1, column = 2, sticky = W)
        # Attendance Combo box
        attendance_combo = ttk.Combobox(class_student_frame, textvariable = self.var_attenstats, font = ("Sans Serif", 12), state = "readonly", width = 14)
        attendance_combo["values"] = ("Attendance Status", "Present", "Absent")
        attendance_combo.current(0)
        attendance_combo.grid(row = 1, column = 3, pady = 5, sticky = W)

        # Date 
        date_label = Label(class_student_frame, text = "Date:", font = ("Sans Serif", 12), bg = "white")
        date_label.grid(row = 0, column = 2, padx = 5,  sticky = W)
        cal = DateEntry(class_student_frame, width= 20, textvariable = self.var_date, background='darkblue', foreground='white', borderwidth=2)
        cal.grid(row=0, column = 3, padx= 5, sticky = W)


        # ===== Functional Buttons 1.0 =====
        # Buttons Frame
        btn_frame = Frame(class_student_frame, bd = 2, relief = RAISED, bg = "white")
        btn_frame.place(x = 3, y = 400, width = 592, height = 37)

        # Update
        updatebtn = Button(btn_frame, text = "Update", command = self.update_student_table, width = 13, font = ("Sans Serif", 12), bg = "#117c9d", fg = "black")
        updatebtn.place(x = 0, y = 0, width= 198)

        # # Delete 
        export_csv_btn = Button(btn_frame, text = "Delete", command = self.delete_data, width = 13, font = ("Sans Serif", 12), bg = "#117c9d", fg = "black")
        export_csv_btn.place(x = 200, y = 0, width= 198)

        # Reset
        resetbtn = Button(btn_frame, text = "Reset", command = self.reset_data, width = 13, font = ("Sans Serif", 12), bg = "#117c9d", fg = "black")
        resetbtn.place(x = 400, y = 0, width= 198)
        # ===== Functional Buttons 1.0 =====

        # ===== Functional Buttons 1.1 =====
    
        # Right label frame
        Right_frame = LabelFrame(main_frame, bd = 2, bg = "white", relief = RAISED, text = "Student Information", font = ("Sans Serif", 12))
        Right_frame.place(x = 630, y = 10, width = 580, height = 450)

        # ===== Table Frame ====
        table_frame = Frame(Right_frame, bd = 2, bg = "white", relief = RIDGE)
        table_frame.place(x = 5, y = 10, width = 565, height = 420)

        # ===== Scroll bar =====
        Scroll_x = ttk.Scrollbar(table_frame, orient = HORIZONTAL)
        Scroll_y = ttk.Scrollbar(table_frame, orient = VERTICAL)
        # ===== Scroll bar =====

        # ===== Table Contents =====
        self.student_table = ttk.Treeview(table_frame, column = ("Student ID", "Name", "Course", "Time", "Date", "Attendance Status"), xscrollcommand = Scroll_x.set, yscrollcommand = Scroll_y.set)
        Scroll_x.pack(side = BOTTOM, fill = X)
        Scroll_y.pack(side = RIGHT, fill = Y)
        Scroll_x.config(command = self.student_table.xview)
        Scroll_y.config(command = self.student_table.yview)     
        self.student_table.heading("Student ID", text = "Student ID")
        self.student_table.heading("Name", text = "Name")
        self.student_table.heading("Course", text = "Course")
        self.student_table.heading("Time", text = "Time")
        self.student_table.heading("Date", text = "Date")
        self.student_table.heading("Attendance Status", text = "Attendance Status")
        self.student_table["show"] = "headings"

        self.student_table.column("Student ID", width = 100)
        self.student_table.column("Name", width = 100)
        self.student_table.column("Course", width = 100)
        self.student_table.column("Time", width = 100)
        self.student_table.column("Date", width = 100)
        self.student_table.column("Attendance Status", width = 100)
        self.student_table.pack(fill = BOTH, expand = 1)
        self.student_table.bind("<ButtonRelease>")
        # ===== Table Contents =====

    def reset_data(self):
        self.var_sID.set("")
        self.var_name.set("")
        self.var_course.set("")
        self.var_date.set("Date")
        self.var_time.set("")
        self.var_attenstats.set("")

    def update_student_table(self):
        std_ID = self.var_sID.get()
        name = self.var_name.get()
        Course = self.var_course.get()
        Date = self.var_date.get()
        Time = self.var_time.get()
        attendance_status = self.var_attenstats.get()
        # Insert the data into the treeview
        self.student_table.insert("", "end", values=(std_ID, name, Course, Date, Time, attendance_status))
        if self.var_name.get() == "" or self.var_time.get() == "" or self.var_sID.get() == "":
            messagebox.showerror("Error", "All fields required", parent = self.root)
        else:
            try:
                Update = messagebox.askyesno("update", "Do you want to update the attendance?", parent = self.root)
                if Update > 0:
                    conn = mysql.connector.connect(host = "localhost", username = "root", password = "PunnSxG@2806", database = "face_recognition")
                    my_cursor = conn.cursor()
                    my_cursor.execute("insert into attendance values(%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_sID.get(),
                                                                                        self.var_name.get(),
                                                                                        self.var_course.get(),
                                                                                        self.var_time.get(),
                                                                                        self.var_date.get(),
                                                                                        self.var_attenstats.get()                                                                                    
                                                                                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success", "Attendance successfully updated", parent = self.root)
                conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent = self.root)

    def delete_data(self):
        if self.var_sID.get() == "":
            messagebox.showerror("Error", "Student ID required", parent = self.root)
        else:
            try:
                delete = messagebox.askyesno("Student Delete Page", "Do you really want to delete this entry?", parent = self.root)
                if delete > 0:
                    conn = mysql.connector.connect(host = "localhost", username = "root", password = "PunnSxG@2806", database = "face_recognition")
                    my_cursor = conn.cursor()
                    sql = "delete from attendance where student_id = %s"
                    val = (self.var_sID.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not delete:
                        return
                conn.commit()
                conn.close()
                messagebox.showinfo("Delete", "Successfully deleted entry", parent = self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent = self.root)

if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
