from tkinter import *
from PIL import ImageTk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
import mysql.connector
from datetime import date
import re

import re

def validate_fields(empid, name, email, gender, contact, employement_type, education, work_shift, address, salary, user_type, password):
    # Trim input fields
    name = name.strip()
    email = email.strip()
    contact = contact.strip()
    address = address.strip()
    salary = salary.strip()
    password = password.strip()
    empid = empid.strip()

    # Check for empty required fields
    if not empid or not name or not email or gender == 'Select Gender' or not contact or employement_type == 'Select Employment Type' or education == 'Select Education' or work_shift == 'Select Work Shift' or not address or not salary or user_type == 'Select User Type' or not password:
        return False, "All fields are required!"

    # Validate email format
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not re.match(email_regex, email):
        return False, "Please enter a valid email address!"

    # Validate contact number (exactly 10 digits)
    if not contact.isdigit() or len(contact) != 10:
        return False, "Please enter a valid 10-digit contact number!"

    # Validate salary (ensure it's a valid positive number)
    try:
        salary_value = float(salary)
        if salary_value <= 0:
            return False, "Salary must be a positive number!"
    except ValueError:
        return False, "Please enter a valid salary (numeric value)."

    # Validate password strength (at least 8 characters, and must contain letters, numbers, and special characters)
    if len(password) < 8 or not re.search(r'[a-z]', password) or not re.search(r'[A-Z]', password) or not re.search(r'[0-9]', password) or not re.search(r'[@$!%*?&]', password):
        return False, "Password must be at least 8 characters long and include one lowercase letter, one uppercase letter, one number, and one special character."

    # Validate dropdown selections
    if gender == 'Select Gender':
        return False, "Please select a gender!"
    if employement_type == 'Select Employment Type':
        return False, "Please select an employment type!"
    if education == 'Select Education':
        return False, "Please select an education level!"
    if work_shift == 'Select Work Shift':
        return False, "Please select a work shift!"
    if user_type == 'Select User Type':
        return False, "Please select a user type!"
    
    # Validate address length
    if len(address) < 10:
        return False, "Address should be at least 10 characters long!"

    # If all validations pass
    return True, ""

def connect_database():
    mydb = mysql.connector.connect(host="localhost", user="root", password="")
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS inventory_system")
    print("Database is created")
    mycursor.execute("USE inventory_system")
    # Removed AUTO_INCREMENT from empid
    mycursor.execute("CREATE TABLE IF NOT EXISTS employee_data (empid INT PRIMARY KEY, name VARCHAR(100), email VARCHAR(100), gender VARCHAR(50), dob VARCHAR(30), contact VARCHAR(30), employement_type VARCHAR(50), education VARCHAR(50), work_shift VARCHAR(50), address VARCHAR(100), doj VARCHAR(30), salary VARCHAR(50), usertype VARCHAR(50),password VARCHAR(50))")
    print("Table is Created")
    return mycursor
connect_database()


def treeview_data():
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="inventory_system")
    mycursor=mydb.cursor()
    mycursor.execute("SELECT * from employee_data")
    employee_records=mycursor.fetchall()
    employee_treeview.delete(*employee_treeview.get_children())
    for record in employee_records:
        employee_treeview.insert('',END,values=record)

def select_data(event,empid_entry,name_entry,email_entry,dob_date_entry,gender_combobox,contact_entry,employement_type_combobox,education_combobox,work_shift_combobox,address_text,doj_date_entry,salary_entry,usertype_combobox,password_entry):
    index=employee_treeview.selection()
    content=employee_treeview.item(index)
    row=content['values']
    clear_fields(empid_entry,name_entry,email_entry,dob_date_entry,gender_combobox,contact_entry,employement_type_combobox,education_combobox,work_shift_combobox,address_text,doj_date_entry,salary_entry,usertype_combobox,password_entry,False)
    empid_entry.insert(0,row[0])
    name_entry.insert(0,row[1])
    email_entry.insert(0,row[2])
    gender_combobox.set(row[3])
    doj_date_entry.set_date(row[4])
    contact_entry.insert(0,row[5])
    employement_type_combobox.set(row[6])
    education_combobox.set(row[7])
    work_shift_combobox.set(row[8])
    address_text.insert(1.0,row[9])
    doj_date_entry.set_date(row[10])
    salary_entry.insert(0,row[11])
    usertype_combobox.set(row[12])
    password_entry.insert(0,row[13])


