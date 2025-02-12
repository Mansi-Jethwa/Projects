from tkinter import *
from PIL import ImageTk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
import mysql.connector
from datetime import date

def validate_update_input(category, supplier, name, price, quantity, status):
    """Validates the input fields for product updates."""
    if name.strip()=='' or quantity.strip()=='' or price.strip()=='':
        messagebox.showerror('Error',"All Fields are required")
    elif category == 'Select':
        messagebox.showerror('Error', 'Please select a Category.')
        return False
    elif supplier == 'Select':
        messagebox.showerror('Error', 'Please select a Supplier.')
        return False
    elif not name:
        messagebox.showerror('Error', 'Please enter a Product Name.')
        return False
    try:
        float(price)
    except ValueError:
        messagebox.showerror('Error', 'Price must be a number.')
        return False
    try:
        int(quantity)
        if int(quantity) < 0:
            messagebox.showerror('Error', 'Quantity must be a positive integer.')
            return False
    except ValueError:
        messagebox.showerror('Error', 'Quantity must be an integer.')
        return False
    if status == 'Select':
        messagebox.showerror('Error', 'Please select a Status.')
        return False
    return True

def validate_input(category, supplier, name, price, quantity, status):
    """Validates the input fields."""
    if category == 'Select':
        messagebox.showerror('Error', 'Please select a Category.')
        return False
    if supplier == 'Select':
        messagebox.showerror('Error', 'Please select a Supplier.')
        return False
    if not name:
        messagebox.showerror('Error', 'Please enter a Product Name.')
        return False
    try:
        float(price)
    except ValueError:
        messagebox.showerror('Error', 'Price must be a number.')
        return False
    try:
        int(quantity)
        if int(quantity) < 0:
            messagebox.showerror('Error', 'Quantity must be a positive integer.')
            return False
    except ValueError:
        messagebox.showerror('Error', 'Quantity must be an integer.')
        return False
    if status == 'Select':
        messagebox.showerror('Error', 'Please select a Status.')
        return False
    return True

# Add the following functions outside the `product_form` function:
def treeview_data(treeview):
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="inventory_system")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM product_data")
    records = mycursor.fetchall()

    # Clear the existing data in the Treeview
    treeview.delete(*treeview.get_children())

    # Insert new data into the Treeview
    for record in records:
        treeview.insert('', END, values=record)

def search_product(treeview, search_by, search_value):
    if search_by == 'Search By' or not search_value.strip():
        messagebox.showerror('Error', 'Please select a valid search criterion and enter a value!')
        return

    try:
        mydb = mysql.connector.connect(host="localhost", user="root", password="", database="inventory_system")
        mycursor = mydb.cursor()

        # Construct query based on selected search criterion
        column_mapping = {
            'Category': 'category',
            'Supplier': 'supplier',
            'Name': 'name',
            'Status': 'status'
        }
        column_name = column_mapping[search_by]
        query = f"SELECT * FROM product_data WHERE {column_name} LIKE %s"
        mycursor.execute(query, ('%' + search_value + '%',))
        rows = mycursor.fetchall()

        # Clear the treeview and insert search results
        treeview.delete(*treeview.get_children())
        for row in rows:
            treeview.insert('', END, values=row)

    except Exception as e:
        messagebox.showerror('Error', f"Error due to: {str(e)}")


def show_all_products(treeview):
    try:
        mydb = mysql.connector.connect(host="localhost", user="root", password="", database="inventory_system")
        mycursor = mydb.cursor()

        # Query to fetch all products
        mycursor.execute("SELECT * FROM product_data")
        rows = mycursor.fetchall()

        # Clear the treeview and display all products
        treeview.delete(*treeview.get_children())
        for row in rows:
            treeview.insert('', END, values=row)

    except Exception as e:
        messagebox.showerror('Error', f"Error due to: {str(e)}")

