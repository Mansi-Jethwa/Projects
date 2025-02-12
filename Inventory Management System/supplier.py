from tkinter import *
from PIL import ImageTk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
import mysql.connector
from datetime import date

def validate_inputs(invoice, name, contact, description):
    """
    Validates the inputs for the supplier form.
    """
    if not invoice.isnumeric():
        messagebox.showerror("Error", "Invoice must be a numeric value.")
        return False
    if not name.strip():
        messagebox.showerror("Error", "Supplier name is required.")
        return False
    if not all(x.isalpha() or x.isspace() for x in name):
        messagebox.showerror("Error", "Supplier name must contain only alphabetic characters and spaces.")
        return False
    if not contact.strip():
        messagebox.showerror("Error", "Supplier contact is required.")
        return False
    if not contact.isdigit() or len(contact) != 10:
        messagebox.showerror("Error", "Supplier contact must be a 10-digit number.")
        return False
    if not description.strip():
        messagebox.showerror("Error", "Description is required.")
        return False
    return True
def delete_supplier(treeview, invoice_entry, name_entry, contact_entry, description_text):
    """
    Deletes a supplier record from the database.
    """
    selected = treeview.selection()  # Get selected row
    if not selected:
        messagebox.showerror('Error', 'No row is selected')
        return

    # Retrieve the 'invoice' value from the selected row
    selected_item = treeview.item(selected)
    invoice = selected_item['values'][0]  # Assuming 'invoice' is the first column

    # Confirmation dialog
    result = messagebox.askyesno('Confirm', 'Do you really want to delete the record?')
    if result:
        try:
            mydb = mysql.connector.connect(host="localhost", user="root", password="", database="inventory_system")
            mycursor = mydb.cursor()
            mycursor.execute('DELETE FROM supplier_data WHERE invoice = %s', (invoice,))
            mydb.commit()

            # Refresh Treeview data
            treeview_data(treeview)
            messagebox.showinfo('Success', 'Data is deleted successfully')
            # Clear fields after deleting supplier
            clear(invoice_entry, name_entry, contact_entry, description_text)
        except Exception as e:
            messagebox.showerror('Error', f'Error occurred: {str(e)}')

def clear(invoice_entry, name_entry, contact_entry, description_text):
    """
    Clears all the input fields in the form.
    """
    invoice_entry.delete(0, END)
    name_entry.delete(0, END)
    contact_entry.delete(0, END)
    description_text.delete(1.0, END)

def show_all(treeview, search_entry):
    # Clear the search field
    search_entry.delete(0, END)
    # Call the treeview_data function to reload all supplier data
    treeview_data(treeview)

def search_supplier(invoice_entry, treeview):
    """
    Searches for a supplier based on the invoice number.
    """
    invoice = invoice_entry.get().strip()
    if not validate_inputs(invoice, "dummy", "0000000000", "dummy"):  # Only validate the invoice field
        return

    try:
        mydb = mysql.connector.connect(host="localhost", user="root", password="", database="inventory_system")
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM supplier_data WHERE invoice = %s", (invoice,))
        record = mycursor.fetchone()

        if record:
            treeview.delete(*treeview.get_children())
            treeview.insert('', END, values=record)
            messagebox.showinfo("Success", "Supplier found.")
        else:
            messagebox.showerror("Error", "No supplier found with the given Invoice number.")
    except Exception as e:
        messagebox.showerror("Error", f"Error occurred: {str(e)}")

def update_supplier(invoice, name, contact, description, treeview, invoice_entry, name_entry, contact_entry, description_text):
    """
    Updates an existing supplier record after validating inputs.
    """
    if validate_inputs(invoice, name, contact, description):  # Validate the inputs
        try:
            # Establish a connection to the database
            mydb = mysql.connector.connect(host="localhost", user="root", password="", database="inventory_system")
            mycursor = mydb.cursor()

            # Check if the supplier with the given invoice exists
            mycursor.execute("SELECT * FROM supplier_data WHERE invoice = %s", (invoice,))
            existing_supplier = mycursor.fetchone()

            if existing_supplier:
                # If supplier exists, perform the update
                mycursor.execute(
                    "UPDATE supplier_data SET name=%s, contact=%s, description=%s WHERE invoice=%s",
                    (name, contact, description, invoice)
                )
                mydb.commit()

                # Check if any row was updated
                if mycursor.rowcount > 0:
                    treeview_data(treeview)  # Refresh the Treeview data
                    messagebox.showinfo("Success", "Supplier updated successfully.")
                    # Clear fields after updating supplier
                    clear(invoice_entry, name_entry, contact_entry, description_text)
                else:
                    messagebox.showwarning("Warning", "No changes made.")
            else:
                messagebox.showerror("Error", "No supplier found with the given invoice number.")

        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Database error: {str(err)}")
        except Exception as e:
            messagebox.showerror("Error", f"Error occurred: {str(e)}")


