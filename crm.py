from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import ttkbootstrap as tb
import sqlite3


# color choices: primary, secondary, success, info, warning, danger, light, dark
# dark theme options: solar, superhero, darkly, cyborg, vapor
# light theme options: cosmo, flatly, journal, litera, lumen, minty, pulse, 
#                      sandstone, united, yeti, morph, simplex, cerculean

root = tb.Window(themename="superhero")
root.title('CRM')
root.geometry("%dx%d" % (root.winfo_screenwidth(), root.winfo_screenheight()))  # full screen
#root.geometry('1440x700')

# create styles
style = tb.Style()
style.configure('primary.Outline.TButton', font=("Helvetica", 14))
style.configure('warning.TLabel', font=("Helvetica", 14))
style.configure('success.TMenubutton', font=("Helvetica", 12))
style.configure('warning.Outline.TMenubutton', font=("Helvetica", 14), width=12)


# clear the treeview
def cleartreeview():
    for record in mytree.get_children():
        mytree.delete(record)

# create a query function to load database every time it starts
def querydb():
    # clear the treeview
    cleartreeview()

    #Create a database or connect to one that exists
    conn = sqlite3.connect('crm.db')

    # create a cursor to read around the db
    cur = conn.cursor()

    # query the database
    cur.execute("SELECT rowid, * FROM customers")
    records = cur.fetchall()
    
    # add our data to the screen
    global count
    count = 0

    for record in records:
        if count % 2 == 0:
            mytree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]), tags=('evenrow',))
        else:
            mytree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]), tags=('oddrow',))
    # increase our counter
        count += 1
        
    # commit changes
    conn.commit()

    # close our connection to database
    conn.close()


# clear entry boxes
def clearentries():
    cidentry.delete(0, END)
    fnameentry.delete(0, END)
    lnameentry.delete(0, END)
    emailentry.delete(0, END)
    phoneentry.delete(0, END)
    adrsentry.delete(0, END)
    cityentry.delete(0, END)
    pvnentry.delete(0, END)
    pcentry.delete(0, END)


def searchrecords():
    # create variable of the search box input
    lookuprecord = searchentry.get()

    # close the search box
    search.destroy()

    # clear the treeview
    cleartreeview()
 
    #Create a database or connect to one that exists
    conn = sqlite3.connect('crm.db')

    # create a cursor to read around the db
    cur = conn.cursor()

    # query the database
    cur.execute("SELECT rowid, * FROM customers WHERE last_name like ? or first_name like ?", (lookuprecord, lookuprecord,))
    records = cur.fetchall()
    
    # add our data to the screen
    global count
    count = 0

    for record in records:
        if count % 2 == 0:
            mytree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]), tags=('evenrow',))
        else:
            mytree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]), tags=('oddrow',))
    # increase our counter
        count += 1
        
    # commit changes
    conn.commit()

    # close our connection to database
    conn.close()


def lookuprecords():
    global searchentry, search

    search = tb.Toplevel(root)
    search.title("Lookup Records")
    search.geometry("400x200")
    
    # create label frame
    searchframe = LabelFrame(search, text="First Name or Last Name", font=("Helvetica", 12))
    searchframe.pack(padx=10, pady=10)

    # add entry box
    searchentry = tb.Entry(searchframe, font=("Helvetica", 14))
    searchentry.pack(padx=20, pady=20)

    # add button
    searchbtn = tb.Button(search, text="Search Records", style="primary.Outline.TButton", command=searchrecords)
    searchbtn.pack(padx=20, pady=20)


def searchname(item):
    if item == 'Search':
        lookuprecords()
    else:
        querydb()


# create a menu
#mymenu = tb.Menu(root)
#root.config(menu=mymenu)
#mymenu.pack(pady=20)

# configure search menu
#searchmenu = tb.Menu(mymenu, tearoff=0,)
#mymenu.add_cascade(label="Search", menu=searchmenu,)

# drop down menu  
#searchmenu.add_command(label="Search", command=lookuprecords)
#searchmenu.add_separator()
#searchmenu.add_command(label="Start Over", command=querydb)


