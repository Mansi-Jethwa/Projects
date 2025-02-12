from tkinter import *
from PIL import ImageTk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
import mysql.connector
from datetime import date

# Function to connect to the database and set up the necessary table
# Function to connect to the database and set up the necessary table
def connect_database():
    mydb = mysql.connector.connect(host="localhost", user="root", password="")
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS inventory_system")
    mycursor.execute("USE inventory_system")
    mycursor.execute("CREATE TABLE IF NOT EXISTS category_data (id INT PRIMARY KEY,name VARCHAR(100),description TEXT)")
    print("Database and Category Table are ready.")
    return mycursor
connect_database()
# Function to clear the input fields
# Function to clear the input fields
def clear(id_entry, category_name_entry, description_text):
    id_entry.delete(0, END)
    category_name_entry.delete(0, END)
    description_text.delete(1.0, END)


# Function to load data into the Treeview
def treeview_data(treeview):
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="inventory_system")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM category_data")
    records = mycursor.fetchall()

    # Clear the existing data in the Treeview
    treeview.delete(*treeview.get_children())

    # Insert new data into the Treeview
    for record in records:
        treeview.insert('', END, values=record)

# Function to delete a category
def delete_category(treeview):
    selected = treeview.selection()
    if not selected:
        messagebox.showerror('Error', 'No row is selected')
        return

    selected_item = treeview.item(selected)
    category_id = selected_item['values'][0]  # Get the ID from the first column

    # Confirmation dialog
    result = messagebox.askyesno('Confirm', 'Do you really want to delete the record?')
    if result:
        try:
            mydb = mysql.connector.connect(host="localhost", user="root", password="", database="inventory_system")
            mycursor = mydb.cursor()
            mycursor.execute('DELETE FROM category_data WHERE id = %s', (category_id,))
            mydb.commit()

            # Refresh Treeview data
            treeview_data(treeview)
            messagebox.showinfo('Success', 'Data deleted successfully')
        except Exception as e:
            messagebox.showerror('Error', f'Error occurred: {str(e)}')

# Function to display selected data in the input fields
def select_data(event, id_entry, category_name_entry, description_text, treeview):
    selected = treeview.selection()
    if not selected:
        return

    content = treeview.item(selected)
    actual_content = content['values']

    # Fill the form with selected data
    id_entry.delete(0, END)
    category_name_entry.delete(0, END)
    description_text.delete(1.0, END)

    id_entry.insert(0, actual_content[0])  # ID
    category_name_entry.insert(0, actual_content[1])  # Category Name
    description_text.insert(1.0, actual_content[2])  # Description

# Function to add a new category
# Function to add a new category with validation
# Function to add a new category with validation and clear fields after adding
def add_category(id, name, description, treeview, id_entry, category_name_entry, description_text):
    if id.strip() == '' or name.strip()=='' or description.strip=='':
        messagebox.showerror('Error', 'All  Fields are required')
    elif id.strip() == '':
        messagebox.showerror('Error', 'Id is required')
    elif name.strip() == '':
        messagebox.showerror('Error', 'Category Name is required')
    elif description.strip() == '':
        messagebox.showerror('Error', 'Description is required')
    else:
        try:
            # Convert the id to an integer
            id_value = int(id.strip())  # Ensure the id is an integer

            # Check if the id is already in use
            mydb = mysql.connector.connect(host="localhost", user="root", password="", database="inventory_system")
            mycursor = mydb.cursor()
            mycursor.execute('SELECT * FROM category_data WHERE id = %s', (id_value,))
            existing_id = mycursor.fetchone()

            if existing_id:
                messagebox.showerror('Error', 'Id already exists! Please enter a unique id.')
                return

            # Insert the new category
            query = "INSERT INTO category_data (id, name, description) VALUES (%s, %s, %s)"
            values = (id_value, name.strip(), description.strip())
            mycursor.execute(query, values)
            mydb.commit()

            # Refresh Treeview data
            treeview_data(treeview)
            messagebox.showinfo('Success', 'Category added successfully')

            # Clear the input fields after adding the category
            clear(id_entry, category_name_entry, description_text)

        except ValueError:
            messagebox.showerror('Error', 'Id must be a valid integer')
        except Exception as e:
            messagebox.showerror('Error', f'Error occurred: {str(e)}')




