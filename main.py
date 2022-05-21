from time import strftime
from tkinter import*
from tkinter import ttk
import tkinter
import tkinter
from turtle import title, width
from PIL import Image,ImageTk
import os
from time import strftime
from datetime import datetime
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1270x638+0+0")
        self.root.title("Face recognition System")
        #header data  
        img1 = Image.open("F:\\Face Recoginition System\\college_images\\back1.jfif")
        img1 = img1.resize((1270,638), Image.ANTIALIAS)
        self.photoImg1 = ImageTk.PhotoImage(img1)
        
        bg_img=Label(self.root,image=self.photoImg1)
        bg_img.place(x=0,y=0,width=1270,height=638)

        title=Label(bg_img,text="Face Recognition Attendance System Software",font=("times new roman",30,"bold"),bg="white",fg="red")
        title.place(x=0,y=95,width=1270,height=50)
        
         #first image
        img=Image.open(r"college_images\header.jpg")
        img=img.resize((1270,100),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1270,height=100)
        
        #Time
        def Time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,Time)
            
            lbl = Label(f_lbl,font = ('times new roman',14,'bold'),background='black',foreground='blue')
            lbl.place(x=0,y=0,width=100,height=45)
            Time()
        
        # student button
        b1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",14,"bold"),bg="darkblue",fg="white")
        b1.place(x=80,y=280,width=160,height=100)
        
        # Face Detect button
        b1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",14,"bold"),bg="Teal",fg="white")
        b1.place(x=260,y=280,width=160,height=100)
        
        # Attendance button
        b1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",14,"bold"),bg="LimeGreen",fg="white")
        b1.place(x=440,y=280,width=160,height=100)
        
        # Train Face button
        b1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",14,"bold"),bg="DarkMagenta",fg="white")
        b1.place(x=80,y=405,width=160,height=100)
        
         # Photo Face button
        b1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",14,"bold"),bg="DeepPink",fg="white")
        b1.place(x=260,y=405,width=160,height=100)
        
         # Exit Face button
        b1=Button(bg_img,text="Exit",cursor="hand2",command=self.iExit,font=("times new roman",14,"bold"),bg="red",fg="white")
        b1.place(x=440,y=405,width=160,height=100)
        
    #photo view funcction
    def open_img(slef):
        os.startfile("data")
        
        #Function button for student deatils
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
        
      #Function button for train data
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
            
     #Function button for face recognition
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
        
     #Function button for Attendance
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
  
     #Exit function
    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are You sure to exit the window",parent=self.root)
        if self.iExit >0:
            self.root.destroy()
        else:
            return
        
if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()        