'''
# create fake data
data = [
    [1, "John", "Smith", "john@smith.com", "123-456-7890", "123 Main St", "Regina", "SK", "S3U 6Q4"],
    [2, "Amy", "Hill", "amy@hill.com", "114-225-3336", "34-234 21 Ave SW", "Calgary", "AB", "T0J 3V7"],
    [3, "Mary", "Rosy", "mary@rosy.com", "775-443-5462", "56 Hill Blvd NW", "Edmonton", "AB", "E6B 1C9"],
    [4, "David", "Richardson", "david@richardson.com", "668-254-1136", "443 McKnight Blvd SE", "Calgary", "AB", "T4X 7R0"],
    [5, "Kelly", "Tasker", "kelly@tasker.com", "714-285-3647", "971 Sunset Dr", "Saskatoon", "SK", "S2I 2B5"],
    [6, "Allan", "Taskerson", "allan@taskerson.com", "414-254-3647", "1 Morning Dr", "Saskatoon", "SK", "S4T 2I5"],
    [7, "Kelly", "Tasker", "kelly@tasker.com", "714-285-3647", "971 Sunset Dr", "Saskatoon", "SK", "S2I 2B5"],
    [8, "Kelly", "Tasker", "kelly@tasker.com", "714-285-3647", "971 Sunset Dr", "Saskatoon", "SK", "S2I 2B5"],
    [9, "Kelly", "Tasker", "kelly@tasker.com", "714-285-3647", "971 Sunset Dr", "Saskatoon", "SK", "S2I 2B5"],
    [10, "Kelly", "Tasker", "kelly@tasker.com", "714-285-3647", "971 Sunset Dr", "Saskatoon", "SK", "S2I 2B5"],
    [11, "Kelly", "Tasker", "kelly@tasker.com", "714-285-3647", "971 Sunset Dr", "Saskatoon", "SK", "S2I 2B5"],
    [12, "Kelly", "Tasker", "kelly@tasker.com", "714-285-3647", "971 Sunset Dr", "Saskatoon", "SK", "S2I 2B5"],
    [13, "Kelly", "Tasker", "kelly@tasker.com", "714-285-3647", "971 Sunset Dr", "Saskatoon", "SK", "S2I 2B5"],
    [14, "Kelly", "Tasker", "kelly@tasker.com", "714-285-3647", "971 Sunset Dr", "Saskatoon", "SK", "S2I 2B5"],
    [15, "Kelly", "Tasker", "kelly@tasker.com", "714-285-3647", "971 Sunset Dr", "Saskatoon", "SK", "S2I 2B5"],
    ]
'''

# Create a database or connect to one that exists
conn = sqlite3.connect('crm.db')

# create a cursor to read around the db
cur = conn.cursor()

# create table (only did once)
cur.execute("""CREATE TABLE if not exists customers (
            first_name text,
            last_name text,
            email text,
            phone_number text,
            address text,
            city text,
            province text,
            postal_code text
            )""")
'''
# add fake data to database (only do one time)
for record in data:
    cur.execute("INSERT INTO customers VALUES(:customer_id, :first_name, :last_name, :email, :phone_number, :address, :city, :province, :postal_code)",
                {
                    'customer_id': record[0],
                    'first_name': record[1],
                    'last_name': record[2],
                    'email': record[3],
                    'phone_number': record[4],
                    'address': record[5],
                    'city': record[6],
                    'province': record[7],
                    'postal_code': record[8]
                })
'''

# commit changes
conn.commit()

# close our connection to database
conn.close()


# configure the treeview colors
style.configure("Treeview",
                background="#D3D3D3",
                foreground="black",
                rowheight=30,
                fieldbackground="#D3D3D3",
                font=("Helvetica", 14))

# change selected color
style.map('Treeview',
          background=[('selected','#347083')],
          )

# create a treeview frame
treeframe = tb.Frame(root)
treeframe.pack(pady=20)

# create a treeview scrollbar
treescroll = tb.Scrollbar(treeframe)
treescroll.pack(side=RIGHT, fill=Y)

# create the treeview
mytree = tb.Treeview(treeframe, yscrollcommand=treescroll.set, selectmode='extended')
mytree.pack()

# configure the scrollbar
treescroll.config(command=mytree.yview)

# define our columns
mytree['columns'] = ("Customer ID", "First Name", "Last Name", "Email", "Phone Number", "Address", "City", "Province", "Postal Code")

