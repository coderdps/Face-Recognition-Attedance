from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        #title
        title_lbl=Label(self.root,text="Developer",font=("times new roman",35,"bold"),bg="grey",fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=55)
        
        #top image
        img_top=Image.open(r"C:\Users\Dell\Desktop\face_recognition system\college_images\developer1.png")
        img_top=img_top.resize((1530,720),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=720)
        
        #Frame
        main_frame=Frame(f_lbl, bd=2, bg="white")
        main_frame.place(x=700, y=0, width=500, height=600)
        
        #developer1 image
        img_dev1=Image.open(r"C:\Users\Dell\Desktop\face_recognition system\college_images\dipendra.jpg")
        img_dev1=img_dev1.resize((150,150),Image.ANTIALIAS)
        self.photoimg_dev1=ImageTk.PhotoImage(img_dev1)
        
        f_lbl1=Label(main_frame,image=self.photoimg_dev1)
        f_lbl1.place(x=350,y=0,width=150,height=150)
        
        #developer1 info
        dev1_label=Label(main_frame, text="Hi! My name is Dipendra", font=("times new roman",20,"bold"))
        dev1_label.place(x=0,y=0)
        dev1_label1=Label(main_frame, text="I am a Full Stack Developer", font=("times new roman",20,"bold"))
        dev1_label1.place(x=0,y=40)

        #developer2 image
        img_dev2 = Image.open(r"C:\Users\Dell\Desktop\face_recognition system\college_images\kajal.jpg")
        img_dev2 = img_dev2.resize((150, 150), Image.ANTIALIAS)
        self.photoimg_dev2 = ImageTk.PhotoImage(img_dev2)

        f_lbl2 = Label(main_frame, image=self.photoimg_dev2)
        f_lbl2.place(x=350, y=150, width=150, height=150)
        
        #developer2 info
        dev2_label=Label(main_frame, text="Hi! My name is Kajal", font=("times new roman",20,"bold"))
        dev2_label.place(x=0,y=150)
        dev2_label1=Label(main_frame, text="I am a Full Stack Developer", font=("times new roman",20,"bold"))
        dev2_label1.place(x=0,y=190)
        
        #developer3 image
        img_dev3=Image.open(r"C:\Users\Dell\Desktop\face_recognition system\college_images\prabhu.jpg")
        img_dev3=img_dev3.resize((150,150),Image.ANTIALIAS)
        self.photoimg_dev3=ImageTk.PhotoImage(img_dev3)
        
        f_lbl3=Label(main_frame,image=self.photoimg_dev3)
        f_lbl3.place(x=350,y=300,width=150,height=150)
        
        #developer3 info
        dev3_label=Label(main_frame, text="Hi! My name is Prabhu", font=("times new roman",20,"bold"))
        dev3_label.place(x=0,y=300)
        dev3_label1=Label(main_frame, text="I am a Full Stack Developer", font=("times new roman",20,"bold"))
        dev3_label1.place(x=0,y=340)

        #developer4 image
        img_dev4 = Image.open(r"C:\Users\Dell\Desktop\face_recognition system\college_images\priyanshi.jpg")
        img_dev4 = img_dev4.resize((150, 150), Image.ANTIALIAS)
        self.photoimg_dev4 = ImageTk.PhotoImage(img_dev4)

        f_lbl4 = Label(main_frame, image=self.photoimg_dev4)
        f_lbl4.place(x=350, y=450, width=150, height=150)
        
        #developer2 info
        dev4_label=Label(main_frame, text="Hi! My name is Priyanshi", font=("times new roman",20,"bold"))
        dev4_label.place(x=0,y=450)
        dev4_label1=Label(main_frame, text="I am a Full Stack Developer", font=("times new roman",20,"bold"))
        dev4_label1.place(x=0,y=490)
        
        




if __name__=="__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()     