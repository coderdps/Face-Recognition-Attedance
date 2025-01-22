import tkinter
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer 
from help import Help
from time import strftime
from datetime import datetime 

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        
        #first image
        img=Image.open(r"C:\Users\Dell\Desktop\face_recognition system\college_images\topimg1.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)
        
        #second image
        img1=Image.open(r"C:\Users\Dell\Desktop\face_recognition system\college_images\topimg2.jpg")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)
        
        #third image
        img2=Image.open(r"C:\Users\Dell\Desktop\face_recognition system\college_images\topimg3.jpg")
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
        
        title_lbl=Label(bg_img,text="Attendance Monitoring with Face Recognition",font=("times new roman",35,"bold"),bg="black",fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        #========Time=========
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(100,time)
        
        lbl=Label(title_lbl,font=("times new roman",14,"bold"),background='black',foreground='white')
        lbl.place(x=0,y=0,width=150,height=50)
        time()
            
        
        
        
        #student button
        img4=Image.open(r"C:\Users\Dell\Desktop\face_recognition system\college_images\student.jpg")
        img4=img4.resize((220,220),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        b1=Button(bg_img,image=self.photoimg4, command=self.student_details,  cursor="hand2")
        b1.place(x=100,y=100,width=220,height=220)
        
        b1_1=Button(bg_img,text="Student Details", command=self.student_details, cursor="hand2",font=("times new roman",20,"bold"),bg="darkgrey",fg="white")
        b1_1.place(x=100,y=300,width=220,height=40)
        
        
        #detect face button button
        img5=Image.open(r"C:\Users\Dell\Desktop\face_recognition system\college_images\face_detector.jpg")
        img5=img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        b1=Button(bg_img,image=self.photoimg5,command=self.face_data, cursor="hand2",)
        b1.place(x=400,y=100,width=220,height=220)
        
        b1_1=Button(bg_img,text="Face Detector", command=self.face_data, cursor="hand2",font=("times new roman",20,"bold"),bg="darkgrey",fg="white")
        b1_1.place(x=400,y=300,width=220,height=40)
        
        
        #attendance button
        img6=Image.open(r"C:\Users\Dell\Desktop\face_recognition system\college_images\attendance.jpg")
        img6=img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        
        b1=Button(bg_img,image=self.photoimg6, command=self.attendance_data,cursor="hand2")
        b1.place(x=700,y=100,width=220,height=220)
        
        b1_1=Button(bg_img,text="Attendance",cursor="hand2", command=self.attendance_data,font=("times new roman",20,"bold"),bg="darkgrey",fg="white")
        b1_1.place(x=700,y=300,width=220,height=40)
        
        
        #helpdesk button
        img7=Image.open(r"C:\Users\Dell\Desktop\face_recognition system\college_images\help_desk.jpg")
        img7=img7.resize((220,220),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)
        
        b1=Button(bg_img,command=self.help_data ,image=self.photoimg7,cursor="hand2")
        b1.place(x=1000,y=100,width=220,height=220)
        
        b1_1=Button(bg_img,command=self.help_data, text="Help Desk",cursor="hand2",font=("times new roman",20,"bold"),bg="darkgrey",fg="white")
        b1_1.place(x=1000,y=300,width=220,height=40)
        
        
        #Train button
        img8=Image.open(r"C:\Users\Dell\Desktop\face_recognition system\college_images\train_data.jpg")
        img8=img8.resize((220,220),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)
        
        b1=Button(bg_img,image=self.photoimg8,command=self.train_data, cursor="hand2")
        b1.place(x=100,y=350,width=220,height=220)
        
        b1_1=Button(bg_img,text="Train Data",command=self.train_data,cursor="hand2",font=("times new roman",20,"bold"),bg="darkgrey",fg="white")
        b1_1.place(x=100,y=550,width=220,height=40)
        
        
        #Photos face button
        img9=Image.open(r"C:\Users\Dell\Desktop\face_recognition system\college_images\photos.png")
        img9=img9.resize((220,220),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)
        
        b1=Button(bg_img,image=self.photoimg9, command=self.open_img ,cursor="hand2")
        b1.place(x=400,y=350,width=220,height=220)
        
        b1_1=Button(bg_img,text="Photos",command=self.open_img ,cursor="hand2",font=("times new roman",20,"bold"),bg="darkgrey",fg="white")
        b1_1.place(x=400,y=550,width=220,height=40)
        
        
        
        #developer  button
        img10=Image.open(r"C:\Users\Dell\Desktop\face_recognition system\college_images\developer.png")
        img10=img10.resize((220,220),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)
        
        b1=Button(bg_img,image=self.photoimg10, command=self.developer_data , cursor="hand2")
        b1.place(x=700,y=350,width=220,height=220)
        
        b1_1=Button(bg_img,text="Developer",command=self.developer_data ,cursor="hand2",font=("times new roman",20,"bold"),bg="darkgrey",fg="white")
        b1_1.place(x=700,y=550,width=220,height=40)
        
        
        #Exit button
        img11=Image.open(r"college_images\exit.jpg")
        img11=img11.resize((220,220),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)
        
        b1=Button(bg_img,image=self.photoimg11,command=self.iExit,cursor="hand2")
        b1.place(x=1000,y=350,width=220,height=220)
        
        b1_1=Button(bg_img,text="Exit",command=self.iExit,cursor="hand2",font=("times new roman",20,"bold"),bg="darkgrey",fg="white")
        b1_1.place(x=1000,y=550,width=220,height=40)
 
 
 

    #=================Function Buttons===================
        
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
        
    def open_img(self):
        os.startfile("data") 
    
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
    
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
        
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
    
    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)
        
    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)
        
    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure to exit this application!",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return
    
        
        
if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()     