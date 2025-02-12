from customtkinter import *
from PIL import Image
import mysql.connector
from tkinter import messagebox
import os

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("600x480")
        self.root.resizable(0, 0)

        # Variables
        self.employee_id = StringVar()
        self.password = StringVar()

        # Load images
        try:
            side_img_data = Image.open("side-img.png")
            email_icon_data = Image.open("email-icon.png")
            password_icon_data = Image.open("password-icon.png")
            google_icon_data = Image.open("google-icon.png")
        except FileNotFoundError as e:
            print(f"Error: {e}")
            exit()

        side_img = CTkImage(light_image=side_img_data, size=(300, 480))
        email_icon = CTkImage(light_image=email_icon_data, size=(20, 20))
        password_icon = CTkImage(light_image=password_icon_data, size=(17, 17))
        google_icon = CTkImage(light_image=google_icon_data, size=(17, 17))

        # Left-side image
        CTkLabel(master=self.root, text="", image=side_img).pack(expand=True, side="left")

        # Right-side frame
        frame = CTkFrame(master=self.root, width=300, height=480, fg_color="#ffffff")
        frame.pack_propagate(0)
        frame.pack(expand=True, side="right")

        # Labels and input fields
        CTkLabel(master=frame, text="Welcome Back!", text_color="#601E88", anchor="w", justify="left",
                 font=("Arial Bold", 24)).pack(anchor="w", pady=(50, 5), padx=(25, 0))
        CTkLabel(master=frame, text="Sign in to your account", text_color="#7E7E7E", anchor="w", justify="left",
                 font=("Arial Bold", 12)).pack(anchor="w", padx=(25, 0))

        CTkLabel(master=frame, text="  Employee Id:", text_color="#601E88", anchor="w", justify="left",
                 font=("Arial Bold", 14), image=email_icon, compound="left").pack(anchor="w", pady=(38, 0), padx=(25, 0))
        CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#601E88", border_width=1,
                 text_color="#000000", textvariable=self.employee_id).pack(anchor="w", padx=(25, 0))

        CTkLabel(master=frame, text="  Password:", text_color="#601E88", anchor="w", justify="left",
                 font=("Arial Bold", 14), image=password_icon, compound="left").pack(anchor="w", pady=(21, 0), padx=(25, 0))
        CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#601E88", border_width=1,
                 text_color="#000000", show="*", textvariable=self.password).pack(anchor="w", padx=(25, 0))

        # Buttons
        CTkButton(master=frame, text="Login", fg_color="#601E88", hover_color="#E44982", font=("Arial Bold", 12),
                  text_color="#ffffff", width=225, command=self.login).pack(anchor="w", pady=(40, 0), padx=(25, 0))
        CTkButton(master=frame, text="Continue With Google", fg_color="#EEEEEE", hover_color="#EEEEEE",
                  font=("Arial Bold", 9), text_color="#601E88", width=225, image=google_icon).pack(anchor="w", pady=(20, 0), padx=(25, 0))

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
    app = CTk()
    LoginApp(app)
    app.mainloop()
