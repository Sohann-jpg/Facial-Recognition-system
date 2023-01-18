from tkinter import * 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2 
import os 
import csv
from tkinter import filedialog

mydata = []
# Making a class that initiates the backend application of the project
class Attendance:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

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
        f_lbl = Label(self.root, image = self.photoimg)
        f_lbl.place(x= -1, y=0)
        # Adding a background image to the application software
        img1 = Image.open(r"App-Images\Background.webp")
        img1 = img1.resize((1530, 710), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        bg_img = Label(self.root, image = self.photoimg1)
        bg_img.place(x = 0, y = 130, width = 1530, height = 710)
        # Adding a text in the application
        title_lbl = Label(bg_img,text = "Attendance Management System", font = ("open sans", 30), bg = "white", fg = "Black")
        title_lbl.place(x = -100, y = 0, width = 1530, height = 40)
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
        fln = filedialog.askopenfilename(initialdir = os.getcwd(), title = "Open CSV", filetypes = (("CSV FILE", "*.csv"), ("All File", "*.*")), parent = self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile, delimiter = ",")
            for i in csvread:
                mydata.append(i)
            self.fetch_data(mydata)   

    # export CSV
    def exportCSV(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("Error", "No data to export", parent = self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir = os.getcwd(), title = "Open CSV", filetypes = (("CSV FILE", "*.csv"), ("All File", "*.*")), parent = self.root)
            with open(fln, mode = "w", newline = "") as myfile:
                exp_write = csv.writer(myfile, delimiter = ",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Success", "Data exported successfully to " + os.path.basename(fln))
        except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent = self.root)


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




















if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()