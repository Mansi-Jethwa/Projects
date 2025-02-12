from tkinter import *
from PIL import ImageTk
import pymysql
from employees import employee_form
from supplier import supplier_form
from category import category_form
from products import product_form
from sales import sales_form

import os
from datetime import datetime  # Import datetime module

# GUI Part
window = Tk()
window.title("Dashboard")
window.geometry("1270x668+0+0")
window.resizable(0, 0)
window.config(bg='white')

def redirect_to_login():
    window.destroy()  # Close the current window
    os.system('python logine.py')
def exit_program():
    window.quit()  
# Load background image
bg_image = PhotoImage(file='inventory.png')

# Title label with image and text
titleLabel = Label(window, image=bg_image, compound=LEFT, text="Inventory Management System",
                   font=("times new roman", 40, "bold"), bg="#010c48", fg="white", anchor="w", padx=20)
titleLabel.place(x=0, y=0, relwidth=1)

logoutButton = Button(window, text="Logout", font=('times new roman', 20, 'bold'), fg='#010c48', command=redirect_to_login, cursor="hand2")
logoutButton.place(x=1100, y=10)

subtitleLabel = Label(window, text="Welcome Admin\t\t Date:15-11-2024\t\t Time:9:00:00pm", font=('times new roman', 15), bg='#4d636d', fg='white')
subtitleLabel.place(x=0, y=70, relwidth=1)

# Function to update date and time dynamically
def update_date_time():
    # Get the current date and time
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_date = now.strftime("%d-%m-%Y")
    
    # Update the subtitle label with the current date and time
    subtitleLabel.config(text=f"Welcome Admin\t\t Date: {current_date}\t\t Time: {current_time}")
    
    # Call this function every 1000ms (1 second)
    window.after(1000, update_date_time)

# Call update_date_time() to start updating the label
update_date_time()

leftFrame = Frame(window)
leftFrame.place(x=0, y=102, width=200, height=555)

logoImage = PhotoImage(file='logo.png')
imageLabel = Label(leftFrame, image=logoImage)
imageLabel.grid(row=0, column=0)

menuLabel = Label(leftFrame, text="Menu", font=('times new roman', 20), bg='#009688')
menuLabel.grid(row=1, column=0, pady=10)
menuLabel.place(width=200, y=150)

import os

# Button for Employees
dash_icon = ImageTk.PhotoImage(file='dash.png')
dash_button = Button(leftFrame, image=dash_icon, compound=LEFT, text=" Dashboard", font=('times new roman', 20, 'bold'), anchor="w", command=lambda: os.system('python dashboard.py'))
dash_button.grid(row=2, column=0, pady=10, padx=10)
dash_button.place(width=200, y=185, height=50)


employee_icon = ImageTk.PhotoImage(file='employee.png')
employee_button = Button(leftFrame, image=employee_icon, compound=LEFT, text=" Employees", font=('times new roman', 20, 'bold'), anchor="w", command=lambda: employee_form(window))
employee_button.grid(row=3, column=0, pady=10, padx=10)
employee_button.place(width=200, y=234, height=50)

# Remaining code for buttons, frames, and labels
# ...

supplier_icon=ImageTk.PhotoImage(file='supplier.png')
supplier_button=Button(leftFrame,image=supplier_icon,compound=LEFT,text=" Supplier",font=('times new roman',20,'bold'),anchor="w",command=lambda :supplier_form(window))
supplier_button.grid(row=3,column=0,pady=10,padx=10)
supplier_button.place(width=200,y=284,height=50)

category_icon=ImageTk.PhotoImage(file='category.png')
category_button=Button(leftFrame,image=category_icon,compound=LEFT,text=" Categories",font=('times new roman',20,'bold'),anchor="w",command=lambda:category_form(window))
category_button.grid(row=5,column=0,pady=10,padx=10)
category_button.place(width=200,y=334,height=50)

products_icon=ImageTk.PhotoImage(file='product.png')
products_button=Button(leftFrame,image=products_icon,compound=LEFT,text=" Products",font=('times new roman',20,'bold'),anchor="w",command=lambda:product_form(window))
products_button.grid(row=6,column=0,pady=10,padx=10)
products_button.place(width=200,y=384,height=50)

sales_icon=ImageTk.PhotoImage(file='sales.png')
sales_button=Button(leftFrame,image=sales_icon,compound=LEFT,text=" Sales",font=('times new roman',20,'bold'),anchor="w",command=lambda:sales_form(window))
sales_button.grid(row=7,column=0,pady=10,padx=10)
sales_button.place(width=200,y=434,height=50)

exit_icon = ImageTk.PhotoImage(file='exit.png')
exit_button = Button(leftFrame, image=exit_icon, compound=LEFT, text=" Exit", font=('times new roman', 20, 'bold'), anchor="w", command=exit_program)
exit_button.grid(row=8, column=0, pady=10, padx=10)
exit_button.place(width=200, y=484, height=50)
try:
    conn = pymysql.connect(host='localhost', user='root', password='', database='inventory_system')
    cursor = conn.cursor()

    # Execute queries to get counts
    cursor.execute("SELECT COUNT(*) FROM employee_data")
    total_employees = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM supplier_data")
    total_suppliers = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM category_data")
    total_categories = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM product_data")
    total_products = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM bills")  # Assuming you have a 'sales' table
    total_sales = cursor.fetchone()[0]