def fetch_supplier_category(category_combobox,supplier_combobox):
    category_option=[]
    supplier_option=[]
    mydb=mysql.connector.connect(host="localhost",user="root",password="")
    mycursor=mydb.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS inventory_system")
    print("Database is created")
    mycursor.execute("USE inventory_system")
    mycursor.execute("SELECT name from category_data")
    names=mycursor.fetchall()
    for name in names:
        category_option.append(name[0])
    category_combobox.config(values=category_option)

    mycursor.execute("SELECT name from supplier_data")
    names=mycursor.fetchall()
    for name in names:
        supplier_option.append(name[0])
    supplier_combobox.config(values=supplier_option)

def connect_database():
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="inventory_system")
    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE IF NOT EXISTS product_data (id INT AUTO_INCREMENT PRIMARY KEY,category VARCHAR(100),supplier VARCHAR(100),name VARCHAR(100),price DECIMAL(10, 2),quantity INT,status VARCHAR(50))")
    mydb.commit()
    print("product_data table is ready")
connect_database()

def add_product(category, supplier, name, price, quantity, status, treeview,category_combobox, supplier_combobox, name_entry, price_entry, quantity_entry, status_combobox):
    if validate_input(category, supplier, name, price, quantity, status):
# Your existing code for adding a product
        try:
            mydb = mysql.connector.connect(host="localhost", user="root", password="", database="inventory_system")
            mycursor = mydb.cursor()
            query = "INSERT INTO product_data (category, supplier, name, price, quantity, status) VALUES (%s, %s, %s, %s, %s, %s)"
            mycursor.execute(query, (category, supplier, name, float(price), int(quantity), status))
            mydb.commit()
        
        # Call to refresh the Treeview
            treeview_data(treeview)
            messagebox.showinfo('Success', 'Product added successfully!')
            clear_form(category_combobox, supplier_combobox, name_entry, price_entry, quantity_entry, status_combobox)
        except Exception as e:
            messagebox.showerror('Error', f"Error due to: {str(e)}")

def update_product(category, supplier, name, price, quantity, status, treeview,category_combobox, supplier_combobox, name_entry, price_entry, quantity_entry, status_combobox):
    # Get the selected item's ID from the Treeview
    selected_item = treeview.selection()
    if not selected_item:
        messagebox.showerror('Error', 'Please select a product to update!')
        return

    if validate_update_input(category, supplier, name, price, quantity, status):
        product_id = treeview.item(selected_item[0], 'values')[0]  # Assuming the 'id' is in the first column

        try:
            mydb = mysql.connector.connect(host="localhost", user="root", password="", database="inventory_system")
            mycursor = mydb.cursor()
            query = "UPDATE product_data SET category = %s, supplier = %s, name = %s, price = %s, quantity = %s, status = %s WHERE id = %s"
            mycursor.execute(query, (category, supplier, name, float(price), int(quantity), status, product_id))
            mydb.commit()

            # Call to refresh the Treeview
            treeview_data(treeview)
            messagebox.showinfo('Success', 'Product updated successfully!')
            clear_form(category_combobox, supplier_combobox, name_entry, price_entry, quantity_entry, status_combobox)
        except Exception as e:
            messagebox.showerror('Error', f"Error due to: {str(e)}")


def delete_product(treeview,category_combobox, supplier_combobox, name_entry, price_entry, quantity_entry, status_combobox):
    # Get the selected item's ID from the Treeview
    selected_item = treeview.selection()
    if not selected_item:
        messagebox.showerror('Error', 'Please select a product to delete!')
        return
    product_id = treeview.item(selected_item[0], 'values')[0]  # Assuming the 'id' is in the first column

    try:
        mydb = mysql.connector.connect(host="localhost", user="root", password="", database="inventory_system")
        mycursor = mydb.cursor()
        query = "DELETE FROM product_data WHERE id = %s"
        mycursor.execute(query, (product_id,))
        mydb.commit()

        # Call to refresh the Treeview
        treeview_data(treeview)
        messagebox.showinfo('Success', 'Product deleted successfully!')
        clear_form(category_combobox, supplier_combobox, name_entry, price_entry, quantity_entry, status_combobox)
    except Exception as e:
        messagebox.showerror('Error', f"Error due to: {str(e)}")
def clear_form(category_combobox, supplier_combobox, name_entry, price_entry, quantity_entry, status_combobox):
    # Reset combo boxes to their default values
    category_combobox.set('Select')
    supplier_combobox.set('Select')
    status_combobox.set('Select')
    
    # Clear text entries
    name_entry.delete(0, END)
    price_entry.delete(0, END)
    quantity_entry.delete(0, END)