def add_employee(empid, name, email, gender, dob, contact, employement_type, education, work_shift, address, doj, salary, user_type, password,empid_entry, name_entry, email_entry, dob_date_entry, gender_combobox, contact_entry, employement_type_combobox, education_combobox, work_shift_combobox, address_text, doj_date_entry, salary_entry, usertype_combobox, password_entry):
    valid, message = validate_fields(empid, name, email, gender, contact, employement_type, education, work_shift, address, salary, user_type, password)
    if not valid:
        messagebox.showerror('Error', message)
        return

    if (empid == '' or name == '' or gender == 'Select Gender' or contact == '' or employement_type == 'Select Employment Type' or education == 'Select Education' or work_shift == 'Select Work Shift' or address == '\n' or salary == '' or user_type == 'Select User Type' or password == ''):
        messagebox.showerror('Error', 'All Fields are Required')
    else:
        mydb = mysql.connector.connect(host="localhost", user="root", password="", database="inventory_system")
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM employee_data WHERE empid = %s", (empid,))
        existing_empid = mycursor.fetchone()

        if existing_empid:
            messagebox.showerror('Error', 'Employee ID already exists!')
            return

        # Proceed to insert the data if empid is unique
        mycursor.execute('INSERT INTO employee_data (empid, name, email, gender, dob, contact, employement_type, education, work_shift, address, doj, salary, usertype, password) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', 
                        (empid, name, email, gender, dob, contact, employement_type, education, work_shift, address, doj, salary, user_type, password))

        mydb.commit()
        treeview_data()
        messagebox.showinfo('Success', 'Data is inserted Successfully')
        clear_fields(empid_entry, name_entry, email_entry, dob_date_entry, gender_combobox, contact_entry, employement_type_combobox, education_combobox, work_shift_combobox, address_text, doj_date_entry, salary_entry, usertype_combobox, password_entry, True)

def clear_fields(empid_entry,name_entry,email_entry,dob_date_entry,gender_combobox,contact_entry,employement_type_combobox,education_combobox,work_shift_combobox,address_text,doj_date_entry,salary_entry,usertype_combobox,password_entry,check):
    empid_entry.delete(0,END)
    name_entry.delete(0,END)
    email_entry.delete(0,END)
    from datetime import date
    dob_date_entry.set_date(date.today())
    gender_combobox.set('Select Gender')
    contact_entry.delete(0,END)
    employement_type_combobox.set('Select Employement Type')
    education_combobox.set('Select Education')
    work_shift_combobox.set('Select Work Shift')
    address_text.delete(1.0,END)
    doj_date_entry.set_date(date.today())
    salary_entry.delete(0,END)
    usertype_combobox.set('Select User Type')
    password_entry.delete(0,END)
    if check:
        employee_treeview.selection_remove(employee_treeview.selection())

def update_employee(empid, name, email, gender, dob, contact, employement_type, education, work_shift, address, doj, salary, user_type, password,empid_entry, name_entry, email_entry, dob_date_entry, gender_combobox, contact_entry, employement_type_combobox, education_combobox, work_shift_combobox, address_text, doj_date_entry, salary_entry, usertype_combobox, password_entry):
    valid, message = validate_fields(empid,name, email, gender, contact, employement_type, education, work_shift, address, salary, user_type, password)
    if not valid:
        messagebox.showerror('Error', message)
        return
    selected=employee_treeview.selection()
    if not selected:
        messagebox.showerror('Error','No row is selected')
    else:
        mydb=mysql.connector.connect(host="localhost",user="root",password="",database="inventory_system")
        mycursor=mydb.cursor()
        mycursor.execute('UPDATE employee_data SET name=%s,email=%s,gender=%s,dob=%s,contact=%s,employement_type=%s,education=%s,work_shift=%s,address=%s,doj=%s,salary=%s,usertype=%s,password=%s WHERE empid=%s',(name,email,gender,dob,contact,employement_type,education,work_shift,address,doj,salary,user_type,password,empid,))
        mydb.commit()
        treeview_data()
        messagebox.showinfo('Success','Data is updated successfully')
        clear_fields(empid_entry, name_entry, email_entry, dob_date_entry, gender_combobox, contact_entry, employement_type_combobox, education_combobox, work_shift_combobox, address_text, doj_date_entry, salary_entry, usertype_combobox, password_entry, True)