def select_data(event,invoice_entry,name_entry,contact_entry,description_text,treeview):
    index=treeview.selection()
    content=treeview.item(index)
    actual_content=content['values']
    print(actual_content)
    invoice_entry.delete(0,END)
    name_entry.delete(0,END)
    contact_entry.delete(0,END)
    description_text.delete(1.0,END)
    invoice_entry.insert(0,actual_content[0])
    name_entry.insert(0,actual_content[1])
    contact_entry.insert(0,actual_content[2])
    description_text.insert(1.0,actual_content[3])


def connect_database():
    mydb=mysql.connector.connect(host="localhost",user="root",password="")
    mycursor=mydb.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS inventory_system")
    print("Database is created")
    mycursor.execute("USE inventory_system")
    mycursor.execute("CREATE TABLE IF NOT EXISTS supplier_data (invoice INT PRIMARY KEY, name VARCHAR(100), contact VARCHAR(30), description TEXT)")
    print("Employee Table is Created")
    return mycursor
connect_database()

def treeview_data(treeview):
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="inventory_system")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM supplier_data")
    records = mycursor.fetchall()

    # Clear the existing data in the Treeview
    treeview.delete(*treeview.get_children())

    # Insert new data into the Treeview
    for record in records:
        treeview.insert('', END, values=record)

def add_supplier(invoice, name, contact, description, treeview, invoice_entry,name_entry, contact_entry, description_text):
    """
    Adds a new supplier to the database after validating inputs.
    """
    if validate_inputs(invoice, name, contact, description):  # Validate the inputs
        try:
            mydb = mysql.connector.connect(host="localhost", user="root", password="", database="inventory_system")
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM supplier_data WHERE invoice = %s", (invoice,))
            existing_supplier = mycursor.fetchone()

            if existing_supplier:
                messagebox.showerror("Error", "Invoice number already exists. Please use a unique invoice number.")
                return

            # Insert query to add the supplier
            query = "INSERT INTO supplier_data (invoice, name, contact, description) VALUES (%s, %s, %s, %s)"
            values = (invoice, name, contact, description.strip())
            mycursor.execute(query, values)
            mydb.commit()

            # Refresh Treeview with updated data
            treeview_data(treeview)

            messagebox.showinfo("Success", "Supplier added successfully.")

            # Clear the input fields after adding the supplier
            clear(invoice_entry,name_entry, contact_entry, description_text)

        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Database error: {str(err)}")
        except Exception as e:
            messagebox.showerror("Error", f"Error occurred: {str(e)}")