def select_item(treeview, category_combobox, supplier_combobox, name_entry, price_entry, quantity_entry, status_combobox):
    selected_item = treeview.selection()
    
    if not selected_item:
        messagebox.showerror('Error', 'Please select a product from the table!')
        return

    # Get the values of the selected row
    product_id, category, supplier, name, price, quantity, status = treeview.item(selected_item, 'values')
    
    # Populate the form fields with the selected item's values
    category_combobox.set(category)
    supplier_combobox.set(supplier)
    name_entry.delete(0, END)
    name_entry.insert(0, name)
    price_entry.delete(0, END)
    price_entry.insert(0, price)
    quantity_entry.delete(0, END)
    quantity_entry.insert(0, quantity)
    status_combobox.set(status)

def product_form(window):
    global back_image
    product_frame=Frame(window,width=1070,height=567,bg='white')
    product_frame.place(x=200,y=100)

    back_image = PhotoImage(file='arrow.png')
    back_button = Button(product_frame, image=back_image, bd=0, cursor='hand2', bg='white', command=lambda: product_frame.place_forget())
    back_button.place(x=10, y=10)

    left_frame=Frame(product_frame,bg='white',bd=2,relief=RIDGE)
    left_frame.place(x=20,y=40)

    heading_Label = Label(left_frame, text='Manage Products Details', font=('times new roman', 16, 'bold'), bg='#0f4d7d', fg='white')
    heading_Label.grid(row=0,columnspan=2,sticky="we")

    category_label = Label(left_frame, text='Category:', font=('times new roman', 14, 'bold'), bg='white')
    category_label.grid(row=1, column=0, padx=20, sticky="w")
    category_combobox=ttk.Combobox(left_frame,font=('times new roman', 14),width=20,state='readonly')
    category_combobox.grid(row=1,column=1,pady=30)
    category_combobox.set('Select')

    supplier_label = Label(left_frame, text='Supplier:', font=('times new roman', 14, 'bold'), bg='white')
    supplier_label.grid(row=2, column=0, padx=20, sticky="w")
    supplier_combobox=ttk.Combobox(left_frame,font=('times new roman', 14),width=20,state='readonly')
    supplier_combobox.grid(row=2,column=1)
    supplier_combobox.set('Select')

    name_label = Label(left_frame, text='Product Name:', font=('times new roman', 14, 'bold'), bg='white')
    name_label.grid(row=3, column=0, padx=20, sticky="w")
    name_entry = Entry(left_frame, font=('times new roman', 14, 'bold'), bg='white')
    name_entry.grid(row=3, column=1,pady=30)

    price_label = Label(left_frame, text='Price:', font=('times new roman', 14, 'bold'), bg='white')
    price_label.grid(row=4, column=0, padx=20, sticky="w")
    price_entry = Entry(left_frame, font=('times new roman', 14, 'bold'), bg='white')
    price_entry.grid(row=4, column=1)

    quantity_label = Label(left_frame, text='Quantity:', font=('times new roman', 14, 'bold'), bg='white')
    quantity_label.grid(row=5, column=0, padx=20, sticky="w")
    quantity_entry = Entry(left_frame, font=('times new roman', 14, 'bold'), bg='white')
    quantity_entry.grid(row=5, column=1,pady=30)

    status_label = Label(left_frame, text='Status:', font=('times new roman', 14, 'bold'), bg='white')
    status_label.grid(row=6, column=0, padx=20, sticky="w")
    status_combobox=ttk.Combobox(left_frame,values=('Active','Inactive'),font=('times new roman', 14),width=20,state='readonly')
    status_combobox.grid(row=6,column=1)
    status_combobox.set('Select')

    button_frame=Frame(left_frame,bg="white")
    button_frame.grid(row=7,columnspan=2,padx=20)

    add_button = Button(button_frame,text='Add',font=('times new roman', 14),width=8,cursor='hand2',fg='white',bg='#0f4d7d',command=lambda: add_product(category_combobox.get(),supplier_combobox.get(),name_entry.get(),price_entry.get(),quantity_entry.get(),status_combobox.get(),treeview,category_combobox, supplier_combobox, name_entry, price_entry, quantity_entry, status_combobox))
    add_button.grid(row=0, column=0, padx=5)

    update_button = Button(button_frame, text='Update', font=('times new roman', 14), width=8, cursor='hand2', fg='white', bg='#0f4d7d',command=lambda: update_product(category_combobox.get(), supplier_combobox.get(), name_entry.get(),
                                                       price_entry.get(), quantity_entry.get(), status_combobox.get(), treeview,category_combobox, supplier_combobox, name_entry, price_entry, quantity_entry, status_combobox))
    update_button.grid(row=0, column=1, padx=5)

    delete_button = Button(button_frame, text='Delete', font=('times new roman', 14), width=8, cursor='hand2', fg='white', bg='#0f4d7d',
                       command=lambda: delete_product(treeview,category_combobox, supplier_combobox, name_entry, price_entry, quantity_entry, status_combobox))
    delete_button.grid(row=0, column=2, padx=5, pady=20)

    clear_button = Button(button_frame, text='Clear', font=('times new roman', 14), width=8, cursor='hand2', fg='white', bg='#0f4d7d',
                      command=lambda: clear_form(category_combobox, supplier_combobox, name_entry, price_entry, quantity_entry, status_combobox))
    clear_button.grid(row=0, column=3, padx=5, pady=20)


    search_frame=LabelFrame(product_frame,text='Search Product',font=('times new roman',14,'bold'), bg='white')
    search_frame.place(x=480,y=30)

    search_combobox=ttk.Combobox(search_frame,values=('Category','Supplier','Name','Status'),state='readonly',width=16,font=('times new roman',14,'bold'))
    search_combobox.grid(row=0,column=0,padx=10)
    search_combobox.set('Search By')

    search_entry = Entry(search_frame, font=('times new roman', 14, 'bold'), bg='white',width=16)
    search_entry.grid(row=0, column=1)

    search_button = Button(search_frame, text='Search', font=('times new roman', 14), width=8, cursor='hand2', fg='white', bg='#0f4d7d',
                       command=lambda: search_product(treeview, search_combobox.get(), search_entry.get()))
    search_button.grid(row=0, column=2, padx=(10, 0), pady=10)

    show_button = Button(search_frame, text='Show all', font=('times new roman', 14), width=8, cursor='hand2', fg='white', bg='#0f4d7d',
                     command=lambda: show_all_products(treeview))
    show_button.grid(row=0, column=3, padx=10)

    treeview_frame=Frame(product_frame)
    treeview_frame.place(x=480,y=125,width=570,height=410)

    scrolly = Scrollbar(treeview_frame, orient=VERTICAL)
    scrollx = Scrollbar(treeview_frame, orient=HORIZONTAL)
    treeview = ttk.Treeview(treeview_frame, column=('id','category', 'supplier', 'name','price','quantity','status'), show='headings',
                            yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
    scrolly.pack(side=RIGHT, fill=Y)
    scrollx.pack(side=BOTTOM, fill=X)
    scrollx.config(command=treeview.xview)
    scrolly.config(command=treeview.yview)
    treeview.pack(fill=BOTH, expand=1)

    treeview.heading('id', text='Id')
    treeview.heading('category', text='Category')
    treeview.heading('supplier', text='Supplier')
    treeview.heading('name', text='Name')
    treeview.heading('price', text='Price')
    treeview.heading('quantity', text='Quantity')
    treeview.heading('status', text='Status')

    treeview.column('id', width=80)
    treeview.column('category', width=160)
    treeview.column('supplier', width=160)
    treeview.column('name', width=160)
    treeview.column('price', width=160)
    treeview.column('quantity', width=160)
    treeview.column('status', width=160)
    treeview.bind(
        "<ButtonRelease-1>",
        lambda event: select_item(
            treeview, category_combobox, supplier_combobox,
            name_entry, price_entry, quantity_entry, status_combobox
        )
    )

    # Fetch initial data for the Treeview
    fetch_supplier_category(category_combobox, supplier_combobox)
    treeview_data(treeview)
