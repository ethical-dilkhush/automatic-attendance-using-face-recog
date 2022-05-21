from textwrap import fill
from tkinter import*
from tkinter import ttk
from turtle import left, title, width
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1270x638+0+0")
        self.root.title("Face recognition System")
        
         # =======variable=======
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        
        
        
         #first image
        img=Image.open(r"F:\Face Recoginition System\college_images\header.jpg")
        img=img.resize((1270,100),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1270,height=100)
        
        
        
        #background image
        img3=Image.open(r"F:\Face Recoginition System\college_images\back1.jfif")
        img3=img3.resize((1270,638),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=100,width=1270,height=638)
        
        title_lbl=Label(bg_img,text="Student Management System",font=("times new roman",28,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=-5,width=1270,height=47)
        
        #=========Back Button============
        # Back_Button=Button(title,text="Back",command=self.root.destroy,font=("arial",11,"bold"),width=15,bg="white",fg="red")
        # Back_Button.pack(side=RIGHT)
        
        
        # main mean whole frame include left and right
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=35,y=48,width=1200,height=485)
        
        #left label frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Students Details",font=("times new roman",10,"bold"))
        left_frame.place(x=8,y=2,width=600,height=477)
        
        # #Left Image frame
        # img_left=Image.open(r"F:\Face Recoginition System\college_images\AdobeStock_303989091.jpeg")
        # img_left=img_left.resize((580,80),Image.ANTIALIAS)
        # self.photoimg_left=ImageTk.PhotoImage(img_left)
        
        # f_lbl=Label(left_frame,image=self.photoimg_left)
        # f_lbl.place(x=8,y=0,width=580,height=80)
        
        #current course information
        current_course_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course",font=("times new roman",10,"bold"))
        current_course_frame.place(x=8,y=20,width=580,height=85)
        
        
        #department comobo
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",10,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=6)
        
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",10,"bold"),state="readonly",width=16)
        dep_combo['values']=("Select Department","Computer","IT","Civil","Machanical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=5)
        
        #course Combo
        course_label=Label(current_course_frame,text="Course",font=("times new roman",10,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=6,sticky=W)
        
        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",10,"bold"),state="readonly",width=16)
        course_combo['values']=("Select Course","FCS","FEDA","BPES","HM")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=6,sticky=W)
        
        #Year Combo
        year_label=Label(current_course_frame,text="Year",font=("times new roman",10,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=6,sticky=W)
        
        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",10,"bold"),state="readonly",width=16)
        year_combo['values']=("Select Year","2019-2022","2018-2022","2020-2023","2021-2025")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=6,sticky=W)
        
        #Semester Combo
        semester_label=Label(current_course_frame,text="Semester",font=("times new roman",10,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=6,sticky=W)
        
        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",10,"bold"),state="readonly",width=16)
        semester_combo['values']=("Select Semester","Semester-1","Semester-2","Semester-3","Semester-4","Semester-5","Semester-6","Semester-7","Semester-8")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=6,sticky=W)
        
        #class student information
        class_student_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Students Information",font=("times new roman",10,"bold"))
        class_student_frame.place(x=8,y=130,width=580,height=323)
        
        #Student ID
        student_id_label=Label(class_student_frame,text="Student Id",font=("times new roman",10,"bold"),bg="white")
        student_id_label.grid(row=0,column=0,padx=6,sticky=W)
        
        studentID_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20,font=("times new roman",10,"bold"))
        studentID_entry.grid(row=0,column=1,pady=6,sticky=W)
        
        #Student name
        studentName_label=Label(class_student_frame,text="Student Name",font=("times new roman",10,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=6,sticky=W)
        
        studentName_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",10,"bold"))
        studentName_entry.grid(row=0,column=3,pady=6,sticky=W)
        
        #Class Division
        class_div_label=Label(class_student_frame,text="Class Division",font=("times new roman",10,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=6,sticky=W)
        
        div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("times new roman",10,"bold"),state="readonly",width=16)
        div_combo['values']=("Select","A","B","C","D")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=2,pady=6,sticky=W)
        
        #Roll Number
        roll_no_label=Label(class_student_frame,text="Roll No.",font=("times new roman",10,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=6,sticky=W)
        
        roll_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("times new roman",10,"bold"))
        roll_no_entry.grid(row=1,column=3,pady=6,sticky=W)
        
        #Gender
        gender_label=Label(class_student_frame,text="Gender",font=("times new roman",10,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=6,sticky=W)
        
        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",10,"bold"),state="readonly",width=16)
        gender_combo['values']=("Select","Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=2,pady=6,sticky=W)
        
        #Student DOB
        dob_label=Label(class_student_frame,text="DOB",font=("times new roman",10,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=6,sticky=W)
        
        dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman",10,"bold"))
        dob_entry.grid(row=2,column=3,pady=6,sticky=W)
        
        #Student Email
        email_label=Label(class_student_frame,text="Email",font=("times new roman",10,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=6,sticky=W)
        
        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",10,"bold"))
        email_entry.grid(row=3,column=1,pady=6,sticky=W)
        
        #Student Phone number
        phone_label=Label(class_student_frame,text="Phone Number",font=("times new roman",10,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=6,sticky=W)
        
        phone_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",10,"bold"))
        phone_entry.grid(row=3,column=3,pady=6,sticky=W)
        
        #Student Address
        address_label=Label(class_student_frame,text="Address",font=("times new roman",10,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=6,sticky=W)
        
        address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("times new roman",10,"bold"))
        address_entry.grid(row=4,column=1,pady=6,sticky=W)
        
        #Teacher name
        teacher_label=Label(class_student_frame,text="Teacher Name",font=("times new roman",10,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=6,sticky=W)
        
        teacher_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",10,"bold"))
        teacher_entry.grid(row=4,column=3,pady=6,sticky=W)
        
        #Radio Button
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Simple",value="yes")
        radiobtn1.grid(row=5,column=0)
        
        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Simple",value="No")
        radiobtn2.grid(row=5,column=1)
        
        #button Frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=3,y=195,width=570,height=56)
        
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=39,font=("times new roman",10,"bold"),bg="Green",fg="white")
        save_btn.grid(row=0,column=0)
        
        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=39,font=("times new roman",10,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)
        
        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=39,font=("times new roman",10,"bold"),bg="Red",fg="white")
        delete_btn.grid(row=1,column=0)
        
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=39,font=("times new roman",10,"bold"),bg="Black",fg="white")
        reset_btn.grid(row=1,column=1)
        
        #second button Frame like photo update and photo taking
        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=2,y=260,width=573,height=44)
        
        take_photo_btn=Button(btn_frame1,command=self.generate_dataset,text="Take a Photo Simple",width=80,height=2,font=("times new roman",10,"bold"),bg="GreenYellow",fg="black")
        take_photo_btn.grid(row=0,column=0)
        
         #Right label frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Students Details",font=("times new roman",10,"bold"))
        right_frame.place(x=618,y=2,width=570,height=477)
       
        
        # =========Search System ===========
        search_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",10,"bold"))
        search_frame.place(x=8,y=22,width=550,height=53)
        
        search_label=Label(search_frame,text="Search By",font=("times new roman",10,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=6,sticky=W)
        
        search_combo=ttk.Combobox(search_frame,font=("times new roman",10,"bold"),state="readonly",width=13)
        search_combo['values']=("Select","Roll No","Phone No.")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=4,sticky=W)
        
        search_entry=ttk.Entry(search_frame,width=15,font=("times new roman",10,"bold"))
        search_entry.grid(row=0,column=2,pady=4,padx=4,sticky=W)
        
        search_btn=Button(search_frame,text="Search",width=15,font=("times new roman",10,"bold"),bg="purple",fg="white")
        search_btn.grid(row=0,column=3,padx=2)
        
        showAll_btn=Button(search_frame,text="Show All",width=14,font=("times new roman",10,"bold"),bg="darkBlue",fg="white")
        showAll_btn.grid(row=0,column=4,padx=2)
        
        # ==========Table frame where we can show the data ===========
        table_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=8,y=100,width=550,height=350)
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="Student Id")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll No.")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="Photo Sample Status")
        self.student_table["show"]="headings"
        
        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=150)
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
    # ==========function declareation============ 
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_course.get()=="Select course" or self.var_year.get()=="Select year" or self.var_semester.get()=="Select semester" or self.var_std_id.get()=="" or self.var_std_name.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                # messagebox.showinfo("success","Data Submitted")
                conn=mysql.connector.connect(host="localhost",username="root",password="Anita@852216",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                        self.var_dep.get(),
                                                                        self.var_course.get(),
                                                                        self.var_year.get(),
                                                                        self.var_semester.get(),
                                                                        self.var_std_id.get(),
                                                                        self.var_std_name.get(),
                                                                        self.var_div.get(),
                                                                        self.var_roll.get(),
                                                                        self.var_gender.get(),
                                                                        self.var_dob.get(),
                                                                        self.var_email.get(),
                                                                        self.var_phone.get(),
                                                                        self.var_address.get(),
                                                                        self.var_teacher.get(),
                                                                        self.var_radio1.get()
                                                                    
                                                                        ))    
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success","Students details has been added",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)   
                
    # ==============Fetch data into Right frame ================
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Anita@852216",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()
        
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()
        
    #======== get cursor mean all data show in left frame fileds==================
    def get_cursor(self, event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        
        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])
        
    #==========Update function ==================
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_course.get()=="Select course" or self.var_year.get()=="Select year" or self.var_semester.get()=="Select semester" or self.var_std_id.get()=="" or self.var_std_name.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                Upadate=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if Upadate>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Anita@852216",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("UPDATE student SET Dep=%s,course=%s,Year=%s,Semester=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s WHERE Student_id=%s",(
                        
                                                                                                                                                                                        self.var_dep.get(),
                                                                                                                                                                                        self.var_course.get(),
                                                                                                                                                                                        self.var_year.get(),
                                                                                                                                                                                        self.var_semester.get(),
                                                                                                                                                                                        self.var_div.get(),
                                                                                                                                                                                        self.var_roll.get(),
                                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                                        self.var_teacher.get(),
                                                                                                                                                                                        self.var_radio1.get(),
                                                                                                                                                                                        self.var_std_id.get()                                                                
                                                                                                                                                                                    ))
                else:
                    if not Upadate:
                        return
                messagebox.showinfo("Success","Student deatils successfully update completed",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
                        
    #=========Delete function==========
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete the student?",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Anita@852216",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted the student details!")   
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)         
    
    #==========Reset Function ===========
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course"),
        self.var_year.set("Select Year"),
        self.var_semester.set("Select Semester"),
        self.var_std_id.set(""),
        self.var_std_name.set(""),
        self.var_div.set("Select"),
        self.var_roll.set(""),
        self.var_gender.set("Select"),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_teacher.set(""),
        self.var_radio1.set("")        
        
    #===========Genrate data set Take Photo simple============
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_course.get()=="Select course" or self.var_year.get()=="Select year" or self.var_semester.get()=="Select semester" or self.var_std_id.get()=="" or self.var_std_name.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Anita@852216",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("UPDATE student SET Dep=%s,course=%s,Year=%s,Semester=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s WHERE Student_id=%s",(
                        
                                                                        self.var_dep.get(),
                                                                        self.var_course.get(),
                                                                        self.var_year.get(),
                                                                        self.var_semester.get(),
                                                                        self.var_div.get(),
                                                                        self.var_roll.get(),
                                                                        self.var_gender.get(),
                                                                        self.var_dob.get(),
                                                                        self.var_email.get(),
                                                                        self.var_phone.get(),
                                                                        self.var_address.get(),
                                                                        self.var_teacher.get(),
                                                                        self.var_radio1.get(),
                                                                        self.var_std_id.get()==id+1                                                                
                                                                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                # =========Load Predefined data on face frontals from open cv ==========
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor = 1.3
                    #minimum neigher=5
                    
                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                cap = cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face = cv2.resize(face_cropped(my_frame),(450,450))
                        face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)
                    
                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data set completed successfully")
                
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root) 
                    
    
        
if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()                