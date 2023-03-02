from tkinter import * 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from tkcalendar import DateEntry
import csv
import os
# Making a class that initiates the backend application of the project
class Student:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        ####Variables####
        self.var_level = StringVar()
        self.var_sID = StringVar()
        self.var_date = StringVar()
        self.var_Time = StringVar()
        self.var_tutorID = StringVar()
        self.var_roomID = StringVar()
        self.var_module_code = StringVar()

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
        Time_entry = ttk.Entry(class_student_frame, textvariable= self.var_Time, width = 15, font = ("Sans Serif", 12))
        Time_entry.grid(row = 1, column = 1, pady = 5, sticky = W)

        # Level
        level_label = Label(class_student_frame, text = "Level:", font = ("Sans Serif", 12), bg = "white")
        level_label.grid(row = 2, column = 0, sticky = W)
        # Level Combo box
        level_combo = ttk.Combobox(class_student_frame, textvariable = self.var_level, font = ("Sans Serif", 12), state = "readonly", width = 13)
        level_combo["values"] = ("Select Level", "1", "2", "3", "4", "5", "6")
        level_combo.current(0)
        level_combo.grid(row = 2, column = 1, pady = 3, sticky = W)

        # Tutor ID
        tutor_ID_label = Label(class_student_frame, text = "Tutor ID:", font = ("Sans Serif", 12), bg = "white")
        tutor_ID_label.grid(row = 3, column = 0, sticky = W)
        tutor_ID_entry = ttk.Entry(class_student_frame, textvariable= self.var_tutorID, width = 15, font = ("Sans Serif", 12))
        tutor_ID_entry.grid(row = 3, column = 1, pady = 5, sticky = W)

        # Room ID
        room_ID_label = Label(class_student_frame, text = "Room ID:", font = ("Sans Serif", 12), bg = "white")
        room_ID_label.grid(row = 4, column = 0, sticky = W)
        room_ID_entry = ttk.Entry(class_student_frame, textvariable= self.var_roomID, width = 15, font = ("Sans Serif", 12))
        room_ID_entry.grid(row = 4, column = 1, pady = 5, sticky = W)

        # Date 
        date_label = Label(class_student_frame, text = "Date:", font = ("Sans Serif", 12), bg = "white")
        date_label.grid(row = 0, column = 2, padx = 5,  sticky = W)
        cal = DateEntry(class_student_frame, width= 20, textvariable = self.var_date, background='darkblue', foreground='white', borderwidth=2)
        cal.grid(row=0, column = 3, padx= 5, sticky = W)

        # Module Code
        module_code_label = Label(class_student_frame, text = 'Module Code: ', font = ("Sans Serif", 12), bg = "white")
        module_code_label.grid(row = 1, column = 2, padx = 5,  sticky = W)
        module_code_entry = ttk.Entry(class_student_frame, textvariable= self.var_module_code, width = 15, font = ("Sans Serif", 12))
        module_code_entry.grid(row = 1, column = 3, padx = 5, sticky = W)

        # ===== Functional Buttons 1.0 =====
        # Buttons Frame
        btn_frame = Frame(class_student_frame, bd = 2, relief = RAISED, bg = "white")
        btn_frame.place(x = 3, y = 400, width = 592, height = 37)

        # Update
        updatebtn = Button(btn_frame, text = "Update", command = self.update_student_table, width = 13, font = ("Sans Serif", 12), bg = "#117c9d", fg = "black")
        updatebtn.place(x = 0, y = 0, width= 198)

        # Delete 
        export_csv_btn = Button(btn_frame, text = "Export CSV", command = self.export_student_data, width = 13, font = ("Sans Serif", 12), bg = "#117c9d", fg = "black")
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
        self.student_table = ttk.Treeview(table_frame, column = ("Student ID", "Date", "Time", "Module Code", "Level", "Tutor ID", "Room ID"), xscrollcommand = Scroll_x.set, yscrollcommand = Scroll_y.set)
        Scroll_x.pack(side = BOTTOM, fill = X)
        Scroll_y.pack(side = RIGHT, fill = Y)
        Scroll_x.config(command = self.student_table.xview)
        Scroll_y.config(command = self.student_table.yview)     
        self.student_table.heading("Student ID", text = "Student ID")
        self.student_table.heading("Date", text = "Date")
        self.student_table.heading("Time", text = "Time")
        self.student_table.heading("Module Code", text = "Module Code")
        self.student_table.heading("Level", text = "Level")
        self.student_table.heading("Tutor ID", text = "Tutor ID")
        self.student_table.heading("Room ID", text = "Room ID")
        self.student_table["show"] = "headings"

        self.student_table.column("Student ID", width = 100)
        self.student_table.column("Date", width = 100)
        self.student_table.column("Time", width = 100)
        self.student_table.column("Module Code", width = 100)
        self.student_table.column("Level", width = 100)
        self.student_table.column("Tutor ID", width = 100)
        self.student_table.column("Room ID", width = 100)
        self.student_table.pack(fill = BOTH, expand = 1)
        self.student_table.bind("<ButtonRelease>")
        # self.fetch_data()
        # ===== Table Contents =====

    def update_student_table(self):
        level = self.var_level.get()
        std_ID = self.var_sID.get()
        Date = self.var_date.get()
        Time = self.var_Time.get()
        t_ID = self.var_tutorID.get()
        r_ID = self.var_roomID.get()
        m_code = self.var_module_code.get()
        # Insert the data into the treeview
        self.student_table.insert("", "end", values=(std_ID, Date, Time, m_code, level, t_ID, r_ID))

    def reset_data(self):
        self.var_sID.set("")
        self.var_date.set("Date")
        self.var_Time.set("")
        self.var_level.set("Select Level")
        self.var_tutorID.set("")
        self.var_roomID.set("")
        self.var_module_code.set("")

    def export_student_data(self):
        file_exists = os.path.isfile("student_data.csv")
        # Open a file for writing
        with open("student_data.csv", "a", newline="") as file:
            writer = csv.writer(file)
            
            # Write the header row
            if not file_exists:
                writer.writerow(["Student ID", "Date", "Time", "Module Code", "Level", "Tutor ID", "Room ID"])
            
            # Write each row of data from the treeview
            for row in self.student_table.get_children():
                std_ID = self.student_table.item(row, "values")[0]
                Date = self.student_table.item(row, "values")[1]
                Time = self.student_table.item(row, "values")[2]
                m_code = self.student_table.item(row, "values")[3]
                level = self.student_table.item(row, "values")[4]
                t_ID = self.student_table.item(row, "values")[5]
                r_ID = self.student_table.item(row, "values")[6]
                writer.writerow([std_ID, Date, Time, m_code, level, t_ID, r_ID])
        try:
            messagebox.showinfo("Export CSV", "CSV file exported successfully!")
        except:
            messagebox.showerror("Export CSV", "Error exporting CSV file.")

if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()