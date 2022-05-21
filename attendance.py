from textwrap import fill
from tkinter import*
from tkinter import ttk
from turtle import left, title, width
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2,os,csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1270x638+0+0")
        self.root.title("Face recognition System")
        
        #===========Variable ==============
        self.var_atten_id = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendance= StringVar()
        
          #first image
        img=Image.open(r"F:college_images\header.jpg")
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
        
        title_lbl=Label(bg_img,text="Attendance Management System",font=("times new roman",28,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=-5,width=1270,height=47)
        
         # main mean whole frame include left and right
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=35,y=48,width=1200,height=485)
        
          #left label frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Students Attendance Details",font=("times new roman",10,"bold"))
        left_frame.place(x=8,y=2,width=600,height=477)
        
         
         #Left Image frame
        img_left=Image.open(r"F:\Face Recoginition System\college_images\AdobeStock_303989091.jpeg")
        img_left=img_left.resize((580,190),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        
        f_lbl=Label(left_frame,image=self.photoimg_left)
        f_lbl.place(x=8,y=0,width=580,height=190)
        
        left_inside_frame=Frame(left_frame,bd=2,relief= RIDGE, bg="white")
        left_inside_frame.place(x=13,y=200,width=570,height=250)
        
        #label and entry
          
        #Student ID
        attendance_id_label=Label(left_inside_frame,text="Student id:",font=("times new roman",10,"bold"),bg="white")
        attendance_id_label.grid(row=0,column=0,padx=6,sticky=W)
        
        attendanceID_entry=ttk.Entry(left_inside_frame, width=20,textvariable=self.var_atten_id,font=("times new roman",10,"bold"))
        attendanceID_entry.grid(row=0,column=1,pady=10,sticky=W)
        
        #Roll
        rollLabel=Label(left_inside_frame,text="Roll:",font=("times new roman",10,"bold"),bg="white")
        rollLabel.grid(row=0,column=2,padx=6,sticky=W)
        
        atten_roll=ttk.Entry(left_inside_frame, width=20,textvariable=self.var_atten_roll,font=("times new roman",10,"bold"))
        atten_roll.grid(row=0,column=3,pady=10,sticky=W)
        
        #Name
        nameLabel=Label(left_inside_frame,text="Name:",font=("times new roman",10,"bold"),bg="white")
        nameLabel.grid(row=1,column=0,padx=6,sticky=W)
        
        atten_name=ttk.Entry(left_inside_frame, width=20,textvariable=self.var_atten_name,font=("times new roman",10,"bold"))
        atten_name.grid(row=1,column=1,pady=10,sticky=W)
        
        #Department
        depLabel=Label(left_inside_frame,text="Department:",font=("times new roman",10,"bold"),bg="white")
        depLabel.grid(row=1,column=2,padx=6,sticky=W)
        
        atten_dep=ttk.Entry(left_inside_frame, width=20,textvariable=self.var_atten_dep,font=("times new roman",10,"bold"))
        atten_dep.grid(row=1,column=3,pady=10,sticky=W)
        
        #Time
        timeLabel=Label(left_inside_frame,text="Time:",font=("times new roman",10,"bold"),bg="white")
        timeLabel.grid(row=2,column=0,padx=6,sticky=W)
        
        atten_time=ttk.Entry(left_inside_frame, width=20,textvariable=self.var_atten_time,font=("times new roman",10,"bold"))
        atten_time.grid(row=2,column=1,pady=10,sticky=W)
        
         #Date
        dateLabel=Label(left_inside_frame,text="Date:",font=("times new roman",10,"bold"),bg="white")
        dateLabel.grid(row=2,column=2,padx=6,sticky=W)
        
        atten_date=ttk.Entry(left_inside_frame, width=20,textvariable=self.var_atten_date,font=("times new roman",10,"bold"))
        atten_date.grid(row=2,column=3,pady=10,sticky=W)
        
         #Attendance
        attendanceLabel=Label(left_inside_frame,text="Attendance:",font=("times new roman",10,"bold"),bg="white")
        attendanceLabel.grid(row=3,column=0,padx=6,sticky=W)
        
        self.atten_status=ttk.Combobox(left_inside_frame,font=("times new roman",10,"bold"),state="readonly",width=16,textvariable=self.var_atten_attendance)
        self.atten_status['values']=("Status","Present","Absent")
        self.atten_status.current(0)
        self.atten_status.grid(row=3,column=1,padx=2,pady=6,sticky=W)
        
         #button Frame
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=3,y=190,width=562,height=55)
        
        save_btn=Button(btn_frame,text="Import csv",command=self.importCsv,width=38,font=("times new roman",10,"bold"),bg="Green",fg="white")
        save_btn.grid(row=0,column=0)
        
        update_btn=Button(btn_frame,text="Export csv",command=self.exportCsv,width=39,font=("times new roman",10,"bold"),bg="yellow",fg="black")
        update_btn.grid(row=0,column=1)
        
        delete_btn=Button(btn_frame,text="Update",width=38,font=("times new roman",10,"bold"),bg="cyan",fg="black")
        delete_btn.grid(row=1,column=0)
        
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=39,font=("times new roman",10,"bold"),bg="red",fg="white")
        reset_btn.grid(row=1,column=1)
        
        
        
        
        #Right label frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",10,"bold"))
        right_frame.place(x=618,y=2,width=570,height=477)
        
        # =========Search System ===========
        search_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",10,"bold"))
        search_frame.place(x=8,y=10,width=550,height=53)
        
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
        table_frame.place(x=8,y=80,width=550,height=370)
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL) 
        
        self.Attendance_ReportTable=ttk.Treeview(table_frame,column=("id","name","roll","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.Attendance_ReportTable.xview)
        scroll_y.config(command=self.Attendance_ReportTable.yview)
        
        self.Attendance_ReportTable.heading("id",text="Student id")
        self.Attendance_ReportTable.heading("name",text="Name")
        self.Attendance_ReportTable.heading("roll",text="Roll")
        self.Attendance_ReportTable.heading("department",text="Department")
        self.Attendance_ReportTable.heading("time",text="Time")
        self.Attendance_ReportTable.heading("date",text="Date")
        self.Attendance_ReportTable.heading("attendance",text="Attendance")
        
        self.Attendance_ReportTable["show"]="headings"
        
        self.Attendance_ReportTable.column("id",width=100)
        self.Attendance_ReportTable.column("name",width=100)
        self.Attendance_ReportTable.column("roll",width=100)
        self.Attendance_ReportTable.column("department",width=100)
        self.Attendance_ReportTable.column("time",width=100)
        self.Attendance_ReportTable.column("date",width=100)
        self.Attendance_ReportTable.column("attendance",width=100)
        
        self.Attendance_ReportTable.pack(fill=BOTH,expand=1)
        
        self.Attendance_ReportTable.bind("<ButtonRelease>",self.get_cursor)
        
    #===========Fatch Data Function import=============
    def fetchData(self,rows):
      self.Attendance_ReportTable.delete(*self.Attendance_ReportTable.get_children())
      for i in rows:
        self.Attendance_ReportTable.insert("",END,values=i)
        
        #import
    def importCsv(self):
      global mydata
      mydata.clear()
      fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
      with open(fln) as myfile:
        csvread=csv.reader(myfile,delimiter=",")
        for i in csvread:
          mydata.append(i)
        self.fetchData(mydata)
        
    #===========Fatch Data Function export=============
    def exportCsv(self):
      try:
        if len(mydata)<1:
          messagebox.showerror("No Data","No data found to export",parent=self.root)
          return False
        
        fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln,mode="w",newline="") as myfile:
          exp_write=csv.writer(myfile,delimiter=",")
          for i in mydata:
            exp_write.writerow(i)
          messagebox.showinfo("Data Export","Your data exported to "+os.path.basename(fln)+" Successfully")
          
      except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root) 
                
    #================Cursor function to show data in entry fill ===============
    def get_cursor(self,event=""):
      cursor_row=self.Attendance_ReportTable.focus()
      content=self.Attendance_ReportTable.item(cursor_row)
      rows=content['values']
      self.var_atten_id.set(rows[0])
      self.var_atten_name.set(rows[1])
      self.var_atten_roll.set(rows[2])
      self.var_atten_dep.set(rows[3])
      self.var_atten_time.set(rows[4])
      self.var_atten_date.set(rows[5])
      self.var_atten_attendance.set(rows[6])
      
      
  #==========Reset Data ==============
    def reset_data(self):
      self.var_atten_id.set("")
      self.var_atten_name.set("")
      self.var_atten_roll.set("")
      self.var_atten_dep.set("")
      self.var_atten_time.set("")
      self.var_atten_date.set("")
      self.var_atten_attendance.set("")
      
    
      
if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()                