from textwrap import fill
from tkinter import*
from tkinter import ttk
from turtle import left, title, width
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2,os
from time import strftime
from datetime import datetime

class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1270x638+0+0")
        self.root.title("Face recognition System")
        
        #title
        title_lbl=Label(self.root,text="FACE RECOGNITION",font=("times new roman",28,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=1,width=1270,height=47)
        
        #image right
        img_right=Image.open(r"college_images\facedetector.png")
        img_right=img_right.resize((1270,595),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)
        
        f_lb2=Label(self.root,image=self.photoimg_right)
        f_lb2.place(x=0,y=50,width=1270,height=595)
        
         #button
        b1=Button(f_lb2,text="Face Recognition",cursor="hand2",command=self.face_recog,font=("times new roman",14,"bold"),bg="Lime",fg="Black")
        b1.place(x=299,y=228,width=190,height=120)
        
        # ===============Attendance ================
    def mark_attendance(self,i,n,r,d):
        with open("Dilkhush.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (n not in name_list) and (r not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{n},{r},{d},{dtString},{d1},Present")
                
            
        
        # ==========Face Recognition Function =========
    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gary_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gary_image,scaleFactor,minNeighbors)
            coord=[]
            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gary_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))
                conn=mysql.connector.connect(host="localhost",username="root",password="Anita@852216",database="face_recognizer")
                my_cursor=conn.cursor()
                
                my_cursor.execute("select Name from student where Student_id="+str(id))
                n = my_cursor.fetchone()
                n= "+".join(n)
                my_cursor.execute("select Roll from student where Student_id="+str(id))
                r = my_cursor.fetchone()
                r= "+".join(r)
                my_cursor.execute("select Dep from student where Student_id="+str(id))
                d = my_cursor.fetchone()
                d= "+".join(d)
                my_cursor.execute("select Student_id from student where Student_id="+str(id))
                i = my_cursor.fetchone()
                i= "+".join(i)
                
                if confidence>77:
                    cv2.putText(img,f"ID:{i}",(x,y-80),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),1)
                    cv2.putText(img,f"Name:{n}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),1)
                    cv2.putText(img,f"Roll:{r}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),1)
                    cv2.putText(img,f"Department:{d}",(x,y-8),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),1)
                    self.mark_attendance(i,n,r,d)
                    
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img ,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    
                coord=[x,y,w,h]
                
            return coord
        
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        
        video_cap = cv2.VideoCapture(0)
        
        while TRUE:
            ret,img=video_cap.read()
            img = recognize(img,clf,faceCascade)
            cv2.imshow("Wellcome to face recognition",img)
           
            if cv2.waitKey(1)==13:
             break
           
        video_cap.release()
        cv2.destroyAllWindows()
                    
                        
        
if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()  