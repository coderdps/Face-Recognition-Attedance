from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        #title
        title_lbl=Label(self.root,text="Help Desk",font=("times new roman",35,"bold"),bg="grey",fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=55)
        
        #top image
        img_top=Image.open(r"C:\Users\Dell\Desktop\face_recognition system\college_images\help_desk.png")
        img_top=img_top.resize((1530,720),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=720)
        
        dev1_label=Label(f_lbl, text="Email:srivastavadipendra@gmail.com", font=("times new roman",15,"bold"))
        dev1_label.place(x=600,y=150)
        
        dev1_label=Label(f_lbl, text="Email:srivastavakajal679@gmail.com", font=("times new roman",15,"bold"))
        dev1_label.place(x=600,y=180)

        dev1_label=Label(f_lbl, text="Email:prabhudutt25@gmail.com", font=("times new roman",15,"bold"))
        dev1_label.place(x=600,y=210)
        
        dev1_label=Label(f_lbl, text="Email:priyanshisingh966@gmail.com", font=("times new roman",15,"bold"))
        dev1_label.place(x=600,y=240)




if __name__=="__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()     