# Function to display the category form
def category_form(window):
    global back_image, logo

    # Frame for category management
    category_frame = Frame(window, width=1070, height=567, bg='white')
    category_frame.place(x=200, y=100)

    heading_Label = Label(category_frame, text='Manage Categories Details', font=('times new roman', 16, 'bold'), bg='#0f4d7d', fg='white')
    heading_Label.place(x=0, y=0, relwidth=1)

    back_image = PhotoImage(file='arrow.png')
    back_button = Button(category_frame, image=back_image, bd=0, cursor='hand2', bg='white', command=lambda: category_frame.place_forget())
    back_button.place(x=10, y=30)

    logo = PhotoImage(file='cat4.png')
    label = Label(category_frame, image=logo, bg="white")
    label.place(x=30, y=100)

    details_frame = Frame(category_frame, bg="white")
    details_frame.place(x=500, y=60)

    id_label = Label(details_frame, text='Id:', font=('times new roman', 14, 'bold'), bg='white')
    id_label.grid(row=0, column=0, padx=20, sticky="w")
    id_entry = Entry(details_frame, font=('times new roman', 14, 'bold'), bg='lightyellow')
    id_entry.grid(row=0, column=1)

    category_name_label = Label(details_frame, text='Category Name:', font=('times new roman', 14, 'bold'), bg='white')
    category_name_label.grid(row=1, column=0, padx=20, sticky="w")
    category_name_entry = Entry(details_frame, font=('times new roman', 14, 'bold'), bg='lightyellow')
    category_name_entry.grid(row=1, column=1, pady=20)

    description_label = Label(details_frame, text='Description:', font=('times new roman', 14, 'bold'), bg='white')
    description_label.grid(row=2, column=0, padx=20, sticky="nw")
    description_text = Text(details_frame, width=25, height=6, bg='lightyellow')
    description_text.grid(row=2, column=1)

    button_frame = Frame(category_frame, bg='white')
    button_frame.place(x=580, y=280)

    add_button = Button(button_frame, text='Add', font=('times new roman', 14), width=8, cursor='hand2', fg='white', bg='#0f4d7d',
                    command=lambda: add_category(id_entry.get(),category_name_entry.get(), description_text.get(1.0, END), treeview, id_entry, category_name_entry, description_text))
    add_button.grid(row=0, column=0, padx=20)


    delete_button = Button(button_frame, text='Delete', font=('times new roman', 14), width=8, cursor='hand2', fg='white', bg='#0f4d7d',
                           command=lambda: delete_category(treeview))
    delete_button.grid(row=0, column=1, padx=20)

    clear_button = Button(button_frame, text='Clear', font=('times new roman', 14), width=8, cursor='hand2', fg='white', bg='#0f4d7d',
                          command=lambda: clear(id_entry, category_name_entry, description_text))
    clear_button.grid(row=0, column=2, padx=20)

    treeview_frame = Frame(category_frame, bg='white')
    treeview_frame.place(x=530, y=340, height=200, width=500)

    scrolly = Scrollbar(treeview_frame, orient=VERTICAL)
    scrollx = Scrollbar(treeview_frame, orient=HORIZONTAL)
    treeview = ttk.Treeview(treeview_frame, column=('id', 'name', 'description'), show='headings',
                            yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
    scrolly.pack(side=RIGHT, fill=Y)
    scrollx.pack(side=BOTTOM, fill=X)
    scrollx.config(command=treeview.xview)
    scrolly.config(command=treeview.yview)
    treeview.pack(fill=BOTH, expand=1)

    treeview.heading('id', text='Id')
    treeview.heading('name', text='Category Name')
    treeview.heading('description', text='Description')

    treeview.column('id', width=80)
    treeview.column('name', width=160)
    treeview.column('description', width=300)

    treeview_data(treeview)
    treeview.bind('<ButtonRelease-1>', lambda event: select_data(event, id_entry, category_name_entry, description_text, treeview))

