from tkinter import * 
from tkinter import ttk
from PIL import Image,ImageTk
# from student import Student


# Making a class that initiates the backend application of the project
class Face_Recognition_System:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        # Adding a header image to the application software
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
        title_lbl = Label(bg_img,text = "Hello there! Welcome", font = ("open sans", 30), bg = "white", fg = "Black")
        title_lbl.place(x = -100, y = 0, width = 1530, height = 40)

        # Menu Section
        # Student button
        img2 = Image.open(r"C:\Users\sohan\Desktop\College\FYP\Facial_Recognition_System\App-Images\Student.png")
        img2 = img2.resize((220, 220), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        b1 = Button(bg_img, image = self.photoimg2)
        b1.place(x = 80, y = 50, width = 220, height = 180)
        # Text: Student Details
        b1_1 = Button(bg_img, text = "Student Details", cursor = "hand2", font = ("open sans", 15), bg = "aqua", fg = "Black")
        b1_1.place(x = 80, y = 230, width = 220, height = 40)

        # Face detection button
        img3 = Image.open(r"C:\Users\sohan\Desktop\College\FYP\Facial_Recognition_System\App-Images\Face-recognition.jpg")
        img3 = img3.resize((220, 220), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        b2 = Button(bg_img, image = self.photoimg3)
        b2.place(x = 350, y = 50, width = 220, height = 180)
        # Text: Face Recognition
        b2_2 = Button(bg_img, text = "Face Recognition", cursor = "hand2", font = ("open sans", 15), bg = "aqua", fg = "Black")
        b2_2.place(x = 350, y = 230, width = 220, height = 40)

        # Attendance button
        img4 = Image.open(r"C:\Users\sohan\Desktop\College\FYP\Facial_Recognition_System\App-Images\Attendance.jpg")
        img4 = img4.resize((220, 220), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        b3 = Button(bg_img, image = self.photoimg4)
        b3.place(x = 620, y = 50, width = 220, height = 180)
        # Text: Attendance
        b3_3 = Button(bg_img, text = "Attendance", cursor = "hand2", font = ("open sans", 15), bg = "aqua", fg = "Black")
        b3_3.place(x = 620, y = 230, width = 220, height = 40)

        # Help button
        img5 = Image.open(r"C:\Users\sohan\Desktop\College\FYP\Facial_Recognition_System\App-Images\Help.png")
        img5 = img5.resize((220, 220), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        b4 = Button(bg_img, image = self.photoimg5)
        b4.place(x = 890, y = 50, width = 220, height = 180)
        # Text: Help
        b4_4 = Button(bg_img, text = "Help", cursor = "hand2", font = ("open sans", 15), bg = "aqua", fg = "Black")
        b4_4.place(x = 890, y = 230, width = 220, height = 40)

        # Train data button
        img6 = Image.open(r"C:\Users\sohan\Desktop\College\FYP\Facial_Recognition_System\App-Images\Train-data.jpg")
        img6 = img6.resize((220, 220), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        b5 = Button(bg_img, image = self.photoimg6)
        b5.place(x = 80, y = 300, width = 220, height = 180)
        # Text: Train Data
        b5_5 = Button(bg_img, text = "Train Data", cursor = "hand2", font = ("open sans", 15), bg = "aqua", fg = "Black")
        b5_5.place(x = 80, y = 480, width = 220, height = 40)

        # Photos button
        img7 = Image.open(r"C:\Users\sohan\Desktop\College\FYP\Facial_Recognition_System\App-Images\Photos.jpg")
        img7 = img7.resize((220, 220), Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)
        b6 = Button(bg_img, image = self.photoimg7)
        b6.place(x = 350, y = 300, width = 220, height = 180)
        # Text: Photos
        b6_6 = Button(bg_img, text = "Photos", cursor = "hand2", font = ("open sans", 15), bg = "aqua", fg = "Black")
        b6_6.place(x = 350, y = 480, width = 220, height = 40)

        # Developer button
        img8 = Image.open(r"C:\Users\sohan\Desktop\College\FYP\Facial_Recognition_System\App-Images\Developer.png")
        img8 = img8.resize((220, 220), Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)
        b7 = Button(bg_img, image = self.photoimg8)
        b7.place(x = 620, y = 300, width = 220, height = 180)
        # Text: Developer
        b7_7 = Button(bg_img, text = "Developer", cursor = "hand2", font = ("open sans", 15), bg = "aqua", fg = "Black")
        b7_7.place(x = 620, y = 480, width = 220, height = 40)

        # Exit button
        img9 = Image.open(r"C:\Users\sohan\Desktop\College\FYP\Facial_Recognition_System\App-Images\Exit.jpg")
        img9 = img9.resize((220, 220), Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)
        b8 = Button(bg_img, image = self.photoimg9)
        b8.place(x = 890, y = 300, width = 220, height = 180)
        # Text: Exit
        b8_8 = Button(bg_img, text = "Exit", cursor = "hand2", font = ("open sans", 15), bg = "aqua", fg = "Black")
        b8_8.place(x = 890, y = 480, width = 220, height = 40)

        # # # ## Function buttons ##
        # def student_details(self):
        #     self.new_window = Toplevel(self.root)
        #     self.app = Student(self.new_window)



if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()