def supplier_form(window):
    global back_image
    supplier_frame=Frame(window,width=1070,height=567,bg='white')
    supplier_frame.place(x=200,y=100)

    heading_Label=Label(supplier_frame,text='Manage Supplier Details',font=('times new roman',16,'bold'),bg='#0f4d7d',fg='white')
    heading_Label.place(x=0,y=0,relwidth=1)

    back_image=PhotoImage(file='arrow.png')
    back_button = Button(supplier_frame, image=back_image, bd=0, cursor='hand2',bg='white', command=lambda: supplier_frame.place_forget())
    back_button.place(x=10,y=30)

    left_frame=Frame(supplier_frame,bg='white')
    left_frame.place(x=10,y=100)

    invoice_label=Label(left_frame,text='Invoice No:',font=('times new roman',14,'bold'),bg='white')
    invoice_label.grid(row=0,column=0,padx=20,sticky="w")
    invoice_entry=Entry(left_frame,font=('times new roman',14,'bold'),bg='lightyellow')
    invoice_entry.grid(row=0,column=1)

    name_label=Label(left_frame,text='Supplier Name:',font=('times new roman',14,'bold'),bg='white')
    name_label.grid(row=1,column=0,padx=20,pady=20,sticky="w")
    name_entry=Entry(left_frame,font=('times new roman',14,'bold'),bg='lightyellow')
    name_entry.grid(row=1,column=1)

    contact_label=Label(left_frame,text='Supplier Contact:',font=('times new roman',14,'bold'),bg='white')
    contact_label.grid(row=2,column=0,padx=20,sticky="w")
    contact_entry=Entry(left_frame,font=('times new roman',14,'bold'),bg='lightyellow')
    contact_entry.grid(row=2,column=1)

    description_label=Label(left_frame,text='Description:',font=('times new roman',14,'bold'),bg='white')
    description_label.grid(row=3,column=0,padx=20,sticky="nw",pady=25)
    description_text=Text(left_frame,width=25,height=6,bg='lightyellow')
    description_text.grid(row=3,column=1,pady=20)

    buttonFrame=Frame(left_frame,bg='white')
    buttonFrame.grid(row=4,columnspan=2,pady=20)

    # Assuming you have a frame or container for buttons
    add_button = Button(buttonFrame, text='Add', font=('times new roman', 14), width=8, cursor='hand2', fg='white', bg='#0f4d7d', 
                    command=lambda: add_supplier(invoice_entry.get(), name_entry.get(), contact_entry.get(), description_text.get(1.0, END).strip(), treeview,invoice_entry, name_entry, contact_entry, description_text))
    add_button.grid(row=0, column=0, padx=20)


    # Create the Update button and bind it to the update_supplier function
    update_button = Button(buttonFrame, text='Update', font=('times new roman', 14), width=8, cursor='hand2', fg='white', bg='#0f4d7d',
                       command=lambda: update_supplier(
                           invoice_entry.get(),
                           name_entry.get(),
                           contact_entry.get(),
                           description_text.get("1.0", "end-1c"),
                           treeview,
                           invoice_entry,
                           name_entry,
                           contact_entry,
                           description_text
                       ))

    update_button.grid(row=0, column=1)


    delete_button = Button(buttonFrame, text='Delete', font=('times new roman', 14), width=8, cursor='hand2', fg='white', bg='#0f4d7d', 
                       command=lambda: delete_supplier(treeview,invoice_entry, name_entry, contact_entry, description_text))
    delete_button.grid(row=0, column=2, padx=20)


    cancel_button = Button(buttonFrame, text='Clear', font=('times new roman', 14), width=8, cursor='hand2', fg='white', bg='#0f4d7d',
                       command=lambda: clear(invoice_entry, name_entry, contact_entry, description_text))
    cancel_button.grid(row=0, column=3)

    right_frame=Frame(supplier_frame,bg='white')
    right_frame.place(x=520,y=80,width=500,height=350)
    
    search_frame=Frame(right_frame,bg='white')
    search_frame.pack(pady=10)

    num_label=Label(search_frame,text='Invoice No:',font=('times new roman',14,'bold'),bg='white')
    num_label.grid(row=0,column=0,padx=15,sticky="w")
    search_entry=Entry(search_frame,font=('times new roman',14,'bold'),bg='lightyellow',width=10)
    search_entry.grid(row=0,column=1)

    search_button = Button(search_frame, text='Search', font=('times new roman', 14), width=8, cursor='hand2', fg='white', bg='#0f4d7d',
                       command=lambda: search_supplier(search_entry, treeview))
    search_button.grid(row=0, column=2, padx=15)

    show_button=Button(search_frame,text='Show all',font=('times new roman',14) ,width=8,cursor='hand2',fg='white',bg='#0f4d7d',command=lambda: show_all(treeview,search_entry))
    show_button.grid(row=0,column=3)

    scrolly=Scrollbar(right_frame,orient=VERTICAL)
    scrollx=Scrollbar(right_frame,orient=HORIZONTAL)
    treeview=ttk.Treeview(right_frame,column=('invoice','name','contact','description'),show='headings',yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
    scrolly.pack(side=RIGHT,fill=Y)
    scrollx.pack(side=BOTTOM,fill=X)
    scrollx.config(command=treeview.xview)
    scrolly.config(command=treeview.yview)
    treeview.pack(fill=BOTH,expand=1)
    treeview.heading('invoice',text='Invoice Id')
    treeview.heading('name',text='Supplier Name')
    treeview.heading('contact',text='Supplier Contact')
    treeview.heading('description',text='Description')

    treeview.column('invoice',width=80)
    treeview.column('name',width=160)
    treeview.column('contact',width=120)
    treeview.column('description',width=300)

    treeview_data(treeview)
    treeview.bind('<ButtonRelease-1>',lambda event:select_data(event,invoice_entry,name_entry,contact_entry,description_text,treeview))
