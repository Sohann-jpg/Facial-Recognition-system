from tkinter import *
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk  #pip install pillow
from tkinter import messagebox
from main import Face_Recognition_System
import mysql.connector

def main():
    win = Tk()
    app = Login_window(win)
    win.mainloop()
    
class Login_window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1530x790+0+0")
        # Variables
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
        f_lbl = Label(self.root, image = self.photoimg)
        f_lbl.place(x= -1, y=0)
        # Adding a background image to the application software
        img1 = Image.open(r"App-Images\Background.webp")
        img1 = img1.resize((1530, 710), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        bg_img = Label(self.root, image = self.photoimg1)
        bg_img.place(x = 0, y = 130, width = 1530, height = 710)
   # Adding a text in the application
        title_lbl = Label(bg_img,text = "Login or register to continue", font = ("open sans", 30), 
        bg = "white", fg = "Black")
        title_lbl.place(x = -100, y = 0, width = 1530, height = 45)

        self.frame = Frame(bg_img, bg = '#0a384c')
        self.frame.place(x = 480, y = 70, width = 340, height = 450)
        img1 = Image.open("App-Images/user.png")
        img1 = img1.resize((100, 100), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(image = self.photoimage1, bg = "#117c9d", borderwidth = 1)
        lblimg1.place(x = 610, y = 220, width = 100, height = 100)


        get_str = Label(self.frame, text = "Login", font = ("Helvetica", 20), fg = "white", bg = "#0a384c")
        get_str.place(x = 140, y = 130)


        # ===== Labels =====
        username = Label(self.frame, text = "Username", font = ("Helvetica", 15), fg = "white", bg = "#0a384c")
        username.place(x = 48, y = 180)

        self.txtuser = ttk.Entry(self.frame, font = ("Helvetica", 20))
        self.txtuser.place(x = 50, y = 210, width = 200)

        password = Label(self.frame, text = "Password", font = ("Helvetica", 15), fg = "white", bg = "#0a384c")
        password.place(x = 48, y = 270)

        self.txtpass = ttk.Entry(self.frame, font = ("Helvetica", 20))
        self.txtpass.place(x = 50, y = 300, width = 200)


        # ===== Buttons
        loginbutton = Button(self.frame, text = "Login", command = self.login, font = ("Helvetica", 10), bd = 2, relief = RIDGE, bg = "#0a384c", fg = 'white',activebackground = '#0a384c')
        loginbutton.place(x = 100, y = 350, width = 120, height = 35)

        registerbutton = Button(self.frame, text = "Register", command = self.reg_window, font = ("Helvetica", 10), borderwidth= 0, bg = "#0a384c", activebackground = '#0a384c')
        registerbutton.place(x = -15, y = 390, width = 120)
      
        forgotbutton = Button(self.frame, text = "Forgot Password", command = self.forgot_password, font = ("Helvetica", 10), borderwidth= 0, bg = "#0a384c", activebackground = '#0a384c')
        forgotbutton.place(x = 10, y = 420, width = 120)

    def reg_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)
    

    def login(self):
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
                # self.new_window = Toplevel(self.root)
                self.app = Face_Recognition_System(self.new_window)
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

                fplbl = Label(self.root2, text = "Forgot Password", font = ("Helvetica", 10))
                fplbl.place(x = 0, y = 10, relwidth = 1)
                # Security Question
                security_Q = Label(self.root2, text = "Security Question", font = ("Sans Serif", 12))
                security_Q.place(x = 50, y = 80)
                self.combo_security_Q = ttk.Combobox(self.root2, text = "Security Question", textvariable = self.var_secQ, font = ("Sans Serif", 12), state = "readonly")
                self.combo_security_Q["values"] = ("Select","Name of your first pet", "City you were born", "Your first school")
                self.combo_security_Q.place(x = 50, y = 110, width = 250)
                self.combo_security_Q.current(0)

                security_A = Label(self.root2, text = "Security Answer", font = ("Sans Serif", 12))
                security_A.place(x = 50, y = 150)
                self.txt_security = ttk.Entry(self.root2, textvariable = self.var_secA, font = ("Sans Serif", 12))
                self.txt_security.place(x = 50, y = 180, width = 250)

                new_password = Label(self.root2, text = "New Password:", font = ("Sans Serif", 12))
                new_password.place(x = 50, y = 220)
                self.txt_newpass= ttk.Entry(self.root2, width = 15, font = ("Sans Serif", 12))
                self.txt_newpass.place(x = 50, y = 250, width = 250)

                btn = Button(self.root2, text = "Reset", font = ("Sans Serif", 12), command = self.reset_pass, bd = 2, relief = RIDGE, bg = "#0a384c", fg = 'white',activebackground = '#0a384c')
                btn.place(x = 50, y = 300, width = 250)
# ===== Forgot Password =====


# ===== Register =====
class Register: 
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1530x790+0+0")
    # Variables
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
        f_lbl = Label(self.root, image = self.photoimg)
        f_lbl.place(x= -1, y=0)
    # Adding a background image to the application software
        img1 = Image.open(r"App-Images\Background.webp")
        img1 = img1.resize((1530, 710), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        bg_img = Label(self.root, image = self.photoimg1)
        bg_img.place(x = 0, y = 130, width = 1530, height = 710)
   # Adding a text in the application
        title_lbl = Label(bg_img,text = "New User? Register", font = ("open sans", 30), 
        bg = "white", fg = "Black")
        title_lbl.place(x = -100, y = 0, width = 1530, height = 45)

       # ===== Work Frames =====
        #Adding a frame
        main_frame = Frame(bg_img, bd = 2, bg = "white")
        main_frame.place(x = 25, y = 50, width = 1230, height = 480)
        # left label frame
        Left_frame = LabelFrame(main_frame, bd = 2, bg = "white", relief = RAISED, text = "Register Here", font = ("Sans Serif", 12))
        Left_frame.place(x = 10, y = 10, width = 580, height = 450)

        inside_left_frame = Frame(Left_frame, bd = 2, relief = RIDGE, bg = "white")
        inside_left_frame.place(x = 5, y = 0, width = 560, height = 420)
        
        # ===== Lables and Entry Fields
        # First Name
       #  ROW 1
        fname = Label(inside_left_frame, text = "First Name", font = ("Sans Serif", 12), bg = "white")
        fname.place(x = 5, y = 0)
        fname_entry = ttk.Entry(inside_left_frame, textvariable = self.var_fname, font = ("Sans Serif", 12))
        fname_entry.place(x = 5, y = 30, width = 250)

        lname = Label(inside_left_frame, text = "Last Name", font = ("Sans Serif", 12), bg = "white")
        lname.place(x = 280, y = 0)
        lname_entry = ttk.Entry(inside_left_frame, textvariable = self.var_lname, font = ("Sans Serif", 12))
        lname_entry.place(x = 280, y = 30, width = 250)

        #  ROW 2
        contact = Label(inside_left_frame, text = "Contact", font = ("Sans Serif", 12), bg = "white")
        contact.place(x = 5, y = 60)
        self.txt_contact = ttk.Entry(inside_left_frame, textvariable = self.var_contact, font = ("Sans Serif", 12))
        self.txt_contact.place(x = 5, y = 90, width = 250)

        email = Label(inside_left_frame, text = "Email", font = ("Sans Serif", 12), bg = "white")
        email.place(x = 280, y = 60)
        self.txt_email = ttk.Entry(inside_left_frame, textvariable = self.var_email, font = ("Sans Serif", 12))
        self.txt_email.place(x = 280, y = 90, width = 250)

        #  ROW 3
        security_Q = Label(inside_left_frame, text = "Security Question", font = ("Sans Serif", 12), bg = "white")
        security_Q.place(x = 5, y = 120)
        self.combo_security_Q = ttk.Combobox(inside_left_frame, text = "Security Question", textvariable = self.var_secQ, font = ("Sans Serif", 12), state = "readonly")
        self.combo_security_Q["values"] = ("Select","Name of your first pet", "City you were born", "Your first school")
        self.combo_security_Q.place(x = 5, y = 150, width = 250)
        self.combo_security_Q.current(0)

        security_A = Label(inside_left_frame, text = "Security Answer", font = ("Sans Serif", 12), bg = "white")
        security_A.place(x = 280, y = 120)
        self.txt_security = ttk.Entry(inside_left_frame, textvariable = self.var_secA, font = ("Sans Serif", 12))
        self.txt_security.place(x = 280, y = 150, width = 250)

        # ROW 4
        pswd = Label(inside_left_frame, text = "Password", font = ("Sans Serif", 12), bg = "white")
        pswd.place(x = 5, y = 180)
        self.txt_pswd = ttk.Entry(inside_left_frame, textvariable = self.var_pass, font = ("Sans Serif", 12))
        self.txt_pswd.place(x = 5, y = 210, width = 250)

        confirm_pswd = Label(inside_left_frame, text = "Confirm Password", font = ("Sans Serif", 12), bg = "white")
        confirm_pswd.place(x = 280, y = 180)
        self.txt_confirm_pswd = ttk.Entry(inside_left_frame, textvariable = self.var_conpass, font = ("Sans Serif", 12))
        self.txt_confirm_pswd.place(x = 280, y = 210, width = 250)
        
     # ===== Functional Buttons 1.0 =====
        # Buttons Frame
        btn_frame = Frame(inside_left_frame, bd = 2, relief = RAISED, bg = "white")
        btn_frame.place(x = 1, y = 372, width = 555, height = 37)

        # Register
        registerbtn = Button(btn_frame, text = "Register user", command = self.register_user, width = 28, font = ("Sans Serif", 12), bg = "#117c9d", fg = "black")
        registerbtn.grid(row = 0, column = 0, padx= 5)

        # Login
        loginbtn = Button(btn_frame, text = "Back to Login", command = self.exit, width = 29, font = ("Sans Serif", 12), bg = "#117c9d", fg = "black")
        loginbtn.grid(row = 0, column = 1, padx= 5)
    # ===== Functional Buttons 1.0 =====

    # Function decleration 
    def register_user(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_secQ.get() == "Select":
            messagebox.showerror("Error", "All fields required", parent = self.root)
        elif self.var_pass.get() != self.var_conpass.get():
            messagebox.showerror("Error", "Password did not match", parent = self.root)
        else:
            conn = mysql.connector.connect(host = "localhost", username = "root", password = "PunnSxG@2806", database = "face_recognition")
            my_cursor = conn.cursor()
            query = ("select * from users where email = %s")
            value = (self.var_email.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row != None:
                messagebox.showerror("Error", "User already exists. Try another email", parent = self.root)
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
            messagebox.showinfo("Success", "Registered Succesfully", parent = self.root)

    def exit(self):
        self.exit = tkinter.messagebox.askyesno("Back to Login", "Are you sure you want to go back to login?", parent = self.root)
        if self.exit > 0:
            self.root.destroy()
        else:
            return
# ===== Register =====
    def close(self):
        self.root2.destroy()
        return

if __name__ == "__main__":
    main()