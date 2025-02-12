from tkinter import *
from PIL import Image, ImageTk
import os  # For executing the dashboard.py script

# Function for login validation
def login():
    username = username_entry.get()
    password = password_entry.get()

    # Validate credentials
    if username == "admin" and password == "password":
        login_frame.pack_forget()  # Hide the login frame
        open_dashboard()  # Open the dashboard script
    else:
        error_label.config(text="Invalid username or password", fg="red")

# Function to open the dashboard.py script
def open_dashboard():
    # Close the current login window
    root.destroy()

    # Open dashboard.py using the os.system() command
    os.system("python dashboard.py")

# Create the main window
root = Tk()
root.title("Login - Inventory Management System")
root.geometry("1270x668+0+0")
root.resizable(False, False)
root.config(bg="white")

# Title bar with background
title_frame = Frame(root, bg="#010c48")
title_frame.place(x=0, y=0, relwidth=1, height=100)

# Title Label (centered vertically and horizontally)
title_label = Label(title_frame, text="Inventory Management System - Login", font=("Times New Roman", 30, "bold"),
                    bg="#010c48", fg="white", anchor="center")
title_label.place(relx=0.5, rely=0.5, anchor="center")  # Center vertically and horizontally

# Login Frame (centered)
login_frame = Frame(root, bg="white", relief=RIDGE)

# Calculate the center of the window to position the login frame
frame_width = 600
frame_height = 350
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Position of the top-left corner of the login frame to center it
x_position = (screen_width // 2) - (frame_width // 2)
y_position = (screen_height // 2) - (frame_height // 2)

login_frame.place(x=x_position, y=y_position, width=frame_width, height=frame_height)

# Load and add sidebar image
image_path = "login.png"  # Path to the uploaded image
sidebar_img = Image.open(image_path)
sidebar_img = sidebar_img.resize((200, 350))  # Resize the image to fit the sidebar
sidebar_photo = ImageTk.PhotoImage(sidebar_img)

image_label = Label(login_frame, image=sidebar_photo, bg="white")
image_label.place(x=0, y=0, width=200, height=350)

# Form Area in Login Frame
form_frame = Frame(login_frame, bg="white")
form_frame.place(x=210, y=0, width=380, height=350)

# Title for login form
login_title = Label(form_frame, text="Login", font=("Times New Roman", 25, "bold"), bg="white", fg="#333")
login_title.pack(pady=20)

# Username Label and Entry
username_label = Label(form_frame, text="Username:", font=("Arial", 14), bg="white", fg="#333")
username_label.pack(pady=5, anchor="w", padx=20)

username_entry = Entry(form_frame, font=("Arial", 14), bg="#f0f0f0", width=25)
username_entry.pack(pady=5)

# Password Label and Entry
password_label = Label(form_frame, text="Password:", font=("Arial", 14), bg="white", fg="#333")
password_label.pack(pady=5, anchor="w", padx=20)

password_entry = Entry(form_frame, font=("Arial", 14), bg="#f0f0f0", width=25, show="*")
password_entry.pack(pady=5)

# Error label for invalid credentials
error_label = Label(form_frame, text="", font=("Arial", 12), bg="white", fg="red")
error_label.pack(pady=5)

# Buttons
button_frame = Frame(form_frame, bg="white")
button_frame.pack(pady=20)

login_button = Button(button_frame, text="Login", font=("Arial", 14, "bold"), bg="#010c48", fg="white", width=10, command=login)
login_button.grid(row=0, column=0, padx=10)

cancel_button = Button(button_frame, text="Cancel", font=("Arial", 14, "bold"), bg="#010c48", fg="white", width=10, command=root.destroy)
cancel_button.grid(row=0, column=1, padx=10)

# Footer Label
footer_label = Label(root, text="© 2024 Inventory Management System", font=("Arial", 10), bg="white", fg="#aaa")
footer_label.place(x=0, y=640, relwidth=1)

# Run the app
root.mainloop()
