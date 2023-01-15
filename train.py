from tkinter import * 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2 
import os
import numpy as np

# Making a class that initiates the backend application of the project
class Train:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

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
        title_lbl = Label(bg_img,text = "Train Data", font = ("open sans", 30), bg = "white", fg = "Black")
        title_lbl.place(x = -100, y = 0, width = 1530, height = 40)

        # Train data button
        img6 = Image.open(r"App-Images\Train-data.jpg")
        img6 = img6.resize((220, 220), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        b5 = Button(bg_img, image = self.photoimg6)
        b5.place(x = 550, y = 50, width = 220, height = 180)
        # Text: Train Data
        b5_5 = Button(bg_img, text = "Train Data", cursor = "hand2", command = self.train_classifier, font = ("open sans", 15), bg = "aqua", fg = "Black")
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





















if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()