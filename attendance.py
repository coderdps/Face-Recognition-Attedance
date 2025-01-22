from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog
import datetime
mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        #===================variables===================
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()
        
        #first image
        img=Image.open(r"C:\Users\Dell\Desktop\face_recognition system\college_images\studentpage1.jpg")
        img=img.resize((750,200),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=750,height=200)
        
        #second image
        img1=Image.open(r"C:\Users\Dell\Desktop\face_recognition system\college_images\studentpage3.jpg")
        img1=img1.resize((750,200),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=750,y=0,width=750,height=200)
        
        #bg image
        img3=Image.open(r"C:\Users\Dell\Desktop\face_recognition system\college_images\bgimg.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=200,width=1530,height=710)
        
        title_lbl=Label(bg_img,text="Attendance Management System",font=("times new roman",35,"bold"),bg="grey",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        main_frame=Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=20, y=50, width=1330, height=550)
        
        #Left label frame
        Left_frame=LabelFrame(main_frame, bd=2, relief=RIDGE, text="STUDENT ATTENDANCE DETAILS", font=("times new roman",12,"bold"))
        Left_frame.place(x=10, y=10, width=680, height=530)
        
        img_left=Image.open(r"C:\Users\Dell\Desktop\face_recognition system\college_images\student_page_left_label1.jpg")
        img_left=img_left.resize((670,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        
        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=670,height=130)
        
        left_inside_frame=Frame(Left_frame,relief=RIDGE, bd=2, bg="white")
        left_inside_frame.place(x=0, y=135, width=670, height=310)
        
        # Labels and Entry
        # Attendance ID
        attendanceID_label=Label(left_inside_frame, text="Attendance ID:", font="comicsansns 11 bold")
        attendanceID_label.grid(row=0, column=0, padx=10, sticky=W)
        
        attendanceID_entry=ttk.Entry(left_inside_frame, textvariable=self.var_atten_id,font="comicsansns 11 bold", width=20)
        attendanceID_entry.grid(row=0, column=1, padx=10, sticky=W)

        # Roll
        rollLabel=Label(left_inside_frame, text="Roll:", font="comicsansns 11 bold")
        rollLabel.grid(row=0, column=2, padx=4,pady=8, )
        
        atten_roll=ttk.Entry(left_inside_frame, textvariable=self.var_atten_roll, font="comicsansns 11 bold", width=20)
        atten_roll.grid(row=0, column=3, pady=8)
        
        # Name
        nameLabel=Label(left_inside_frame, text="Name:", font="comicsansns 11 bold")
        nameLabel.grid(row=1, column=0)
        
        atten_name=ttk.Entry(left_inside_frame, textvariable=self.var_atten_name, font="comicsansns 11 bold", width=20)
        atten_name.grid(row=1, column=1, pady=8)
        
        # Depart
        depLabel=Label(left_inside_frame, text="Department:", font="comicsansns 11 bold")
        depLabel.grid(row=1, column=2)
        
        atten_dep=ttk.Entry(left_inside_frame, textvariable=self.var_atten_dep, font="comicsansns 11 bold", width=20)
        atten_dep.grid(row=1, column=3, pady=8)
        
        # Time
        timeLabel=Label(left_inside_frame, text="Time:", font="comicsansns 11 bold")
        timeLabel.grid(row=2, column=0)
        
        atten_time=ttk.Entry(left_inside_frame,  textvariable=self.var_atten_time,font="comicsansns 11 bold", width=20)
        atten_time.grid(row=2, column=1, pady=8)
        
        # Date
        dateLabel=Label(left_inside_frame, text="Date:", font="comicsansns 11 bold")
        dateLabel.grid(row=2, column=2)
        
        atten_date=ttk.Entry(left_inside_frame, textvariable=self.var_atten_date, font="comicsansns 11 bold", width=20)
        atten_date.grid(row=2, column=3, pady=8)
        
        #attendance status
        attendanceLabel=Label(left_inside_frame, text="Attendance Status:", font="comicsansns 11 bold")
        attendanceLabel.grid(row=3, column=0)
        
        self.atten_status=ttk.Combobox(left_inside_frame,  textvariable=self.var_atten_id, width=20, font="comicsansns 11 bold", state="readonly")
        self.atten_status["values"]=("Status","Present", "Absent")
        self.atten_status.grid(row=3, column=1,pady=8)
        self.atten_status.current(0)
       
        #buttons frame
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=0, y=265,width=665, height=30)
        
        save_btn=Button(btn_frame, text="Import CSV", command=self.importCSV, width=18, font=("times new roman",12,"bold"), bg="grey", fg="white")
        save_btn.grid(row=0, column=0)
        
        update_btn=Button(btn_frame, text="Export CSV",command=self.exportCsv, width=18, font=("times new roman",12,"bold"), bg="grey", fg="white")
        update_btn.grid(row=0, column=1)
        
        delete_btn=Button(btn_frame, text="Update",  width=18, font=("times new roman",12,"bold"), bg="grey", fg="white")
        delete_btn.grid(row=0, column=2)
        
        reset_btn=Button(btn_frame, text="Reset", command=self.reset_data, width=18, font=("times new roman",12,"bold"), bg="grey", fg="white")
        reset_btn.grid(row=0, column=3)
        
        #Right label frame
        Right_frame=LabelFrame(main_frame, bd=2, relief=RIDGE, text="ATTENDANCE DETAILS", font=("times new roman",12,"bold"))
        Right_frame.place(x=700, y=10, width=620, height=530)
        
        table_frame=Frame(Right_frame,bd=2,relief=RIDGE)
        table_frame.place(x=5, y=5,width=600, height=415)
        
        #==========Scroll Bar Table==============
        scroll_x=Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(table_frame,orient=VERTICAL)
        
        self.AttendanceReportTable=ttk.Treeview(table_frame,columns=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)
        
        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll No")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")
                        
        self.AttendanceReportTable["show"]="headings"
        
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)
                        
        self.AttendanceReportTable.pack(fill=BOTH, expand=1)
        
        self.AttendanceReportTable.bind("<ButtonRelease>", self.get_cursor)

    #===================fetch data===========
    
    
    def fetchData(self,row):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in row:
            self.AttendanceReportTable.insert("",END,values=i)
        self.AttendanceReportTable.pack(fill=BOTH, expand=1)
            
    #import CSV        
    def importCSV(self):
        global myData
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                if i:
                    mydata.append(i)
        self.fetchData(mydata)
    
    #export CSV 
    def exportCsv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("No Data", "No Data found to export", parent=self.root)
                return False

            current_date = datetime.date.today()
            filename = f"attendance_sheet_{current_date}.csv"

            # Check if the file already exists for the current date
            if os.path.exists(filename):
                with open(filename, mode="a") as myfile:
                    exp_write = csv.writer(myfile, delimiter=",")
                    for i in mydata:
                        exp_write.writerow(i)
            else:
                with open(filename, mode="w") as myfile:
                    exp_write = csv.writer(myfile, delimiter=",")
                    for i in mydata:
                        exp_write.writerow(i)

            messagebox.showinfo("Data Export", "Your Data Exported to " + filename + " successfully")
        except Exception as es:
            messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)
                
    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])
                
    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")
        
                
                
                
                
                
                        
if __name__=="__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()     