# format our columns
mytree.column("#0", width=0, stretch=NO)   # hidden column to make treeview look good and tidy
mytree.column("Customer ID", anchor=CENTER, width=100)
mytree.column("First Name", anchor=W, width=160)
mytree.column("Last Name", anchor=W, width=160)
mytree.column("Email", anchor=W, width=250)
mytree.column("Phone Number", anchor=CENTER, width=180)
mytree.column("Address", anchor=W, width=250)
mytree.column("City", anchor=W, width=180)
mytree.column("Province", anchor=W, width=100)
mytree.column("Postal Code", anchor=W, width=150)

# create and format headings
style.configure('Treeview.Heading', font=("Helvetica", 14),)
mytree.heading("#0", text="", anchor=W)
mytree.heading("Customer ID", text="Customer ID", anchor=CENTER)
mytree.heading("First Name", text="First Name", anchor=W)
mytree.heading("Last Name", text="Last Name", anchor=W)
mytree.heading("Email", text="Email", anchor=W)
mytree.heading("Phone Number", text="Phone Number", anchor=CENTER)
mytree.heading("Address", text="Address", anchor=W)
mytree.heading("City", text="City", anchor=W)
mytree.heading("Province", text="Province", anchor=W)
mytree.heading("Postal Code", text="Postal Code", anchor=W)

#create striped row tags
mytree.tag_configure('oddrow', background="white")
mytree.tag_configure('evenrow', background="lightgreen")


# add record entry boxes
dataframe = LabelFrame(root, text="Record", font=("Helvetica", 12))
dataframe.pack(fill="x", expand="yes", padx=20)

cidlabel = tb.Label(dataframe, text="Customer ID", style='warning.TLabel')
cidlabel.grid(row=0, column=0, padx=10, pady=10)
cidentry = tb.Entry(dataframe, font=("Helvetica", 14))
cidentry.grid(row=0, column=1, padx=10, pady=10)

fnamelabel = tb.Label(dataframe, text="First Name", style='warning.TLabel')
fnamelabel.grid(row=1, column=0, padx=10, pady=10)
fnameentry = tb.Entry(dataframe, font=("Helvetica", 14))
fnameentry.grid(row=1, column=1, padx=10, pady=10)

lnamelabel = tb.Label(dataframe, text="Last Name", style='warning.TLabel')
lnamelabel.grid(row=1, column=2, padx=10, pady=10)
lnameentry = tb.Entry(dataframe, font=("Helvetica", 14))
lnameentry.grid(row=1, column=3, padx=10, pady=10)

emaillabel = tb.Label(dataframe, text="Email", style='warning.TLabel')
emaillabel.grid(row=1, column=4, padx=10, pady=10)
emailentry = tb.Entry(dataframe, font=("Helvetica", 14))
emailentry.grid(row=1, column=5, padx=10, pady=10)

phonelabel = tb.Label(dataframe, text="Phone Number", style='warning.TLabel')
phonelabel.grid(row=1, column=6, padx=10, pady=10)
phoneentry = tb.Entry(dataframe, font=("Helvetica", 14))
phoneentry.grid(row=1, column=7, padx=10, pady=10)

adrslabel = tb.Label(dataframe, text="Address", style='warning.TLabel')
adrslabel.grid(row=2, column=0, padx=10, pady=10)
adrsentry = tb.Entry(dataframe, font=("Helvetica", 14))
adrsentry.grid(row=2, column=1, padx=10, pady=10)

citylabel = tb.Label(dataframe, text="City", style='warning.TLabel')
citylabel.grid(row=2, column=2, padx=10, pady=10)
cityentry = tb.Entry(dataframe, font=("Helvetica", 14))
cityentry.grid(row=2, column=3, padx=10, pady=10)

pvnlabel = tb.Label(dataframe, text="Province", style='warning.TLabel')
pvnlabel.grid(row=2, column=4, padx=10, pady=10)
pvnentry = tb.Entry(dataframe, font=("Helvetica", 14))
pvnentry.grid(row=2, column=5, padx=10, pady=10)

pclabel = tb.Label(dataframe, text="Postal Code", style='warning.TLabel')
pclabel.grid(row=2, column=6, padx=10, pady=10)
pcentry = tb.Entry(dataframe, font=("Helvetica", 14))
pcentry.grid(row=2, column=7, padx=10, pady=10)


