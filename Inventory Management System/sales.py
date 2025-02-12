from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import os

def show(window, sales_list):
    sales_list.delete(0, END)
    # List files in 'bills' directory and filter for '.txt' files
    for i in os.listdir('bills'):  
        if i.split('.')[-1] == 'txt':  # Only show .txt files
            sales_list.insert(END, i)

def get_data(event, bill_area):
    # Get the widget from the event
    sales_list = event.widget
    # Get the selected index
    index_ = sales_list.curselection()  # Check if a selection is made
    filename = sales_list.get(index_[0])
    print("Selected file:", filename)
    bill_area.delete('1.0', END)
    filepath = f'bills/{filename}'  # Update to correct path
    try:
        with open(filepath, 'r', encoding='utf-8') as fp:
            bill_area.insert(END, fp.read())
    except Exception as e:
        messagebox.showerror("Error", f"Could not open the bill: {e}")

def sales_form(window):
    global back_image, bill_photo

    sales_frame = Frame(window, width=1070, height=567, bg='white')
    sales_frame.place(x=200, y=100)

    heading_Label = Label(sales_frame, text='View Customer Details', font=('Arial Unicode MS', 16, 'bold'), bg='#0f4d7d', fg='white')
    heading_Label.place(x=0, y=0, relwidth=1)

    back_image = PhotoImage(file='arrow.png')
    back_button = Button(sales_frame, image=back_image, bd=0, cursor='hand2', bg='white', command=lambda: sales_frame.place_forget())
    back_button.place(x=10, y=30)

    detail_frame = Frame(sales_frame, bg='white')
    detail_frame.place(x=50, y=50)

    id_label = Label(detail_frame, text='Invoice:', font=('Arial Unicode MS', 15, 'bold'), bg='white')
    id_label.grid(row=0, column=0, padx=20, sticky="w")
    id_entry = Entry(detail_frame, font=('Arial Unicode MS', 15, 'bold'), bg='lightyellow')
    id_entry.grid(row=0, column=1, pady=20)

    # Search Button
    def search_invoice():
        invoice_id = id_entry.get().strip()
        if not invoice_id:
            messagebox.showerror("Error", "Please enter an invoice ID!")
            return

        # Check if the invoice file exists in the 'bills' directory
        filepath = f'bills/{invoice_id}.txt'
        if os.path.exists(filepath):
            with open(filepath, 'r') as fp:
                bill_area.delete('1.0', END)
                bill_area.insert(END, fp.read())
        else:
            messagebox.showinfo("Not Found", f"Invoice '{invoice_id}' not found!")

    btn_search = Button(
        detail_frame,
        text="Search",
        font=('Arial Unicode MS', 15, 'bold'),
        bg="#010c48",
        fg="white",
        cursor="hand2",
        command=search_invoice
    )
    btn_search.grid(row=0, column=2, padx=20)

    # Cancel Button
    def cancel_search():
        id_entry.delete(0, END)  # Clear the invoice entry field
        bill_area.delete('1.0', END)  # Clear the bill display area
        show(window, sales_list)  # Reload the sales list

    btn_cancel = Button(
        detail_frame,
        text="Cancel",
        font=('Arial Unicode MS', 15, 'bold'),
        bg="#010c48",
        fg="white",
        cursor="hand2",
        command=cancel_search
    )
    btn_cancel.grid(row=0, column=3, padx=10)

    salesd_frame = Frame(sales_frame, bd=3, relief=RIDGE)
    salesd_frame.place(x=20, y=140, width=150, height=330)

    # Adding both vertical and horizontal scrollbars for sales_list
    scrolly = Scrollbar(salesd_frame, orient=VERTICAL)
    scrollx = Scrollbar(salesd_frame, orient=HORIZONTAL)
    sales_list = Listbox(salesd_frame, font=('Arial Unicode MS', 15), bg="white", yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
    scrolly.pack(side=RIGHT, fill=Y)
    scrollx.pack(side=BOTTOM, fill=X)  # Position the horizontal scrollbar at the bottom
    scrolly.config(command=sales_list.yview)
    scrollx.config(command=sales_list.xview)
    sales_list.pack(fill=BOTH, expand=1)

    # Bind the listbox selection to the get_data function
    sales_list.bind("<ButtonRelease-1>", lambda event: get_data(event, bill_area))

    bill_frame = Frame(sales_frame, bd=3, relief=RIDGE)
    bill_frame.place(x=170, y=140, width=580, height=330)

    heading_Label = Label(bill_frame, text='Customer Bills', font=('Arial Unicode MS', 16, 'bold'), bg='#009688', fg='white')
    heading_Label.pack(side=TOP, fill=X)

    # Adding both vertical and horizontal scrollbars for bill_area
    scrolly2 = Scrollbar(bill_frame, orient=VERTICAL)
    scrollx2 = Scrollbar(bill_frame, orient=HORIZONTAL)
    bill_area = Text(bill_frame, font=('times new roman', 15), bg="white", yscrollcommand=scrolly2.set, xscrollcommand=scrollx2.set, wrap="word")
    scrolly2.pack(side=RIGHT, fill=Y)
    scrollx2.pack(side=BOTTOM, fill=X)  # Position the horizontal scrollbar at the bottom
    scrolly2.config(command=bill_area.yview)
    scrollx2.config(command=bill_area.xview)
    bill_area.pack(fill=BOTH, expand=1)

    bill_photo = Image.open('logobill.jpg')  # Open the image
    bill_photo = bill_photo.resize((450, 300))  # Resize the image
    bill_photo = ImageTk.PhotoImage(bill_photo)

    lbl_image = Label(sales_frame, image=bill_photo, bd=0)
    lbl_image.image = bill_photo  # Persist the image reference
    lbl_image.place(x=755, y=110)

    show(window, sales_list)  # Pass `sales_list` to `show` to load the bills
