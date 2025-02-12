import tkinter as tk
from tkinter import *
from PIL import ImageTk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
import mysql.connector
from datetime import date
import datetime
from datetime import datetime
import os
from tkinter import filedialog

import os
#GUI Part
# Create a Tkinter window
window = Tk()
window.title("Dashboard")
window.geometry("1270x668+0+0")
window.resizable(0, 0)
window.config(bg='white')
def redirect_to_login():
    window.destroy()  # Close the current window
    os.system('python logine.py') 
# Load background image
bg_image = PhotoImage(file='inventory.png')

# Title label with image and text
titleLabel = Label(window, image=bg_image, compound=LEFT,text="Inventory Management System",
                   font=("times new roman", 40, "bold"), bg="#010c48", fg="white",anchor="w",padx=20)
titleLabel.place(x=0, y=0,relwidth=1)
cart_list=[]

logoutButton = Button(window, text="Logout", font=('times new roman', 20, 'bold'), fg='#010c48', command=redirect_to_login,cursor="hand2")
logoutButton.place(x=1100, y=10)

subtitleLabel=Label(window,text="Welcome Admin\t\t Date:15-11-2024\t\t Time:9:00:00pm",font=('times new roman',15),bg='#4d636d',fg='white')
subtitleLabel.place(x=0,y=70,relwidth=1)


varsearch=StringVar()
product_frame=Frame(window,bd=4,relief=RIDGE,bg="white")
product_frame.place(x=5,y=110,width=390,height=540)
pTitle=Label(product_frame,text="All Products",font=('times new roman',20,'bold'),bg="#262626",fg="white").pack(side=TOP,fill=X)

product_frame2=Frame(product_frame,relief=RIDGE,bg="white")
product_frame2.place(x=1,y=38,width=380,height=90)

lblsearch=Label(product_frame2,text="Search Product | By Name ",font=('times new roman',15,'bold'),bg="white",fg="green").place(x=2,y=5)

lblname=Label(product_frame2,text="Product Name ",font=('times new roman',15,'bold'),bg="white").place(x=5,y=45)
txtsearch=Entry(product_frame2,textvariable=varsearch,font=('times new roman',15),bg="white").place(x=130,y=47,width=140,height=22)
# ... other code

# Create the button
btnsearch = Button(product_frame2, text="Search", font=('times new roman', 15), bg="#219653", fg="white", cursor="hand2")

# Place the button
btnsearch.place(x=274, y=45, width=100, height=25)

# Configure the command (this is the crucial change)
btnsearch.config(command=lambda:search_products)

# ... rest of your code
# ... other code

# Create the button
btnshowall = Button(product_frame2, text="Show all", font=('times new roman', 15), bg="#219653", fg="white", cursor="hand2")

# Place the button
btnshowall.place(x=274, y=10, width=100, height=25)

# **Directly assign function**
btnshowall.config(command=lambda: show_all_products())
# ... rest of your code
product_frame3=Frame(product_frame,relief=RIDGE)
product_frame3.place(x=2,y=140,width=380,height=390)

scrolly=Scrollbar(product_frame3,orient=VERTICAL)
scrollx=Scrollbar(product_frame3,orient=HORIZONTAL)