# move row up
def moveup():
    rows = mytree.selection()
    for row in rows:
        mytree.move(row, mytree.parent(row), mytree.index(row)-1)


# move row down
def movedown():
    rows = mytree.selection()
    for row in reversed(rows):
        mytree.move(row, mytree.parent(row), mytree.index(row)+1)


# remove one record
def removeone():
    # show a message to ask for confirmation before delete everything
    response = messagebox.askyesno("Delete Record!", "Are you sure? This can't be undone!")

    # add logic for message box
    if response == 1:  # if yes
        # clear the treeview
        x = mytree.selection()[0]
        mytree.delete(x)

        #Create a database or connect to one that exists
        conn = sqlite3.connect('crm.db')

        # create a cursor to read around the db
        cur = conn.cursor()

        # delete the selected record
        cur.execute("DELETE from customers WHERE oid=" + cidentry.get())

        # commit changes
        conn.commit()

        # close our connection to database
        conn.close()

        # clear entry boxes after record deleted
        clearentries()      

        # show a message after record deleted
        messagebox.showinfo("Record deleted!", "The selected record has been deleted from database!")

# remove many records
def removemany():
    # show a message to ask for confirmation before delete everything
    response = messagebox.askyesno("Delete Several Records!", "Are you sure? This can't be undone!")

    # add logic for message box
    if response == 1:  # if yes
        # designate selections
        x = mytree.selection()

        # create list of IDs from the selection
        ids_of_the_selection = []

        # add selections to ids_of_the_selections list
        for record in x:
            ids_of_the_selection.append(mytree.item(record, 'values')[0])

        # clear data from treeview
        for record in x:
            mytree.delete(record)
        
        #Create a database or connect to one that exists
        conn = sqlite3.connect('crm.db')

        # create a cursor to read around the db
        cur = conn.cursor()

        # delete the selected records
        cur.executemany("DELETE from customers WHERE oid = ?", [(i,) for i in ids_of_the_selection])

        # commit changes
        conn.commit()

        # close our connection to database
        conn.close()

        # clear entry boxes after record deleted
        clearentries()      

        # show a message after record deleted
        messagebox.showinfo("Record deleted!", "The selected record has been deleted from database!")  

# remove all records
def removeall():
    # show a message to ask for confirmation before delete everything
    response = messagebox.askyesno("Delete Everything!", "Are you sure? This can't be undone!")

    # add logic for message box
    if response == 1:  # if yes
        # clear the treeview
        for record in mytree.get_children():
            mytree.delete(record)

        #Create a database or connect to one that exists
        conn = sqlite3.connect('crm.db')

        # create a cursor to read around the db
        cur = conn.cursor()

        # delete all records by using drop table 
        cur.execute("DROP TABLE customers")

        # commit changes
        conn.commit()

        # close our connection to database
        conn.close()

        # clear entry boxes after record deleted
        clearentries()

        # recreate the table 
        recreatetable()


# select record
def selectrecord(e):
    # clear entry boxes
    clearentries()

    # grab record number
    selected = mytree.focus()
    # grab record values
    values = mytree.item(selected, "values")

    # output values to entry boxes
    cidentry.insert(0, values[0])
    fnameentry.insert(0, values[1])
    lnameentry.insert(0, values[2])
    emailentry.insert(0, values[3])
    phoneentry.insert(0, values[4])
    adrsentry.insert(0, values[5])
    cityentry.insert(0, values[6])
    pvnentry.insert(0, values[7])
    pcentry.insert(0, values[8])

# update a record
def updaterecord():
    # grab the record number
    selected = mytree.focus()
    # update record
    mytree.item(selected, text="", values=(cidentry.get(), fnameentry.get(), lnameentry.get(), emailentry.get(), phoneentry.get(), adrsentry.get(), cityentry.get(), pvnentry.get(), pcentry.get(),))
    
    # update database
    #Create a database or connect to one that exists
    conn = sqlite3.connect('crm.db')

    # create a cursor to read around the db
    cur = conn.cursor()

    # update database record with whatever in the entry boxes
    cur.execute("""UPDATE customers SET
                first_name = :first,
                last_name = :last,
                email = :email,
                phone_number = :phonenum,
                address = :address,
                city = :city,
                province = :province,
                postal_code = :pcode

                WHERE oid = :oid""",
                {
                    'first': fnameentry.get(),
                    'last': lnameentry.get(),
                    'email': emailentry.get(),
                    'phonenum': phoneentry.get(),
                    'address': adrsentry.get(),
                    'city': cityentry.get(),
                    'province': pvnentry.get(),
                    'pcode': pcentry.get(),
                    'oid': cidentry.get()
                })  
        
    # commit changes
    conn.commit()

    # close our connection to database
    conn.close()

    # clear entry boxes
    clearentries()


