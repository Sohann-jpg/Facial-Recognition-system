import tkinter as tk
from tkinter import ttk
from tkinter import * 
import tkinter
from PIL import Image,ImageTk
import mysql.connector
import cv2 
from tkinter import messagebox
import numpy as np
import os
import csv
from tkinter import filedialog
from time import strftime
from datetime import datetime
from tkcalendar import DateEntry

 
class Login(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_secQ = StringVar()
        self.var_secA = StringVar()
        self.var_pass = StringVar()
        self.var_conpass = StringVar()
        
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
        title_lbl = tk.Label(bg_img,text = "Login or register to continue", font = ("open sans", 30), 
        bg = "white", fg = "Black")
        title_lbl.place(x = -100, y = 0, width = 1530, height = 45)

        self.frame = Frame(bg_img, bg = '#0a384c')
        self.frame.place(x = 480, y = 70, width = 340, height = 450)
        user_img = Image.open("App-Images/user.png")
        user_img = user_img.resize((100, 100), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(user_img)
        lblimg1 = tk.Label(image = self.photoimage1, bg = "#117c9d", borderwidth = 1)
        lblimg1.place(x = 610, y = 220, width = 100, height = 100)

        get_str = tk.Label(self.frame, text = "Login", font = ("Helvetica", 20), fg = "white", bg = "#0a384c")
        get_str.place(x = 140, y = 130)

        # ===== Labels =====
        username = tk.Label(self.frame, text = "Username", font = ("Helvetica", 15), fg = "white", bg = "#0a384c")
        username.place(x = 48, y = 180)
        self.txtuser = ttk.Entry(self.frame, font = ("Helvetica", 20))
        self.txtuser.place(x = 50, y = 210, width = 200)

        password = tk.Label(self.frame, text = "Password", font = ("Helvetica", 15), fg = "white", bg = "#0a384c")
        password.place(x = 48, y = 270)
        self.txtpass = ttk.Entry(self.frame, show = "*", font = ("Helvetica", 20))
        self.txtpass.place(x = 50, y = 300, width = 200)

        # ===== Buttons
        loginbutton = tk.Button(self.frame, text = "Login", command = lambda: self.login(controller), font = ("Helvetica", 10), bd = 2, relief = RIDGE, bg = "#0a384c", fg = 'white',activebackground = '#0a384c')
        loginbutton.place(x = 100, y = 350, width = 120, height = 35)
        registerbutton = tk.Button(self.frame, text = "Register", command = lambda: controller.show_frame(Register), font = ("Helvetica", 10), borderwidth= 0, bg = "#0a384c", activebackground = '#0a384c')
        registerbutton.place(x = -15, y = 390, width = 120)
        forgotbutton = tk.Button(self.frame, text = "Forgot Password", command = self.forgot_password, font = ("Helvetica", 10), borderwidth= 0, bg = "#0a384c", activebackground = '#0a384c')
        forgotbutton.place(x = 10, y = 420, width = 120)

    def reg_window(self, controller):
        self.new_window = Toplevel(self.root)
        controller.show_frame(Register) 

    def login(self, controller):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "All fields required")
        elif self.txtuser.get() == "Sohan" and self.txtpass.get() == "213":
            messagebox.showinfo("Success", "Welcome")
        else:
            conn = mysql.connector.connect(host = "localhost", username = "root", password = "PunnSxG@2806", database = "face_recognition")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from users where email = %s and password = %s", (
                                                                                            self.txtuser.get(),
                                                                                            self.txtpass.get()
                                                                                    ))
            row = my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error", "Invalid username or password")
            else:
                command = lambda: controller.show_frame(Main)
                command()
            conn.commit()
            conn.close()

    #  sQuestion #sAnswer
    # ===== Function decleration for reset password =====
    def reset_pass(self):
        if self.combo_security_Q.get() == "Select":
            messagebox.showerror("Error", "Please select your security question", parent = self.root2)
        elif self.txt_security.get() == "":
            messagebox.showerror("Error", "Please select your answer", parent = self.root2)
        elif self.txt_newpass.get() == "":
            messagebox.showerror("Error", "Please select the new password", parent = self.root2)
        else:
            conn = mysql.connector.connect(host = "localhost", username = "root", password = "PunnSxG@2806", database = "face_recognition")
            my_cursor = conn.cursor()
            query = ("select * from users where email = %s and securityQ = %s and securityA = %s")
            value = (self.txtuser.get(), self.combo_security_Q.get(), self.txt_security.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error", "Please enter correct answer", parent = self.root2)
            else:
                query = ("update users set password = %s where email = %s")
                value = (self.txt_newpass.get(), self.txtuser.get())
                my_cursor.execute(query, value)
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Your password has been successfully reset", parent = self.root2)   
                self.root2.destroy()         
# ===== Function decleration for reset password =====

# ===== Forgot Password =====
    def forgot_password(self):
        if self.txtuser.get() == "":
            messagebox.showerror("Error", "Please enter email to reset your password")
        else:
            conn = mysql.connector.connect(host = "localhost", username = "root", password = "PunnSxG@2806", database = "face_recognition")
            my_cursor = conn.cursor()
            query = ("select * from users where email = %s")
            value = (self.txtuser.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error", "Please provide a valid email")
            else:
                conn.close()
                self.root2 = Toplevel()
                self.root2.title("Reset Password")
                self.root2.geometry("340x450+610+170")
                self.root2.resizable(0,0)
                fplbl = tk.Label(self.root2, text = "Forgot Password", font = ("Helvetica", 10))
                fplbl.place(x = 0, y = 10, relwidth = 1)
                # Security Question
                security_Q = tk.Label(self.root2, text = "Security Question", font = ("Sans Serif", 12))
                security_Q.place(x = 50, y = 80)
                self.combo_security_Q = ttk.Combobox(self.root2, text = "Security Question", textvariable = self.var_secQ, font = ("Sans Serif", 12), state = "readonly")
                self.combo_security_Q["values"] = ("Select","Name of your first pet", "City you were born", "Your first school")
                self.combo_security_Q.place(x = 50, y = 110, width = 250)
                self.combo_security_Q.current(0)

                security_A = tk.Label(self.root2, text = "Security Answer", font = ("Sans Serif", 12))
                security_A.place(x = 50, y = 150)
                self.txt_security = ttk.Entry(self.root2, textvariable = self.var_secA, font = ("Sans Serif", 12))
                self.txt_security.place(x = 50, y = 180, width = 250)

                new_password = tk.Label(self.root2, text = "New Password:", font = ("Sans Serif", 12))
                new_password.place(x = 50, y = 220)
                self.txt_newpass= ttk.Entry(self.root2, width = 15, font = ("Sans Serif", 12))
                self.txt_newpass.place(x = 50, y = 250, width = 250)

                btn = tk.Button(self.root2, text = "Reset", font = ("Sans Serif", 12), command = self.reset_pass, bd = 2, relief = RIDGE, bg = "#0a384c", fg = 'white',activebackground = '#0a384c')
                btn.place(x = 50, y = 300, width = 250)
############################# End of Login Page #####################################################

class Register(tk.Frame):
    def __init__(self,parent, controller):
        tk.Frame.__init__(self, parent)
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_secQ = StringVar()
        self.var_secA = StringVar()
        self.var_pass = StringVar()
        self.var_conpass = StringVar()

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
        title_lbl = tk.Label(bg_img,text = "New User? Register", font = ("open sans", 30), 
        bg = "white", fg = "Black")
        title_lbl.place(x = -100, y = 0, width = 1530, height = 45)

       # ===== Work Frames =====
        #Adding a frame
        main_frame = tk.Frame(bg_img, bd = 2, bg = "white")
        main_frame.place(x = 25, y = 50, width = 1230, height = 480)
        # left label frame
        Left_frame = LabelFrame(main_frame, bd = 2, bg = "white", relief = RAISED, text = "Register Here", font = ("Sans Serif", 12))
        Left_frame.place(x = 10, y = 10, width = 580, height = 450)

        inside_left_frame = tk.Frame(Left_frame, bd = 2, relief = RIDGE, bg = "white")
        inside_left_frame.place(x = 5, y = 0, width = 560, height = 420)
        
        # ===== Lables and Entry Fields
        #  ROW 1
        fname = tk.Label(inside_left_frame, text = "First Name", font = ("Sans Serif", 12), bg = "white")
        fname.place(x = 5, y = 0)
        fname_entry = ttk.Entry(inside_left_frame, textvariable = self.var_fname, font = ("Sans Serif", 12))
        fname_entry.place(x = 5, y = 30, width = 250)

        lname = tk.Label(inside_left_frame, text = "Last Name", font = ("Sans Serif", 12), bg = "white")
        lname.place(x = 280, y = 0)
        lname_entry = ttk.Entry(inside_left_frame, textvariable = self.var_lname, font = ("Sans Serif", 12))
        lname_entry.place(x = 280, y = 30, width = 250)

        #  ROW 2
        contact = tk.Label(inside_left_frame, text = "Contact", font = ("Sans Serif", 12), bg = "white")
        contact.place(x = 5, y = 60)
        self.txt_contact = ttk.Entry(inside_left_frame, textvariable = self.var_contact, font = ("Sans Serif", 12))
        self.txt_contact.place(x = 5, y = 90, width = 250)

        email = tk.Label(inside_left_frame, text = "Email", font = ("Sans Serif", 12), bg = "white")
        email.place(x = 280, y = 60)
        self.txt_email = ttk.Entry(inside_left_frame, textvariable = self.var_email, font = ("Sans Serif", 12))
        self.txt_email.place(x = 280, y = 90, width = 250)

        #  ROW 3
        security_Q = tk.Label(inside_left_frame, text = "Security Question", font = ("Sans Serif", 12), bg = "white")
        security_Q.place(x = 5, y = 120)
        self.combo_security_Q = ttk.Combobox(inside_left_frame, text = "Security Question", textvariable = self.var_secQ, font = ("Sans Serif", 12), state = "readonly")
        self.combo_security_Q["values"] = ("Select","Name of your first pet", "City you were born", "Your first school")
        self.combo_security_Q.place(x = 5, y = 150, width = 250)
        self.combo_security_Q.current(0)

        security_A = tk.Label(inside_left_frame, text = "Security Answer", font = ("Sans Serif", 12), bg = "white")
        security_A.place(x = 280, y = 120)
        self.txt_security = ttk.Entry(inside_left_frame, textvariable = self.var_secA, font = ("Sans Serif", 12))
        self.txt_security.place(x = 280, y = 150, width = 250)

        # ROW 4
        pswd = tk.Label(inside_left_frame, text = "Password", font = ("Sans Serif", 12), bg = "white")
        pswd.place(x = 5, y = 180)
        self.txt_pswd = ttk.Entry(inside_left_frame, textvariable = self.var_pass, font = ("Sans Serif", 12))
        self.txt_pswd.place(x = 5, y = 210, width = 250)

        confirm_pswd = tk.Label(inside_left_frame, text = "Confirm Password", font = ("Sans Serif", 12), bg = "white")
        confirm_pswd.place(x = 280, y = 180)
        self.txt_confirm_pswd = ttk.Entry(inside_left_frame, textvariable = self.var_conpass, font = ("Sans Serif", 12))
        self.txt_confirm_pswd.place(x = 280, y = 210, width = 250)
        
        # ===== Functional Buttons 1.0 =====
        # Buttons Frame
        btn_frame = tk.Frame(inside_left_frame, bd = 2, relief = RAISED, bg = "white")
        btn_frame.place(x = 1, y = 372, width = 555, height = 37)

        # Register
        registerbtn = tk.Button(btn_frame, text = "Register user", command = self.register_user, width = 28, font = ("Sans Serif", 12), bg = "#117c9d", fg = "black")
        registerbtn.grid(row = 0, column = 0, padx= 5)

        # Login
        loginbtn = tk.Button(btn_frame, text = "Back to Login", command = lambda: controller.show_frame(Login), width = 29, font = ("Sans Serif", 12), bg = "#117c9d", fg = "black")
        loginbtn.grid(row = 0, column = 1, padx= 5)
        # ===== Functional Buttons 1.0 =====

    # Function decleration 
    def register_user(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_secQ.get() == "Select":
            messagebox.showerror("Error", "All fields required")
        elif self.var_pass.get() != self.var_conpass.get():
            messagebox.showerror("Error", "Password did not match")
        else:
            conn = mysql.connector.connect(host = "localhost", username = "root", password = "PunnSxG@2806", database = "face_recognition")
            my_cursor = conn.cursor()
            query = ("select * from users where email = %s")
            value = (self.var_email.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row != None:
                messagebox.showerror("Error", "User already exists. Try another email")
            else:
                my_cursor.execute("insert into users values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_secQ.get(),
                                                                                        self.var_secA.get(),
                                                                                        self.var_pass.get()                                                                        
                                                                                    ))
            conn.commit()
            conn.close()

            messagebox.showinfo("Success", "Registered Succesfully")
    def exit(self):
        self.exit = tkinter.messagebox.askyesno("Back to Login", "Are you sure you want to go back to login?", parent = self.root)
        if self.exit > 0:
            self.root.destroy()
        else:
            return
############################# End of Register Page #####################################################

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

        # Manual Attendance
        img5 = Image.open(r"App-Images\manual-atten.png")
        img5 = img5.resize((220, 220), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        b5 = tk.Button(bg_img, image = self.photoimg5)
        b5.place(x = 230, y = 300, width = 220, height = 180)

        # Manual Attendance
        b5_6 = tk.Button(bg_img, text = "Manual Attendance", cursor = "hand2", command = lambda: controller.show_frame(Manual), 
        font = ("open sans", 15), bg = "#117c9d", fg = "Black")
        b5_6.place(x = 230, y = 480, width = 220, height = 40)

        # Photos button
        img7 = Image.open(r"App-Images\Photos.jpg")
        img7 = img7.resize((220, 220), Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)
        b6 = tk.Button(bg_img, image = self.photoimg7)
        b6.place(x = 500, y = 300, width = 220, height = 180)
        # Text: Photos
        b6_6 = tk.Button(bg_img, text = "Photos", cursor = "hand2", command = self.open_img, 
        font = ("open sans", 15), bg = "#117c9d", fg = "Black")
        b6_6.place(x = 500, y = 480, width = 220, height = 40)
        
        # Logout
        img9 = Image.open(r"App-Images\Exit.jpg")
        img9 = img9.resize((220, 220), Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)
        b8 = tk.Button(bg_img, image = self.photoimg9)
        b8.place(x = 770, y = 300, width = 220, height = 180)

        # Text: Log Out
        b8_8 = tk.Button(bg_img, text = "Log Out", command=lambda: controller.show_frame(Login), cursor = "hand2", font = ("open sans", 15), 
        bg = "#117c9d", fg = "Black")
        b8_8.place(x = 770, y = 480, width = 220, height = 40)



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
        Right_frame = tk.LabelFrame(main_frame, bd = 2, bg = "white", relief = RAISED, text = "Student Information", font = ("Sans Serif", 12))
        Right_frame.place(x = 630, y = 10, width = 580, height = 450)

        # ===== Table Frame ====
        table_frame = tk.Frame(Right_frame, bd = 2, bg = "white", relief = RIDGE)
        table_frame.place(x = 5, y = 10, width = 565, height = 420)

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
        mydata = []
        fln = filedialog.askopenfilename(initialdir = os.getcwd(), title = "Open CSV", filetypes = (("CSV FILE", "*.csv"), ("All File", "*.*")), parent = self)
        with open(fln) as myfile:
            csvread = csv.reader(myfile, delimiter = ",")
            for i in csvread:
                mydata.append(i)
            self.fetch_data(mydata)   
        # export CSV
    def exportCSV(self):
        global mydata
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
                    cv2.putText(img, f"ID:{i}", (x, y - 55), cv2.FONT_ITALIC, 0.8, (255,255,255), 2)
                    cv2.putText(img, f"Name:{n}", (x, y - 30), cv2.FONT_ITALIC, 0.8, (255,255,255), 2)
                    cv2.putText(img, f"Course:{c}", (x, y - 5), cv2.FONT_ITALIC, 0.8, (255,255,255), 2)
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

class Manual(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
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
        # ====== Information section =====
        # Course Info label
        # Class Info label
        class_student_frame = LabelFrame(main_frame, bd = 2, bg = "white", relief = RIDGE, text = "Class Student Information", font = ("Sans Serif", 12))
        class_student_frame.place(x = 5, y = 0, width = 600, height = 460)

        # Student ID
        studentID_label = tk.Label(class_student_frame, text = "Student ID:", font = ("Sans Serif", 12), bg = "white")
        studentID_label.grid(row = 0, column = 0, sticky = W)
        studentID_entry = ttk.Entry(class_student_frame, textvariable= self.var_sID, width = 15, font = ("Sans Serif", 12))
        studentID_entry.grid(row = 0, column = 1, pady = 5, sticky = W)

        # TIme
        Time_label = tk.Label(class_student_frame, text = "Time:", font = ("Sans Serif", 12), bg = "white")
        Time_label.grid(row = 1, column = 0, sticky = W)
        Time_entry = ttk.Entry(class_student_frame, textvariable= self.var_Time, width = 15, font = ("Sans Serif", 12))
        Time_entry.grid(row = 1, column = 1, pady = 5, sticky = W)

        # Level
        level_label = tk.Label(class_student_frame, text = "Level:", font = ("Sans Serif", 12), bg = "white")
        level_label.grid(row = 2, column = 0, sticky = W)
        # Level Combo box
        level_combo = ttk.Combobox(class_student_frame, textvariable = self.var_level, font = ("Sans Serif", 12), state = "readonly", width = 13)
        level_combo["values"] = ("Select Level", "1", "2", "3", "4", "5", "6")
        level_combo.current(0)
        level_combo.grid(row = 2, column = 1, pady = 3, sticky = W)

        # Tutor ID
        tutor_ID_label = tk.Label(class_student_frame, text = "Tutor ID:", font = ("Sans Serif", 12), bg = "white")
        tutor_ID_label.grid(row = 3, column = 0, sticky = W)
        tutor_ID_entry = ttk.Entry(class_student_frame, textvariable= self.var_tutorID, width = 15, font = ("Sans Serif", 12))
        tutor_ID_entry.grid(row = 3, column = 1, pady = 5, sticky = W)

        # Room ID
        room_ID_label = tk.Label(class_student_frame, text = "Room ID:", font = ("Sans Serif", 12), bg = "white")
        room_ID_label.grid(row = 4, column = 0, sticky = W)
        room_ID_entry = ttk.Entry(class_student_frame, textvariable= self.var_roomID, width = 15, font = ("Sans Serif", 12))
        room_ID_entry.grid(row = 4, column = 1, pady = 5, sticky = W)

        # Date 
        date_label = tk.Label(class_student_frame, text = "Date:", font = ("Sans Serif", 12), bg = "white")
        date_label.grid(row = 0, column = 2, padx = 5,  sticky = W)
        cal = DateEntry(class_student_frame, width= 20, textvariable = self.var_date, background='darkblue', state = "readonly", foreground='white', borderwidth=2)
        cal.grid(row=0, column = 3, padx= 5, sticky = W)

        # Module Code
        module_code_label = tk.Label(class_student_frame, text = 'Module Code: ', font = ("Sans Serif", 12), bg = "white")
        module_code_label.grid(row = 1, column = 2, padx = 5,  sticky = W)
        module_code_entry = ttk.Entry(class_student_frame, textvariable= self.var_module_code, width = 15, font = ("Sans Serif", 12))
        module_code_entry.grid(row = 1, column = 3, padx = 5, sticky = W)

        # ===== Functional Buttons 1.0 =====
        # Buttons Frame
        btn_frame = tk.Frame(class_student_frame, bd = 2, relief = RAISED, bg = "white")
        btn_frame.place(x = 3, y = 400, width = 592, height = 37)

        # Update
        updatebtn = tk.Button(btn_frame, text = "Update", command = self.update_student_table, width = 13, font = ("Sans Serif", 12), bg = "#117c9d", fg = "black")
        updatebtn.place(x = 0, y = 0, width= 198)

        # Delete 
        export_csv_btn = tk.Button(btn_frame, text = "Export CSV", command = self.export_student_data, width = 13, font = ("Sans Serif", 12), bg = "#117c9d", fg = "black")
        export_csv_btn.place(x = 200, y = 0, width= 198)

        # Reset
        resetbtn = tk.Button(btn_frame, text = "Reset", command = self.reset_data, width = 13, font = ("Sans Serif", 12), bg = "#117c9d", fg = "black")
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
        file_exists = os.path.isfile("Manual Attendance.csv")
        # Open a file for writing
        with open("Manual Attendance.csv", "a", newline="") as file:
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
############################# End of Manual Attendance Page #####################################################
 
class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        window = tk.Frame(self)
        window.pack()

        window.grid_rowconfigure(0, minsize = 790)
        window.grid_columnconfigure(0, minsize = 1530)

        self.frames = {}
        for F in (Login, Register, Main, Student, Train, Attendance, Face_Recognition, Manual):
            frame = F(window, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")
        self.show_frame(Login)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()

app = Application()
app.mainloop()