except pymysql.Error as e:
    print("Error connecting to database:", e)
    total_employees = 0
    total_suppliers = 0
    total_categories = 0
    total_products = 0
    total_sales = 0
finally:
    if conn:
        conn.close()
emp_frame = Frame(window, bg='#2c3e50', bd=3, relief='ridge')
emp_frame.place(x=400, y=100, height=170, width=280)
total_emp_icon = PhotoImage(file='staff.png')
total_emp_icon_label = Label(emp_frame, image=total_emp_icon, bg='#2c3e50')
total_emp_icon_label.grid(row=0, column=0, padx=0)
total_emp_icon_label.place(x=110)
total_emp_label = Label(emp_frame, text="Total Employees", bg='#2c3e50', fg='white', font=('times new roman', 15, 'bold'))
total_emp_label.grid(row=1, column=0, padx=105, pady=10)
total_emp_label.place(x=70, y=50)
total_emp_count_label = Label(emp_frame, text=str(total_employees), bg='#2c3e50', fg='white', font=('times new roman', 30, 'bold'))
total_emp_count_label.grid(row=2, column=0, padx=105, pady=10)
total_emp_count_label.place(x=130, y=80)

sup_frame=Frame(window,bg='#8e44ad',bd=3,relief='ridge')
sup_frame.place(x=800,y=100,height=170,width=280)
total_sup_icon=PhotoImage(file='suppliers.png')
total_sup_icon_label=Label(sup_frame,image=total_sup_icon,bg='#8e44ad')
total_sup_icon_label.grid(row=0,column=0,padx=0)
total_sup_icon_label.place(x=110)
total_sup_label=Label(sup_frame,text="Total Suppliers",bg='#8e44ad',fg='white',font=('times new roman',15,'bold'))
total_sup_label.grid(row=1,column=0,padx=105, pady=10)
total_sup_label.place(x=70,y=50)
total_sup_count_label=Label(sup_frame,text=str(total_suppliers),bg='#8e44ad',fg='white',font=('times new roman',30,'bold'))
total_sup_count_label.grid(row=2,column=0,padx=105, pady=10)
total_sup_count_label.place(x=130,y=80)

cat_frame=Frame(window,bg='#27ae60',bd=3,relief='ridge')
cat_frame.place(x=400,y=285,height=170,width=280)
total_cat_icon=PhotoImage(file='options.png')
total_cat_icon_label=Label(cat_frame,image=total_cat_icon,bg='#27ae60')
total_cat_icon_label.grid(row=0,column=0,padx=0,pady=30)
total_cat_icon_label.place(x=110,y=10)
total_cat_label=Label(cat_frame,text="Total Categories",bg='#27ae60',fg='white',font=('times new roman',15,'bold'))
total_cat_label.grid(row=1,column=0,padx=105, pady=10)
total_cat_label.place(x=70,y=60)
total_cat_count_label=Label(cat_frame,text=str(total_categories),bg='#27ae60',fg='white',font=('times new roman',30,'bold'))
total_cat_count_label.grid(row=2,column=0,padx=105, pady=10)
total_cat_count_label.place(x=130,y=90)

prod_frame=Frame(window,bg='#daa520',bd=3,relief='ridge')
prod_frame.place(x=800,y=285,height=170,width=280)
total_prod_icon=PhotoImage(file='products.png')
total_prod_icon_label=Label(prod_frame,image=total_prod_icon,bg='#daa520')
total_prod_icon_label.grid(row=0,column=0,padx=0)
total_prod_icon_label.place(x=110,y=10)
total_prod_label=Label(prod_frame,text="Total Products",bg='#daa520',fg='white',font=('times new roman',15,'bold'))
total_prod_label.grid(row=1,column=0,padx=105, pady=10)
total_prod_label.place(x=70,y=65)
total_prod_count_label=Label(prod_frame,text=str(total_products),bg='#daa520',fg='white',font=('times new roman',30,'bold'))
total_prod_count_label.grid(row=2,column=0,padx=105, pady=10)
total_prod_count_label.place(x=130,y=95)

sales_frame=Frame(window,bg='#de3163',bd=3,relief='ridge')
sales_frame.place(x=600,y=470,height=170,width=280)
total_sales_icon=PhotoImage(file='trend.png')
total_sales_icon_label=Label(sales_frame,image=total_sales_icon,bg='#de3163')
total_sales_icon_label.grid(row=0,column=0,padx=0)
total_sales_icon_label.place(x=110,y=10)
total_sales_label=Label(sales_frame,text="Total Sales",bg='#de3163',fg='white',font=('times new roman',15,'bold'))
total_sales_label.grid(row=1,column=0,padx=105, pady=10)
total_sales_label.place(x=90,y=65)
total_sales_count_label=Label(sales_frame,text=str(total_sales),bg='#de3163',fg='white',font=('times new roman',30,'bold'))
total_sales_count_label.grid(row=2,column=0,padx=105, pady=10)
total_sales_count_label.place(x=130,y=95)

# Main event loop
window.mainloop()