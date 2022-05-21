from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2,os
import numpy as np


class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1270x638+0+0")
        self.root.title("Face recognition System")
        
        
        title_lbl=Label(self.root,text="TRAIN DATA SET",font=("times new roman",28,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=1,width=1270,height=47)
        
        img_top=Image.open(r"college_images\TrainData.jpg")
        img_top=img_top.resize((1255,585),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=50,width=1270,height=585)
        
        #button
        b1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",14,"bold"),bg="red",fg="white")
        b1.place(x=507,y=411,width=230,height=101)
        
        #back button function
        # Back_Button=Button(f_lbl,text="Back",command=self.root.destroy,font=("arial",11,"bold"),width=17,bg="white",fg="red")
        # Back_Button.pack(side=RIGHT)
        
    #function
    
    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir) ]
        
        faces = []
        ids=[]
        
        for image in path:
            img=Image.open(image).convert('L') #gray scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])
            
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Trainig",imageNp)
            cv2.waitKey(1)==13
            
        ids=np.array(ids)
        # ===============Train The classifier =============
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Traning dataset completed!")
      




        
if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()       