product_table=ttk.Treeview(product_frame3,columns=("pid","name","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
scrollx.pack(side=BOTTOM,fill=X)
scrolly.pack(side=RIGHT,fill=Y)
scrollx.config(command=product_table.xview)
scrolly.config(command=product_table.yview)
def get_data(ev):
    selected_row = product_table.focus()
    if selected_row:  # Check if a row is actually selected
        content = product_table.item(selected_row)
        row = content['values']
        var_pid.set(row[0])
        var_pname.set(row[1])
        var_price.set(row[2])
        # Check if quantity information exists (at least 4 elements)
        if len(row) >= 4:
            lbl_inStock.config(text=f"In Stock [{row[3]}]")
        else:
            lbl_inStock.config(text="In Stock [Data Missing]")  # Handle missing data
    else:
        # Handle the case where no row is selected
        var_pid.set("")
        var_pname.set("")
        var_price.set("")
        lbl_inStock.config(text="In Stock [-]")  # Clear display or show default message

product_table.heading("pid",text="PID")
product_table.heading("name",text="Name")
product_table.heading("price",text="Price")
product_table.heading("qty",text="Quantity")
product_table.heading("status",text="Status")
product_table["show"]="headings"
product_table.column("pid",anchor=tk.CENTER,width=90)
product_table.column("name",anchor=tk.CENTER,width=100)
product_table.column("price",anchor=tk.CENTER,width=100)
product_table.column("qty",anchor=tk.CENTER,width=100)
product_table.column("status",anchor=tk.CENTER,width=100)
product_table.pack(fill=BOTH,expand=1)
product_table.bind("<ButtonRelease-1>", get_data)

lbl_note=Label(product_frame3,text="Note:Enter 0 Quantity to remove product from the cart",font=('times new roman',12),bg="white",fg="red").pack(side=BOTTOM,fill=X)

customer_frame=Frame(window,bd=4,relief=RIDGE,bg="white")
customer_frame.place(x=395,y=110,width=490,height=70)

pTitle=Label(customer_frame,text="Customer Details",font=('times new roman',15,'bold'),bg="lightgray").pack(side=TOP,fill=X)

var_cname=StringVar()
var_contact=StringVar()
lblname=Label(customer_frame,text="Name ",font=('times new roman',15),bg="white").place(x=5,y=35)
txtsearch=Entry(customer_frame,textvariable=var_cname,font=('times new roman',13),bg="white").place(x=60,y=35,width=180,height=22)

lblcontact=Label(customer_frame,text="Contact",font=('times new roman',15),bg="white").place(x=230,y=35)
txtcontact=Entry(customer_frame,textvariable=var_contact,font=('times new roman',13),bg="white").place(x=300,y=35,width=180,height=22)

cal_cart_Frame=Frame(window,bd=4,relief=RIDGE,bg="white")
cal_cart_Frame.place(x=395,y=180,width=490,height=340)

var_cal_input=StringVar()
cal_Frame=Frame(cal_cart_Frame,relief=RIDGE,bg="white")
cal_Frame.place(x=5,y=5,width=268,height=320)

txt_cal_input=Entry(cal_Frame,textvariable=var_cal_input,font=('arial',15,'bold'),width=23,bd=8,relief=GROOVE,state='readonly',justify=RIGHT)
txt_cal_input.grid(row=0,columnspan=4)

btn_7=Button(cal_Frame,text='7',font=('arial',15,'bold'),command=lambda:get_input(7),bd=6,width=4,height=1,pady=10,cursor="hand2").grid(row=1,column=0)
btn_8=Button(cal_Frame,text='8',font=('arial',15,'bold'),command=lambda:get_input(8),bd=6,width=4,height=1,pady=10,cursor="hand2").grid(row=1,column=1)
btn_9=Button(cal_Frame,text='9',font=('arial',15,'bold'),command=lambda:get_input(9),bd=6,width=4,height=1,pady=10,cursor="hand2").grid(row=1,column=2)
btn_sum=Button(cal_Frame,text='+',font=('arial',15,'bold'),command=lambda:get_input('+'),bd=6,width=4,height=1,pady=10,cursor="hand2").grid(row=1,column=3)

btn_4=Button(cal_Frame,text='4',font=('arial',15,'bold'),command=lambda:get_input(4),bd=6,width=4,height=1,pady=10,cursor="hand2").grid(row=2,column=0)
btn_5=Button(cal_Frame,text='5',font=('arial',15,'bold'),command=lambda:get_input(5),bd=6,width=4,height=1,pady=10,cursor="hand2").grid(row=2,column=1)
btn_6=Button(cal_Frame,text='6',font=('arial',15,'bold'),command=lambda:get_input(6),bd=6,width=4,height=1,pady=10,cursor="hand2").grid(row=2,column=2)
btn_sub=Button(cal_Frame,text='-',font=('arial',15,'bold'),command=lambda:get_input('-'),bd=6,width=4,height=1,pady=10,cursor="hand2").grid(row=2,column=3)

btn_1=Button(cal_Frame,text='1',font=('arial',15,'bold'),command=lambda:get_input(1),bd=6,width=4,height=1,pady=10,cursor="hand2").grid(row=3,column=0)
btn_2=Button(cal_Frame,text='2',font=('arial',15,'bold'),command=lambda:get_input(2),bd=6,width=4,height=1,pady=10,cursor="hand2").grid(row=3,column=1)
btn_3=Button(cal_Frame,text='3',font=('arial',15,'bold'),command=lambda:get_input(3),bd=6,width=4,height=1,pady=10,cursor="hand2").grid(row=3,column=2)
btn_mul=Button(cal_Frame,text='*',font=('arial',15,'bold'),command=lambda:get_input('*'),bd=6,width=4,height=1,pady=10,cursor="hand2").grid(row=3,column=3)

btn_0=Button(cal_Frame,text='0',font=('arial',15,'bold'),command=lambda:get_input(0),bd=6,width=4,height=1,pady=10,cursor="hand2").grid(row=4,column=0)
btn_c=Button(cal_Frame,text='C',font=('arial',15,'bold'),command=lambda:clear_cal(),bd=6,width=4,height=1,pady=10,cursor="hand2").grid(row=4,column=1)
btn_eq=Button(cal_Frame,text='=',font=('arial',15,'bold'),command=lambda:perform_cal(),bd=6,width=4,height=1,pady=10,cursor="hand2").grid(row=4,column=2)
btn_div=Button(cal_Frame,text='/',font=('arial',15,'bold'),command=lambda:get_input('/'),bd=6,width=4,height=1,pady=10,cursor="hand2").grid(row=4,column=3)


cart_frame=Frame(cal_cart_Frame,relief=RIDGE,bd=0)
cart_frame.place(x=275,y=5,width=205,height=320)
cartTitle = Label(cart_frame, text="Cart \t Total Products[0]", font=('times new roman', 13), bg="lightgray") 
cartTitle.pack(side=TOP, fill=X)

scrolly=Scrollbar(cart_frame,orient=VERTICAL)
scrollx=Scrollbar(cart_frame,orient=HORIZONTAL)

cart_table=ttk.Treeview(cart_frame,columns=("pid","name","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
scrollx.pack(side=BOTTOM,fill=X)
scrolly.pack(side=RIGHT,fill=Y)
scrollx.config(command=cart_table.xview)
scrolly.config(command=cart_table.yview)

cart_table.heading("pid",text="PID")
cart_table.heading("name",text="Name")
cart_table.heading("price",text="Price")
cart_table.heading("qty",text="Quantity")
cart_table.heading("status",text="Status")
cart_table["show"]="headings"
cart_table.column("pid",width=40)
cart_table.column("name",width=100)
cart_table.column("price",width=90)
cart_table.column("qty",width=40)
cart_table.column("status",width=90)
cart_table.pack(fill=BOTH,expand=1)

var_pid=StringVar()
var_pname=StringVar()
var_price=StringVar()
var_qty=StringVar()
var_stock=StringVar()

Add_CartWidgetsFrame=Frame(window,bd=2,relief=RIDGE,bg="white")
Add_CartWidgetsFrame.place(x=395,y=510,width=490,height=120)

lbl_p_name=Label(Add_CartWidgetsFrame,text="Product Name",font=("times new roman",15),bg="white").place(x=5,y=5)
txt_p_name=Entry(Add_CartWidgetsFrame,textvariable=var_pname,font=("times new roman",15),bg="lightyellow",state='readonly').place(x=5,y=35,width=130,height=22)

lbl_p_price=Label(Add_CartWidgetsFrame,text="Price Per Qty",font=("times new roman",15),bg="white").place(x=160,y=5)
txt_p_price=Entry(Add_CartWidgetsFrame,textvariable=var_price,font=("times new roman",15),bg="lightyellow",state='readonly').place(x=160,y=35,width=130,height=22)

lbl_p_qty=Label(Add_CartWidgetsFrame,text="Quantity",font=("times new roman",15),bg="white").place(x=315,y=5)
txt_p_qty=Entry(Add_CartWidgetsFrame,textvariable=var_qty,font=("times new roman",15),bg="lightyellow").place(x=315,y=35,width=130,height=22)

lbl_inStock = Label(Add_CartWidgetsFrame, text="In Stock [9999]", font=("times new roman", 15), bg="white")
lbl_inStock.place(x=5, y=65)
btn_clear_cart=Button(Add_CartWidgetsFrame,text="Clear",font=("times new roman",15,"bold"),bg="lightgray",cursor="hand2", command=lambda: clear_cart_widgets()).place(x=160,y=65,width=130,height=30)
btn_add_cart = Button(Add_CartWidgetsFrame, 
                     text="Add", 
                     command=lambda: add_update_cart(), 
                     font=("times new roman", 15, "bold"), 
                     bg="orange", 
                     cursor="hand2")
btn_add_cart.place(x=315, y=65, width=130, height=30)
billFrame=Frame(window,bd=2,relief=RIDGE,bg='white')
billFrame.place(x=885,y=110,width=380,height=410)

BTitle=Label(billFrame,text="Customer Bill Area",font=('times new roman',15,'bold'),bg="#262626",fg="white").pack(side=TOP,fill=X)
scrolly=Scrollbar(billFrame,orient=VERTICAL)
scrolly.pack(side=RIGHT,fill=Y)
txt_bill_area=Text(billFrame,yscrollcommand=scrolly.set,font=('times new roman',10))
txt_bill_area.pack(fill=BOTH,expand=1)
scrolly.config(command=txt_bill_area)

billMenuFrame=Frame(window,bd=2,relief=RIDGE,bg='white')
billMenuFrame.place(x=885,y=520,width=380,height=140)

lbl_amnt=Label(billMenuFrame,text='Bill Amount\n[0]',font=('times new roman',12,'bold'),bg="#3f51b5",fg="white")
lbl_amnt.place(x=2,y=3,width=120,height=65)

lbl_discount=Label(billMenuFrame,text='Discount\n[5%]',font=('times new roman',12,'bold'),bg="#8bc34a",fg="white")
lbl_discount.place(x=124,y=3,width=120,height=65)

lbl_net_pay=Label(billMenuFrame,text='Net Pay\n[0]',font=('times new roman',12,'bold'),bg="#607d8b",fg="white")
lbl_net_pay.place(x=246,y=3,width=140,height=65)


def print_content():
    try:
        # Example: Print content of the frame (for simplicity, we'll assume it's a text or label)
        content = "This is the content of your bill or frame."  # Replace this with dynamic content
        print(content)  # Or use a more sophisticated method to print content
        messagebox.showinfo("Print", "Bill has been sent to the printer!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
# Print button
btn_print = tk.Button(billMenuFrame, text='Print', cursor='hand2', font=('times new roman', 12, 'bold'), bg="red", fg="white", command=print_content)
btn_print.place(x=2, y=70, width=120, height=50)

btn_clear_all=Button(billMenuFrame,text='Clear All',cursor='hand2',font=('times new roman',12,'bold'),bg="gray",fg="white",command=lambda:clear_allb)
btn_clear_all.place(x=124,y=70,width=120,height=50)

btn_generate = Button(billMenuFrame, 
                     text='Generate/Save Bill', 
                     cursor='hand2', 
                     font=('times new roman', 12, 'bold'), 
                     bg="#009688", 
                     fg="white", 
                     command=lambda:generate_bill)  # Assign the function here
btn_generate.place(x=246, y=70, width=140, height=50)

def get_input(num):
    xnum=var_cal_input.get()+str(num)
    var_cal_input.set(xnum)
def clear_cal():
    var_cal_input.set('')

def perform_cal():
    result=var_cal_input.get()
    var_cal_input.set(eval(result))


def show_all_products():
    try:
        mydb = mysql.connector.connect(host="localhost", user="root", password="", database="inventory_system")
        mycursor = mydb.cursor()

        # Query to fetch all products
        mycursor.execute("SELECT id,name,price,quantity,status FROM product_data")
        rows = mycursor.fetchall()

        # Clear the treeview and display all products
        product_table.delete(*product_table.get_children())
        for row in rows:
            product_table.insert('', END, values=row)

    except Exception as e:
        messagebox.showerror('Error', f"Error due to: {str(e)}")

    finally:
        if mydb:
            mydb.close()  # Close the connection if it exists
def search_products():
    """Search products with inline validation."""
    search_term = varsearch.get().strip()  # Get search term and remove leading/trailing spaces

    # Inline validation for empty search term
    if not search_term:
        messagebox.showerror("Validation Error", "Please enter product name!!")
        return  # Stop execution if validation fails

    try:
        mydb = mysql.connector.connect(host="localhost", user="root", password="", database="inventory_system")
        mycursor = mydb.cursor()

        # Construct search query with LIKE operator for name
        query = "SELECT id, name, price, quantity, status FROM product_data WHERE name LIKE %s"
        mycursor.execute(query, ("%"+search_term+"%",))
        rows = mycursor.fetchall()

        # Clear table and display search results
        product_table.delete(*product_table.get_children())
        for row in rows:
            product_table.insert('', END, values=row)

    except Exception as e:
        messagebox.showerror('Error', f"Error due to: {str(e)}")

    finally:
        if mydb:
            mydb.close()

def get_data(ev):
    selected_row = product_table.focus()
    if selected_row:  # Check if a row is actually selected
        content = product_table.item(selected_row)
        row = content['values']
        var_pid.set(row[0])
        var_pname.set(row[1])
        var_price.set(row[2])
        # Check if quantity information exists (at least 4 elements)
        if len(row) >= 4:
            lbl_inStock.config(text=f"In Stock [{row[3]}]") 
        else:
            lbl_inStock.config(text="In Stock [Data Missing]")  # Handle missing data
    else:
        # Handle the case where no row is selected
        var_pid.set("")
        var_pname.set("")
        var_price.set("")
        lbl_inStock.config(text="In Stock [-]")  # Clear display or show default message
def add_update_cart():
    """Add or update items in the cart with quantity validation."""
    if var_qty.get() == '':
        messagebox.showerror('Error', 'Quantity is required', parent=window)
        return  # Exit function if quantity is empty

    # Validate if quantity is a positive integer
    if not var_qty.get().isdigit() or int(var_qty.get()) <= 0:
        messagebox.showerror('Error', 'Please enter a valid positive quantity!', parent=window)
        return  # Exit function if quantity is invalid

    try:
        # Calculate price based on quantity and price
        price_cal = int(var_qty.get()) * float(var_price.get())
        price_cal = float(price_cal)
        print(price_cal)
        
        # Call the function to insert into the cart
        insert_into_cart(price_cal)

        # Clear Add_CartWidgetsFrame components
        var_pid.set("")
        var_pname.set("")
        var_price.set("")
        var_qty.set("")
        lbl_inStock.config(text="In Stock [-]")

    except Exception as e:
        messagebox.showerror('Error', f"Error due to: {str(e)}", parent=window)


# This function inserts product details into cart table
def insert_into_cart(price_cal):
  try:
    # Get product details from entry fields
    product_id = var_pid.get()
    product_name = var_pname.get()
    product_price = var_price.get()
    product_qty = var_qty.get()
    # Insert product details into cart_table
    cart_table.insert('', 'end', values=(product_id, product_name, product_price, product_qty, "Added"))
    if cartTitle: 
        cart_title_text = cartTitle.cget("text")
        try:
        # Extract the number within square brackets
            start_index = cart_title_text.find("[") + 1 
            end_index = cart_title_text.find("]")
            product_count_str = cart_title_text[start_index:end_index]
            total_products = int(cart_title_text.split("[")[1].split(")")[0]) + 1
        except ValueError:
        # Handle the case where no products are in the cart (e.g., "[0]")
            total_products = 1 
        cartTitle.config(text=f"Cart \t Total Products[{total_products}]")

  except Exception as e:
    messagebox.showerror('Error', f"Error due to: {str(e)}")
def clear_cart_widgets():
  """Clears the product details and resets the in-stock label in Add_CartWidgetsFrame."""
  var_pid.set("")
  var_pname.set("")
  var_price.set("")
  var_qty.set("")
  lbl_inStock.config(text="In Stock [-]")
def generate_bill():
    """Generates a professionally formatted, center-aligned bill, decreases product quantities, 
    stores it in the database, and saves it as a .txt file."""
    from datetime import datetime
    import mysql.connector
    from tkinter import messagebox
    import tkinter as tk
    import random
    import os

    try:
        # Database connection
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="inventory_system"
        )
        cursor = db.cursor()

        # Current date and time
        current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Generate a random invoice number
        invoice_number = f"INV-{random.randint(1000, 9999)}"

        # Retrieve customer details
        customer_name = var_cname.get().strip()
        customer_contact = var_contact.get().strip()

        # Validate customer name and contact
        if not customer_name and not customer_contact:
            messagebox.showerror("Error", "Customer name and Contact Number is required", parent=window)
            return
        #if not customer_contact:
            #messagebox.showerror("Error", "Contact number is required", parent=window)
           # return
        if not customer_contact.isdigit() or len(customer_contact) != 10:
            messagebox.showerror("Error", "Enter a valid 10-digit contact number", parent=window)
            return

        # Check if cart is empty
        cart_items = cart_table.get_children()
        if not cart_items:
            messagebox.showerror("Error", "Cart is empty! Please add items before generating a bill.", parent=window)
            return

        # Calculate total amount and prepare item data
        total_amount = 0.0
        item_data = []
        for item in cart_items:
            item_values = cart_table.item(item)['values']
            item_id = item_values[0]  # Assuming the first value is the product ID
            item_name = item_values[1]
            item_price = float(item_values[2])
            item_qty = int(item_values[3])
            item_total = item_price * item_qty
            total_amount += item_total
            item_data.append((item_id, item_name, item_price, item_qty, item_total))

        # Apply discount
        discount_rate = 0.05  # 5% discount
        discount_amount = total_amount * discount_rate
        net_payable = total_amount - discount_amount

        # Insert bill data into the `bills` table
        cursor.execute(
            "INSERT INTO bills (invoice_number, customer_name, customer_contact, bill_date, subtotal, discount_amount, net_payable) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (invoice_number, customer_name, customer_contact, current_date, total_amount, discount_amount, net_payable)
        )
        bill_id = cursor.lastrowid

        # Insert items into the `bill_items` table and update product quantities
        for item in item_data:
            product_id = item[0]
            item_name = item[1]
            item_price = item[2]
            item_qty = item[3]
            item_total = item[4]

            # Insert into `bill_items`
            cursor.execute(
                "INSERT INTO bill_items (bill_id, item_name, item_price, item_qty, item_total) VALUES (%s, %s, %s, %s, %s)",
                (bill_id, item_name, item_price, item_qty, item_total)
            )

            # Update product quantity
            cursor.execute(
                "UPDATE product_data SET quantity = quantity - %s WHERE id = %s AND quantity >= %s",
                (item_qty, product_id, item_qty)
            )
            if cursor.rowcount == 0:
                db.rollback()
                messagebox.showerror("Error", f"Insufficient stock for product ID: {product_id}", parent=window)
                return

        db.commit()

        # Generate the bill text
        bill_width = 50
        center = lambda text: text.center(bill_width)

        bill_text = "\n"
        bill_text += "=" * bill_width + "\n"
        bill_text += center("ELECTRONICS SHOP BILLING SYSTEM") + "\n"
        bill_text += center("*** OFFICIAL BILL ***") + "\n"
        bill_text += "=" * bill_width + "\n\n"
        bill_text += f"{center(f'Invoice Number: {invoice_number}')} \n"
        bill_text += f"{center(f'Date: {current_date}')} \n"
        bill_text += f"{center(f'Customer Name: {customer_name}')} \n"
        bill_text += f"{center(f'Contact: {customer_contact}')} \n"
        bill_text += "=" * bill_width + "\n\n"

        # Table header
        bill_text += center("{:<25} {:<15} {:<10} {:<15}".format("Item", "Unit Price (₹)", "Qty", "Total (₹)")) + "\n"
        bill_text += center("-" * 70) + "\n"

        # Table content
        for item in item_data:
            item_line = "{:<25} {:<15.2f} {:<10} {:<15.2f}".format(item[1][:25], item[2], item[3], item[4])
            bill_text += center(item_line) + "\n"

        bill_text += center("-" * 70) + "\n"

        # Summary
        bill_text += f"{center(f'Subtotal: ₹{total_amount:.2f}')} \n"
        bill_text += f"{center(f'Discount (5%): ₹{discount_amount:.2f}')} \n"
        bill_text += f"{center(f'Net Payable: ₹{net_payable:.2f}')} \n"
        bill_text += "=" * bill_width + "\n\n"

        # Footer
        bill_text += center("Thank you for shopping with us!") + "\n"
        bill_text += center("We look forward to serving you again.") + "\n"
        bill_text += center("For inquiries, contact us at support@shop.com") + "\n"
        bill_text += "=" * bill_width + "\n"

        # Display the bill
        txt_bill_area.delete("1.0", tk.END)
        txt_bill_area.insert("1.0", bill_text)

        # Save the bill as a .txt file
        save_path = os.path.join(os.getcwd(), "bills")  # Save in a "bills" directory
        os.makedirs(save_path, exist_ok=True)
        file_name = f"{invoice_number}.txt"
        file_path = os.path.join(save_path, file_name)
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(bill_text)

        messagebox.showinfo("Saved", f"Bill saved successfully as {file_name}", parent=window)

        # Update summary labels
        lbl_amnt.config(text=f"Bill Amount\n₹{total_amount:.2f}")
        lbl_discount.config(text=f"Discount\n₹{discount_amount:.2f}")
        lbl_net_pay.config(text=f"Net Pay\n₹{net_payable:.2f}")

    except mysql.connector.Error as db_error:
        messagebox.showerror("Database Error", f"Error interacting with the database: {str(db_error)}", parent=window)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}", parent=window)
    finally:
        if 'db' in locals() and db.is_connected():
            cursor.close()
            db.close()


def clear_allb():
    """Clears all bill-related information."""

    # Clear bill area text
    txt_bill_area.delete("1.0", tk.END) 

    # Clear cart
    for item in cart_table.get_children():
        cart_table.delete(item)
    cartTitle.config(text="Cart \t Total Products[0]")

    # Clear customer details
    var_cname.set("")
    var_contact.set("")

    # Clear bill amount labels
    lbl_amnt.config(text='Bill Amount\n[0]')
    lbl_discount.config(text='Discount\n[5%]')
    lbl_net_pay.config(text='Net Pay\n[0]')

# Assuming btn_clear_all is defined earlier in your code:
btn_clear_all.config(command=clear_allb)
btnsearch.config(command=search_products)
btn_generate.config(command=generate_bill)
# Main event loop
show_all_products()
window.mainloop()