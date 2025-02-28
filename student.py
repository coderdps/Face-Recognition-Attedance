from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")



        #===========variables============
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_section=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        
        
        
        #first image
        img=Image.open(r"C:\Users\Dell\Desktop\face_recognition system\college_images\studentpage1.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)
        
        #second image
        img1=Image.open(r"C:\Users\Dell\Desktop\face_recognition system\college_images\studentpage2.jpg")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)
        
        #third image
        img2=Image.open(r"C:\Users\Dell\Desktop\face_recognition system\college_images\studentpage3.jpg")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=500,height=130)
        
        
        #bg image
        img3=Image.open(r"C:\Users\Dell\Desktop\face_recognition system\college_images\bgimg.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)
        
        title_lbl=Label(bg_img,text="Student Management System",font=("times new roman",35,"bold"),bg="grey",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        main_frame=Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=20, y=50, width=1330, height=550)
        
        #Left label frame
        Left_frame=LabelFrame(main_frame, bd=2, relief=RIDGE, text="STUDENT DETAILS", font=("times new roman",12,"bold"))
        Left_frame.place(x=10, y=10, width=680, height=530)
        
        img_left=Image.open(r"C:\Users\Dell\Desktop\face_recognition system\college_images\student_page_left_label1.jpg")
        img_left=img_left.resize((670,80),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        
        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=670,height=80)
        
        
        #current course
        current_course_frame=LabelFrame(Left_frame, bd=2, relief=RIDGE, text="Current Course Information", font=("times new roman",12,"bold"))
        current_course_frame.place(x=5, y=85, width=670, height=115)
         
        # Department
        dep_label=Label(current_course_frame, text="Department", font=("times new roman",12,"bold"))
        dep_label.grid(row=0, column=0, padx=10, sticky=W)

        dep_combo=ttk.Combobox(current_course_frame, textvariable=self.var_dep, font=("times new roman",12,"bold"), state="read only", width=20)
        dep_combo["values"]=("Select Department", "CE", "CS", "CSE", "CS/IT", "ECE", "EI", "EN", "IT","ME")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)
       
       # Course
        course_label=Label(current_course_frame, text="Course", font=("times new roman",12,"bold"))
        course_label.grid(row=0, column=2, padx=10, sticky=W)

        course_combo=ttk.Combobox(current_course_frame, textvariable=self.var_course, font=("times new roman",12,"bold"), state="read only", width=20)
        course_combo["values"]=("Select Course", "BTECH", "MBA", "MCA", "MTECH")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)
       
       # Year
        year_label=Label(current_course_frame, text="Year", font=("times new roman",12,"bold"))
        year_label.grid(row=1, column=0, padx=10, sticky=W)

        year_combo=ttk.Combobox(current_course_frame, textvariable=self.var_year, font=("times new roman",12,"bold"), state="read only", width=20)
        year_combo["values"]=("Select Year", "First", "Second", "Third", "Fourth")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)
        
        #Semester
        Semester_label=Label(current_course_frame, text="Semester", font=("times new roman",12,"bold"))
        Semester_label.grid(row=1, column=2, padx=10, sticky=W)

        semester_combo=ttk.Combobox(current_course_frame, textvariable=self.var_sem, font=("times new roman",12,"bold"), state="read only", width=20)
        semester_combo["values"]=("Select Semester", "1", "2", "3", "4", "5", "6", "7", "8")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)
        
        #Class Student Information 
        class_student_frame=LabelFrame(Left_frame, bd=2, relief=RIDGE, text="Class Student Information", font=("times new roman",12,"bold"))
        class_student_frame.place(x=5, y=205, width=670, height=300)
        
        # Student ID
        studentId_label=Label(class_student_frame, text="Student ID:", font=("times new roman",12,"bold"))
        studentId_label.grid(row=0, column=0, padx=10, sticky=W)
        
        studentId_entry=ttk.Entry(class_student_frame,  textvariable=self.var_std_id,font=("times new roman",12,"bold"), width=20)
        studentId_entry.grid(row=0, column=1, padx=10, sticky=W)
        
        
        # Student Name
        studentName_label=Label(class_student_frame, text="Student Name:", font=("times new roman",12,"bold"))
        studentName_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)
        
        studentName_entry=ttk.Entry(class_student_frame, textvariable=self.var_std_name, font=("times new roman",12,"bold"), width=20)
        studentName_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)
        
        # Class Section
        classSection_label=Label(class_student_frame, text="Class Section:", font=("times new roman",12,"bold"))
        classSection_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)
        
        section_combo=ttk.Combobox(class_student_frame, textvariable=self.var_section, font=("times new roman",12,"bold"), state="read only", width=18)
        section_combo["values"]=("IT-1", "IT-2", "IT-3","CS/IT-1","CSE-1", "CSE-2", "CSE-3","CS-1","ME-1", "ME-2", "ME-3","CE-1","CE-2","EN-1","EN-2","ECE-1", "ECE-2", "ECE-3","EI-1" )
        section_combo.current(0)
        section_combo.grid(row=1, column=1, padx=10, pady=5, sticky=W)
        
        # Roll No
        rollNo_label=Label(class_student_frame, text="Roll No:", font=("times new roman",12,"bold"))
        rollNo_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)
        
        rollNo_entry=ttk.Entry(class_student_frame,  textvariable=self.var_roll, font=("times new roman",12,"bold"), width=20)
        rollNo_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)
        
       # Gender
        gender_label=Label(class_student_frame, text="Gender:", font=("times new roman",12,"bold"))
        gender_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)
        
        gender_combo=ttk.Combobox(class_student_frame, textvariable=self.var_gender, font=("times new roman",12,"bold"), state="read only", width=18)
        gender_combo["values"]=( "Male", "Female", "Others")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=10, pady=5, sticky=W)
        
        # DOB
        DOB_label=Label(class_student_frame, text="DOB:", font=("times new roman",12,"bold"))
        DOB_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)
        
        DOB_entry=ttk.Entry(class_student_frame,  textvariable=self.var_dob, font=("times new roman",12,"bold"), width=20)
        DOB_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)
        
        # email
        email_label=Label(class_student_frame, text="Email:", font=("times new roman",12,"bold"))
        email_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)
        
        email_entry=ttk.Entry(class_student_frame,  textvariable=self.var_email, font=("times new roman",12,"bold"), width=20)
        email_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W) 
        
        # Phone No
        phoneNO_label=Label(class_student_frame, text="Phone No:", font=("times new roman",12,"bold"))
        phoneNO_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)
        
        phoneNO_entry=ttk.Entry(class_student_frame,  textvariable=self.var_phone, font=("times new roman",12,"bold"), width=20)
        phoneNO_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)
        
        # Address
        address_label=Label(class_student_frame, text="Address:", font=("times new roman",12,"bold"))
        address_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)
        
        address_entry=ttk.Entry(class_student_frame, textvariable=self.var_address, font=("times new roman",12,"bold"), width=20)
        address_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W) 
        
        # Teacher Name
        teacherName_label=Label(class_student_frame, text="Teacher Name:", font=("times new roman",12,"bold"))
        teacherName_label.grid(row=4, column=2, padx=10, pady=5, sticky=W)
        
        teacherName_entry=ttk.Entry(class_student_frame, textvariable=self.var_teacher, font=("times new roman",12,"bold"), width=20)
        teacherName_entry.grid(row=4, column=3, padx=10, pady=5, sticky=W)
        
        #radio buttons
        self.var_radio1=StringVar()
        radionbtn1=ttk.Radiobutton(class_student_frame, variable=self.var_radio1, text="Take Photo Sample", value="Yes")
        radionbtn1.grid(row=5, column=0)
        
        radionbtn1=ttk.Radiobutton(class_student_frame, variable=self.var_radio1, text="No Photo Sample", value="No")
        radionbtn1.grid(row=5, column=1)
        
        #buttons frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=0, y=200,width=665, height=30)
        
        save_btn=Button(btn_frame, text="Save",command=self.add_data, width=18, font=("times new roman",12,"bold"), bg="grey", fg="white")
        save_btn.grid(row=0, column=0)
        
        update_btn=Button(btn_frame, text="Update", command=self.update_data, width=18, font=("times new roman",12,"bold"), bg="grey", fg="white")
        update_btn.grid(row=0, column=1)
        
        delete_btn=Button(btn_frame, text="Delete", command=self.delete_data, width=18, font=("times new roman",12,"bold"), bg="grey", fg="white")
        delete_btn.grid(row=0, column=2)
        
        reset_btn=Button(btn_frame, text="Reset", command=self.reset_data, width=18, font=("times new roman",12,"bold"), bg="grey", fg="white")
        reset_btn.grid(row=0, column=3)
        
        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE)
        btn_frame1.place(x=0, y=230,width=665, height=30)
        
        take_photo_btn=Button(btn_frame1, text="Take Photo Sample",command=self.generate_dataset, width=36, font=("times new roman",12,"bold"), bg="grey", fg="white")
        take_photo_btn.grid(row=1, column=0)
        
        update_photo_btn=Button(btn_frame1, text="Update Photo Sample", width=36, font=("times new roman",12,"bold"), bg="grey", fg="white")
        update_photo_btn.grid(row=1, column=2)
        
        
        #Right label frame
        Right_frame=LabelFrame(main_frame, bd=2, relief=RIDGE, text="STUDENT DETAILS", font=("times new roman",12,"bold"))
        Right_frame.place(x=700, y=10, width=620, height=530)
        
        img_right=Image.open(r"C:\Users\Dell\Desktop\face_recognition system\college_images\student_page_right_label1.jpg")
        img_right=img_right.resize((610,80),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)
        
        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=610,height=80)
        
        #=============Search System====================
        Search_frame=LabelFrame(Right_frame, bd=2, relief=RIDGE, text="Search System", font=("times new roman",12,"bold"))
        Search_frame.place(x=5, y=85, width=610, height=70)
        
        search_label=Label(Search_frame, text="Search By:", font=("times new roman",13,"bold"),bg="black", fg="white")
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        
        search_combo=ttk.Combobox(Search_frame, font=("times new roman",12,"bold"), state="read only", width=10)
        search_combo["values"]=("Select ", "Roll_NO", "Name", "Phone_No", "DOB", "Student_ID")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)
        
        search_entry=ttk.Entry(Search_frame, font=("times new roman",12,"bold"), width=18)
        search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)
        
        search_btn=Button(Search_frame, text="Search", width=13, font=("times new roman",10,"bold"), bg="grey", fg="white")
        search_btn.grid(row=0, column=3, padx=4)
        
        showAll_btn=Button(Search_frame, text="Show All", width=13, font=("times new roman",10,"bold"), bg="grey", fg="white")
        showAll_btn.grid(row=0, column=4)
        
        #==================Table Frame==================
        table_frame=Frame(Right_frame, bd=2, relief=RIDGE)
        table_frame.place(x=5, y=160, width=610, height=340)
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame,column=("Dep","Course","Year","Sem","ID","Name","Section","RollNo","Gender","DOB","Email","PhoneNo","Address","Teacher","Photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        self.student_table.heading("Dep",text="Department")
        self.student_table.heading("Course",text="Course")
        self.student_table.heading("Year",text="Year")
        self.student_table.heading("Sem",text="Semester")
        self.student_table.heading("ID",text="Student ID")
        self.student_table.heading("Name",text="Student Name")
        self.student_table.heading("Section",text="Class Section")
        self.student_table.heading("RollNo",text="Roll No")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("DOB",text="DOB")
        self.student_table.heading("Email",text="Email")
        self.student_table.heading("PhoneNo",text="Phone No")
        self.student_table.heading("Address",text="Address")
        self.student_table.heading("Teacher",text="Teacher Name")
        self.student_table.heading("Photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"
        
        self.student_table.column("Dep",width=100)
        self.student_table.column("Course",width=100)
        self.student_table.column("Year",width=100)
        self.student_table.column("Sem",width=100)
        self.student_table.column("ID",width=100)
        self.student_table.column("Section",width=100)
        self.student_table.column("RollNo",width=100)
        self.student_table.column("Gender",width=100)
        self.student_table.column("DOB",width=100)
        self.student_table.column("Email",width=100)
        self.student_table.column("PhoneNo",width=100)
        self.student_table.column("Address",width=100)
        self.student_table.column("Teacher",width=100)
        self.student_table.column("Photo",width=100)
        
        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
        
        
        
        #===========funtion declarations==============
        
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error! ", "All fields are required", parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Mysql@123",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    
                                                                                                  self.var_dep.get(),
                                                                                                  self.var_course.get(),
                                                                                                  self.var_year.get(),
                                                                                                  self.var_sem.get(),
                                                                                                  self.var_std_id.get(),
                                                                                                  self.var_std_name.get(),
                                                                                                  self.var_section.get(),
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
                messagebox.showinfo("Success","Student details has been added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
    
    
    
    #============fetch data===========
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Mysql@123",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()
    
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()    
        conn.close()
        
        
        
    #=========Get Cursor============
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
    
        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_sem.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_section.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])
    
    
    
    #========update function==================
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                Upadate=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if Upadate>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Mysql@123",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update Face_recognizer.student set Dep=%s,Course=%s,Year=%s,Semester=%s, Name=%s,Section=%s, Roll=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(

                                                                                                self.var_dep .get(),
                                                                                                self.var_course.get(),
                                                                                                self.var_year.get(),
                                                                                                self.var_sem.get(),
                                                                                                self.var_std_name.get(),
                                                                                                self.var_section.get(),
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
                messagebox.showinfo("Success","Student details successfully update completed",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()                                                             
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
    
    
    
    
    #==================delete function=========================
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student data",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Mysql@123",database="face_recognizer")
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
                messagebox.showinfo("Delete","Successfully deleted student data",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
                
    #===========================Reset fucntion==================
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_sem.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_section.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")
        
    
    #=============Genrate Dataset or Take Photo Samples================================
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Mysql@123",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select *from student")
                my_result=my_cursor.fetchall()
                id=0
                for x in my_result:
                    id+=1
                my_cursor.execute("update Face_recognizer.student set Dep=%s,Course=%s,Year=%s,Semester=%s, Name=%s,Section=%s, Roll=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(

                                                                                                self.var_dep .get(),
                                                                                                self.var_course.get(),
                                                                                                self.var_year.get(),
                                                                                                self.var_sem.get(),
                                                                                                self.var_std_name.get(),
                                                                                                self.var_section.get(),
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
                
                #=========== load predefined data on face frontals from open cv============
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor=1.3
                    #minimum neighbour=5
                    
                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h, x:x+w]
                        return face_cropped
                
                
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret, my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)
                    
                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed")
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
                
                            
        
        
        
        
        
        
        
        
        
if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()     