def delete_employee(empid,empid_entry, name_entry, email_entry, dob_date_entry, gender_combobox, contact_entry, employement_type_combobox, education_combobox, work_shift_combobox, address_text, doj_date_entry, salary_entry, usertype_combobox, password_entry):
    selected=employee_treeview.selection()
    if not selected:
        messagebox.showerror('Error','No row is selected')
    else:
        result=messagebox.askyesno('Confirm','Do you really want to delete the record?')
        if result:
            mydb=mysql.connector.connect(host="localhost",user="root",password="",database="inventory_system")
            mycursor=mydb.cursor()
            mycursor.execute('DELETE FROM employee_data where empid=%s',(empid,))
            mydb.commit()
            treeview_data()
            messagebox.showinfo('Success','Data is deleted successfully')
            clear_fields(empid_entry, name_entry, email_entry, dob_date_entry, gender_combobox, contact_entry, employement_type_combobox, education_combobox, work_shift_combobox, address_text, doj_date_entry, salary_entry, usertype_combobox, password_entry, True)


def search_employee(search_option, value):
    # Map the search option to the corresponding column in the database
    column_mapping = {
        "Id": "empid",
        "Name": "name",
        "Email": "email"
    }

    # Validate inputs
    if search_option == "Search By":
        messagebox.showerror("Error", "Please select a valid search option")
        return
    elif not value.strip():
        messagebox.showerror("Error", "Please enter a value to search")
        return

    # Get the column name from the mapping
    column_name = column_mapping.get(search_option)
    if not column_name:
        messagebox.showerror("Error", "Invalid search option")
        return

    try:
        # Connect to the database
        mydb = mysql.connector.connect(
            host="localhost", user="root", password="", database="inventory_system"
        )
        mycursor = mydb.cursor()

        # Prepare the query with placeholders for the column and search value
        query = f"SELECT * FROM employee_data WHERE {column_name} LIKE %s"
        mycursor.execute(query, (f"%{value}%",))

        # Fetch the results
        records = mycursor.fetchall()

        # Clear the existing rows in the Treeview
        employee_treeview.delete(*employee_treeview.get_children())

        # Insert the fetched records into the Treeview
        for record in records:
            employee_treeview.insert("", END, values=record)

        # Handle case when no records are found
        if not records:
            messagebox.showinfo("Info", "No matching records found")

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Database error: {err}")
    finally:
        if 'mydb' in locals() and mydb.is_connected():
            mycursor.close()
            mydb.close()

def show_all(search_entry,search_combobox):
    treeview_data()
    search_entry.delete(0,END)
    search_combobox.set('Search By')


def employee_form(window):
    global back_image,employee_treeview
    employee_frame=Frame(window,width=1070,height=567,bg='white')
    employee_frame.place(x=200,y=100)
    heading_Label=Label(employee_frame,text='Manage Employee Details',font=('times new roman',16,'bold'),bg='#0f4d7d',fg='white')
    heading_Label.place(x=0,y=0,relwidth=1)
    top_frame=Frame(employee_frame,bg='white')
    top_frame.place(x=0,y=30,relwidth=1)
    back_image=PhotoImage(file='arrow.png')
    back_button = Button(top_frame, image=back_image, bd=0, cursor='hand2',bg='white', command=lambda: employee_frame.place_forget())
    back_button.place(x=10,y=5)
    search_frame=Frame(top_frame,bg='white')
    search_frame.place(x=240)
    search_combobox=ttk.Combobox(search_frame,values=('Id','Name','Email'),font=('times new roman',12),state='readonly')
    search_combobox.set('Search By')
    search_combobox.grid(row=0,column=0,padx=20)
    search_entry=Entry(search_frame,font=('times new roman',12),bg='lightyellow')
    search_entry.grid(row=0,column=1)
    search_button=Button(search_frame,text='SEARCH',width=10,font=('times new roman',12,'bold'),bg="#0f4d7d", fg="white", cursor='hand2',command=lambda :search_employee(search_combobox.get(),search_entry.get()))
    search_button.grid(row=0,column=2,padx=20)
    show_button=Button(search_frame,text='SHOW ALL',width=10,font=('times new roman',12,'bold'),bg="#0f4d7d", fg="white", cursor='hand2',command=lambda :show_all(search_entry,search_combobox))
    show_button.grid(row=0,column=3,padx=10)

    # Add the Treeview and scrollbars
    horizontal_scrollbar = Scrollbar(top_frame, orient=HORIZONTAL)
    vertical_scrollbar = Scrollbar(top_frame, orient=VERTICAL)

