import customtkinter as ctk
from tkinter import messagebox
import mysql.connector
import os

class Login_System:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#fafafa")

        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")

        # Variables
        self.employee_id = ctk.StringVar()
        self.password = ctk.StringVar()

        # Login Frame
        login_frame = ctk.CTkFrame(self.root, corner_radius=10, width=350, height=460)
        login_frame.place(x=650, y=90)

        ctk.CTkLabel(login_frame, text="Login", font=("Arial Black", 30, "bold"), bg_color="transparent").place(x=0, y=30)

        ctk.CTkLabel(login_frame, text="Employee Id", font=("Andalus", 15)).place(x=50, y=100)
        ctk.CTkEntry(login_frame, textvariable=self.employee_id, font=('times new roman', 15), width=250).place(x=50, y=140)

        ctk.CTkLabel(login_frame, text="Password", font=("Andalus", 15)).place(x=50, y=200)
        ctk.CTkEntry(login_frame, textvariable=self.password, show="*", font=('times new roman', 15), width=250).place(x=50, y=240)

        ctk.CTkButton(login_frame, text="Log In", command=self.login, font=("Arial Rounded MT Bold", 15, "bold"),
                      corner_radius=8, height=35, width=250).place(x=50, y=300)

    def login(self):
        con = None
        try:
            # Database Connection
            con = mysql.connector.connect(host="localhost", user="root", password="", database="inventory_system")
            cur = con.cursor()

            if not self.employee_id.get() or not self.password.get():
                messagebox.showerror("Error", "All Fields are required", parent=self.root)
                return

            cur.execute("SELECT usertype FROM employee_data WHERE empid=%s AND password=%s",
                        (self.employee_id.get(), self.password.get()))
            user = cur.fetchone()
            if user is None:
                messagebox.showerror('Error', 'Invalid USERNAME/PASSWORD', parent=self.root)
            else:
                self.root.destroy()
                os.system(f"python {'dashboard.py' if user[0] == 'Admin' else 'billing.py'}")

        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"MySQL Error: {err}", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        finally:
            if con:
                con.close()

if __name__ == "__main__":
    root = ctk.CTk()
    app = Login_System(root)
    root.mainloop()
