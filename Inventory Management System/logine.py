from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import mysql.connector
import os
class Login_System:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#fafafa")

        self.phone_image=ImageTk.PhotoImage(file="phone.png")
        self.lbl_Phone_image=Label(self.root,image=self.phone_image,bd=0).place(x=200,y=10)

        self.employee_id=StringVar()
        self.password=StringVar()

        login_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        login_frame.place(x=650,y=90,width=350,height=460)

        title=Label(login_frame,text="Login", font=("Arial Black",30,"bold"),bg="white").place(x=0,y=30,relwidth=1)

        
        lbl_user=Label(login_frame,text="Employee Id",font=("Andalus",15),bg="white",fg="#767171").place(x=50,y=100)
        txt_employee_id=Entry(login_frame,textvariable=self.employee_id,font=('times new roman',15),bg="#ececec").place(x=50,y=140,width=250)

        lbl_pass=Label(login_frame,text="Password",font=("Andalus",15),bg="white",fg="#767171").place(x=50,y=200)
        txt_pass=Entry(login_frame,textvariable=self.password,show="*",font=('times new roman',15),bg="#ececec").place(x=50,y=240,width=250)

        btn_login=Button(login_frame,text="Log In",command=self.login,font=("Arial Rounded MT Bold",15,"bold"),bg="#00b0f0",fg="white",activebackground="#00b0f0",activeforeground="white",bd=0,cursor="hand2").place(x=50,y=300,width=250,height=35)

        """hr=Label(login_frame,bg="lightgray").place(x=50,y=370,width=250,height=2)
        or_=Label(login_frame,text="OR",bg="white",fg="lightgray",font=("times new roman",15,"bold")).place(x=160,y=355)"""

        #btn_forget=Button(login_frame,text="Forget Password?",command=self.forget_window,font=("times new roman",13),bg="white",fg="#00759e",activebackground="white",activeforeground="#00759e",bd=0,cursor="hand2").place(x=110,y=390)

        self.im1=ImageTk.PhotoImage(file="im1.png")
        self.im2=ImageTk.PhotoImage(file="im2.png")
        self.im3=ImageTk.PhotoImage(file="im3.png")

        self.lbl_change_image=Label(self.root,bg="gray")
        self.lbl_change_image.place(x=367,y=113,width=240,height=428)

        self.animate()

    def animate(self):
        self.im=self.im1
        self.im1=self.im2
        self.im2=self.im3
        self.im3=self.im
        self.lbl_change_image.config(image=self.im)
        self.lbl_change_image.after(1500,self.animate)


    def login(self):
        con = mysql.connector.connect(host="localhost", user="root", password="", database="inventory_system")
        cur = con.cursor()
        try:
            if self.employee_id.get() == "" or self.password.get() == "":
                messagebox.showerror("Error", "All Fields are required", parent=self.root)
            else:
            # Use %s placeholders for MySQL queries
                cur.execute("SELECT usertype FROM employee_data WHERE empid=%s AND password=%s", 
                        (self.employee_id.get(), self.password.get()))
                user = cur.fetchone()  # Corrected fetchone method
                if user is None:
                    messagebox.showerror('Error', 'Invalid USERNAME/PASSWORD', parent=self.root)
                else:
                    if user[0]=="Admin":
                        self.root.destroy()
                        os.system("python dashboard.py")
                    else:
                        self.root.destroy()
                        os.system("python billing.py")
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
    
    """def forget_window(self):
        con = mysql.connector.connect(host="localhost", user="root", password="", database="inventory_system")
        cur = con.cursor()
        try:
            if self.employee_id.get()=="":
                messagebox.showerror('Error','Employee ID must be required',parent=self.root)
            else:
                cur.execute("SELECT usertype FROM employee_data WHERE empid=%s",(self.employee_id.get(),))
                email = cur.fetchone()
                if email is None:
                    messagebox.showerror('Error', 'Invalid Employee ID, try again', parent=self.root)
                else:
                    self.var_otp=StringVar()
                    self.var_new_pass=StringVar
                    self.var_conf_pass=StringVar
                    self.forget_win=Toplevel(self.root)
                    self.forget_win.title('RESET PASSWORD')
                    self.forget_win.geometry('400x350+500+100')
                    self.forget_win.focus_force()
                    
                    title=Label(self.forget_win,text='Reset Password',font=('goudy old style',15,'bold'),bg='#3f51b5',fg="white").pack(side=TOP,fill=X)
                    lbl_reset=Label(self.forget_win,text="Enter OTP Sent on Registered Email",font=('times new roman',15)).place(x=20,y=60)
                    txt_reset=Entry(self.forget_win,textvariable=self.var_otp,font=('times new roman',15),bg="lightyellow").place(x=20,y=100,width=250,height=30)
                    
                    self.btn_reset=Button(self.forget_win,text="SUBMIT",font=('times new roman',15),bg="lightblue",bd=0,cursor="hand2").place(x=280,y=100,width=100,height=30)

                    lbl_new_pass=Label(self.forget_win,text="New Password",font=('times new roman',15)).place(x=20,y=160)
                    txt_new_pass=Entry(self.forget_win,textvariable=self.var_new_pass,font=('times new roman',15),bg="lightyellow").place(x=20,y=190,width=250,height=30)

                    lbl_c_pass=Label(self.forget_win,text="Confirm Password",font=('times new roman',15)).place(x=20,y=225)
                    txt_c_pass=Entry(self.forget_win,textvariable=self.var_conf_pass,font=('times new roman',15),bg="lightyellow").place(x=20,y=255,width=250,height=30)

                    self.btn_update=Button(self.forget_win,text="UPDATE",font=('times new roman',15),bg="lightblue",bd=0,cursor="hand2").place(x=150,y=300,width=100,height=30)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)"""


root=Tk()
obj=Login_System(root)
root.mainloop()