# Create the Treeview and link scrollbars
    employee_treeview = ttk.Treeview(
    top_frame,
    columns=(
        'empid', 'name', 'email', 'gender', 'dob', 'contact', 
        'employement_type', 'education', 'work_shift', 'address', 
        'doj', 'salary', 'usertype'
    ),
    show='headings',
    yscrollcommand=vertical_scrollbar.set,
    xscrollcommand=horizontal_scrollbar.set
    )

# Configure scrollbars to work with the Treeview
    horizontal_scrollbar.config(command=employee_treeview.xview)
    vertical_scrollbar.config(command=employee_treeview.yview)

# Place Treeview and scrollbars
    employee_treeview.place(x=100,y=200,height=200,width=100)
    employee_treeview.grid(row=0, column=0, padx=10, pady=40)
    vertical_scrollbar.grid(row=0, column=1,sticky='ns')
    horizontal_scrollbar.grid(row=1, column=0, sticky='ew', padx=10)


    horizontal_scrollbar.place(x=10,y=255,width=1050)
    vertical_scrollbar.place(x=1050,y=50,height=200)


# Define Treeview columns and headings
    employee_treeview.heading('empid', text='EmpId')
    employee_treeview.heading('name', text='Name')
    employee_treeview.heading('email', text='Email')
    employee_treeview.heading('gender', text='Gender')
    employee_treeview.heading('dob', text='Date Of Birth')
    employee_treeview.heading('contact', text='Contact')
    employee_treeview.heading('employement_type', text='Employement Type')
    employee_treeview.heading('education', text='Education')
    employee_treeview.heading('work_shift', text='Work Shift')
    employee_treeview.heading('address', text='Address')
    employee_treeview.heading('doj', text='Date of Joining')
    employee_treeview.heading('salary', text='Salary')
    employee_treeview.heading('usertype', text='User Type')

    employee_treeview.column('empid', width=60)
    employee_treeview.column('name', width=140)
    employee_treeview.column('email', width=180)
    employee_treeview.column('gender', width=80)
    employee_treeview.column('dob', width=100)
    employee_treeview.column('contact', width=100)
    employee_treeview.column('employement_type', width=120)
    employee_treeview.column('education', width=120)
    employee_treeview.column('work_shift', width=100)
    employee_treeview.column('address', width=200)
    employee_treeview.column('doj', width=100)
    employee_treeview.column('salary', width=140)
    employee_treeview.column('usertype', width=120)

    treeview_data()
    
    top_frame.grid_rowconfigure(0, weight=1)
    top_frame.grid_columnconfigure(0, weight=1)

    detail_frame=Frame(employee_frame,bg='white')
    detail_frame.place(x=0,y=300)

    empid_label=Label(detail_frame,text='EmpId',font=('times new roman',12,'bold'),bg='white')
    empid_label.grid(row=0,column=0,padx=20,pady=10,sticky="w")
    empid_entry=Entry(detail_frame,font=('times new roman',12),bg='lightyellow')
    empid_entry.grid(row=0,column=1,padx=20,pady=10)

    name_label=Label(detail_frame,text='Name',font=('times new roman',12,'bold'),bg='white')
    name_label.grid(row=0,column=2,padx=20,pady=10,sticky="w")
    name_entry=Entry(detail_frame,font=('times new roman',12),bg='lightyellow')
    name_entry.grid(row=0,column=3,padx=20,pady=10)

    email_label=Label(detail_frame,text='Email',font=('times new roman',12,'bold'),bg='white')
    email_label.grid(row=0,column=4,padx=20,pady=10,sticky="w")
    email_entry=Entry(detail_frame,font=('times new roman',12),bg='lightyellow')
    email_entry.grid(row=0,column=5,padx=20,pady=10)

    gender_label=Label(detail_frame,text='Gender',font=('times new roman',12,'bold'),bg='white')
    gender_label.grid(row=1,column=0,padx=20,pady=5,sticky="w")
    gender_combobox=ttk.Combobox(detail_frame,values=('Male','Female'),font=('times new roman',12),width=18,state='readonly')
    gender_combobox.set('Select Gender')
    gender_combobox.grid(row=1,column=1,padx=20,pady=5)

    dob_label=Label(detail_frame,text='Date Of Birth',font=('times new roman',12,'bold'),bg='white')
    dob_label.grid(row=1,column=2,padx=20,pady=5,sticky="w")
    dob_date_entry=DateEntry(detail_frame,width=18,font=('times new roman',12),state='readonly',date_pattern='dd/mm/yyyy')
    dob_date_entry.grid(row=1,column=3,padx=20,pady=5)

    contact_label=Label(detail_frame,text='Contact',font=('times new roman',12,'bold'),bg='white')
    contact_label.grid(row=1,column=4,padx=20,pady=5,sticky="w")
    contact_entry=Entry(detail_frame,font=('times new roman',12),bg='lightyellow')
    contact_entry.grid(row=1,column=5,padx=20,pady=5)

    employement_type_label=Label(detail_frame,text='Employement Type',font=('times new roman',12,'bold'),bg='white')
    employement_type_label.grid(row=2,column=0,padx=20,pady=5,sticky="w")
    employement_type_combobox=ttk.Combobox(detail_frame,values=('Full Time','Part Time','Casual','Contract','Intern'),font=('times new roman',12),width=18,state='readonly')
    employement_type_combobox.set('Select Employement Type')
    employement_type_combobox.grid(row=2,column=1,padx=20,pady=5)

    education_label=Label(detail_frame,text='Education',font=('times new roman',12,'bold'),bg='white')
    education_label.grid(row=2,column=2,padx=20,pady=5,sticky="w")
    education_options=['B.Tech','B.Com','M.Tech','B.Sc','M.Sc','BBA','MBA','LLB','LLM','B.Arch','M.Arch']
    education_combobox=ttk.Combobox(detail_frame,values=education_options,font=('times new roman',12),width=18,state='readonly')
    education_combobox.set('Select Education')
    education_combobox.grid(row=2,column=3,padx=20,pady=5)

    work_shift_label=Label(detail_frame,text='Work Shift',font=('times new roman',12,'bold'),bg='white')
    work_shift_label.grid(row=2,column=4,padx=20,pady=5,sticky="w")
    work_shift_combobox=ttk.Combobox(detail_frame,values=('Morning','Evening','Night'),font=('times new roman',12),width=18,state='readonly')
    work_shift_combobox.set('Select Work Shift')
    work_shift_combobox.grid(row=2,column=5,padx=20,pady=5)

    address_label=Label(detail_frame,text='Address',font=('times new roman',12,'bold'),bg='white')
    address_label.grid(row=3,column=0,padx=20,pady=5,sticky='w')
    address_text=Text(detail_frame,width=20,height=5)
    address_text.grid(row=3,column=1,rowspan=2)

    doj_label=Label(detail_frame,text='Date Of Joining',font=('times new roman',12,'bold'),bg='white')
    doj_label.grid(row=3,column=2,padx=20,pady=5,sticky="w")
    doj_date_entry=DateEntry(detail_frame,width=18,font=('times new roman',12),state='readonly',date_pattern='dd/mm/yyyy')
    doj_date_entry.grid(row=3,column=3,padx=20,pady=5)

    usertype_label=Label(detail_frame,text='User Type',font=('times new roman',12,'bold'),bg='white')
    usertype_label.grid(row=4,column=2,padx=20,pady=5,sticky="w")
    usertype_combobox=ttk.Combobox(detail_frame,values=('Admin','Employee'),font=('times new roman',12),width=18,state='readonly')
    usertype_combobox.set('Select User Type')
    usertype_combobox.grid(row=4,column=3,padx=20,pady=5)

    salary_label=Label(detail_frame,text='Salary',font=('times new roman',12,'bold'),bg='white')
    salary_label.grid(row=3,column=4,padx=20,pady=5,sticky="w")
    salary_entry=Entry(detail_frame,font=('times new roman',12),bg='lightyellow')
    salary_entry.grid(row=3,column=5,padx=20,pady=5)

    password_label=Label(detail_frame,text='Password',font=('times new roman',12,'bold'),bg='white')
    password_label.grid(row=4,column=4,padx=20,pady=5,sticky="w")
    password_entry=Entry(detail_frame,font=('times new roman',12),bg='lightyellow')
    password_entry.grid(row=4,column=5,padx=20,pady=5)

    button_frame=Frame(employee_frame,bg='white')
    button_frame.place(x=200,y=510)
    ad_button=Button(button_frame,text='Add',font=('times new roman',12,'bold') ,width=10,cursor='hand2',fg='white',bg='#0f4d7d',command=lambda :add_employee(empid_entry.get(),name_entry.get(),email_entry.get(),gender_combobox.get(),dob_date_entry.get(),contact_entry.get(),employement_type_combobox.get(),education_combobox.get(),work_shift_combobox.get(),address_text.get(1.0,END),doj_date_entry.get(),salary_entry.get(),usertype_combobox.get(),password_entry.get(),empid_entry, name_entry, email_entry, dob_date_entry, gender_combobox, contact_entry, employement_type_combobox, education_combobox, work_shift_combobox, address_text, doj_date_entry, salary_entry, usertype_combobox, password_entry))
    ad_button.grid(row=0,column=0,padx=20)

    update_button=Button(button_frame,text='Update',font=('times new roman',12,'bold') ,width=10,cursor='hand2',fg='white',bg='#0f4d7d',command=lambda :update_employee(empid_entry.get(),name_entry.get(),email_entry.get(),gender_combobox.get(),dob_date_entry.get(),contact_entry.get(),employement_type_combobox.get(),education_combobox.get(),work_shift_combobox.get(),address_text.get(1.0,END),doj_date_entry.get(),salary_entry.get(),usertype_combobox.get(),password_entry.get(),empid_entry, name_entry, email_entry, dob_date_entry, gender_combobox, contact_entry, employement_type_combobox, education_combobox, work_shift_combobox, address_text, doj_date_entry, salary_entry, usertype_combobox, password_entry))
    update_button.grid(row=0,column=1,padx=20)

    delete_button=Button(button_frame,text='Delete',font=('times new roman',12,'bold') ,width=10,cursor='hand2',fg='white',bg='#0f4d7d',command=lambda :delete_employee(empid_entry.get(),empid_entry, name_entry, email_entry, dob_date_entry, gender_combobox, contact_entry, employement_type_combobox, education_combobox, work_shift_combobox, address_text, doj_date_entry, salary_entry, usertype_combobox, password_entry,))
    delete_button.grid(row=0,column=2,padx=20)

    clear_button=Button(button_frame,text='Clear',font=('times new roman',12,'bold') ,width=10,cursor='hand2',fg='white',bg='#0f4d7d',command=lambda :clear_fields(empid_entry,name_entry,email_entry,dob_date_entry,gender_combobox,contact_entry,employement_type_combobox,education_combobox,work_shift_combobox,address_text,doj_date_entry,salary_entry,usertype_combobox,password_entry,True))
    clear_button.grid(row=0,column=3,padx=20)
    employee_treeview.bind('<ButtonRelease-1>',lambda event:select_data(event,empid_entry,name_entry,email_entry,dob_date_entry,gender_combobox,contact_entry,employement_type_combobox,education_combobox,work_shift_combobox,address_text,doj_date_entry,salary_entry,usertype_combobox,password_entry))