# add a new record into database
def addrecord():
    #Create a database or connect to one that exists
    conn = sqlite3.connect('crm.db')

    # create a cursor to read around the db
    cur = conn.cursor()

    # add new record
    cur.execute("INSERT INTO customers VALUES (:first, :last, :email, :phonenum, :address, :city, :province, :pcode)",
                {
                    'first': fnameentry.get(),
                    'last': lnameentry.get(),
                    'email': emailentry.get(),
                    'phonenum': phoneentry.get(),
                    'address': adrsentry.get(),
                    'city': cityentry.get(),
                    'province': pvnentry.get(),
                    'pcode': pcentry.get()
                })
       
    # commit changes
    conn.commit()

    # close our connection to database
    conn.close()

    # clear entry boxes
    clearentries()

    # clear the treeview table
    mytree.delete(*mytree.get_children())

    # reload the treeview table
    querydb()


def recreatetable():
    # Create a database or connect to one that exists
    conn = sqlite3.connect('crm.db')

    # create a cursor to read around the db
    cur = conn.cursor()

    # create table (only did once)
    cur.execute("""CREATE TABLE if not exists customers (
                first_name text,
                last_name text,
                email text,
                phone_number text,
                address text,
                city text,
                province text,
                postal_code text
                )""")
    
    # commit changes
    conn.commit()

    # close our connection to database
    conn.close()


# add buttons
btnframe = LabelFrame(root, text="Commands", font=("Helvetica", 12))
btnframe.pack(fill="x", expand="yes", padx=20)

addbtn = tb.Button(btnframe, text="Add Record", style='primary.Outline.TButton', command=addrecord)
addbtn.grid(row=0, column=0, padx=10, pady=10)

updatebtn = tb.Button(btnframe, text="Update Record", style="primary.Outline.TButton", command=updaterecord)
updatebtn.grid(row=0, column=1, padx=10, pady=10)

selectbtn = tb.Button(btnframe, text="Clear Entry Boxes", style="primary.Outline.TButton", command=clearentries)
selectbtn.grid(row=0, column=2, padx=10, pady=10)

moveupbtn = tb.Button(btnframe, text="Move Up", style="primary.Outline.TButton", command=moveup)
moveupbtn.grid(row=0, column=3, padx=10, pady=10)

movedownbtn = tb.Button(btnframe, text="Move Down", style="primary.Outline.TButton", command=movedown)
movedownbtn.grid(row=0, column=4, padx=10, pady=10)

removeonebtn = tb.Button(btnframe, text="Remove One Selected Record", style="primary.Outline.TButton", command=removeone)
removeonebtn.grid(row=0, column=5, padx=10, pady=10)

removemanybtn = tb.Button(btnframe, text="Remove Many Selected Records", style="primary.Outline.TButton", command=removemany)
removemanybtn.grid(row=0, column=6, padx=10, pady=10)

removeallbtn = tb.Button(btnframe, text="Remove All Records", style="primary.Outline.TButton", command=removeall)
removeallbtn.grid(row=0, column=7, padx=10, pady=10)

mymenu = tb.Menubutton(btnframe, text='Name Search', style='warning.Outline.TMenubutton')
mymenu.grid(row=0, column=8, padx=10, pady=10)

# configure search menu
searchmenu = tb.Menu(mymenu)
# drop down menu - add items to inside menubutton
item_in_dropdown = tb.StringVar()
for item in ['Search', 'Start Over']:
    searchmenu.add_radiobutton(label=item, 
                               font=("Helvetica", 14),
                               variable=item_in_dropdown, 
                               command=lambda item=item : searchname(item))
# associate inside menu with the menubutton
mymenu['menu'] = searchmenu


# bind the treeview with mouse selected and release the button
mytree.bind("<ButtonRelease-1>", selectrecord)

# load and display the table on start
querydb()


root.mainloop()