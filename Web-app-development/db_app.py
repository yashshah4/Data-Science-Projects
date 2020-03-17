# importing application framework
from tkinter import *
import tkinter as tkinter
import psycopg2
# creating an instance of Tk class
root = Tk()
# Changing the title of the app
root.title("Database application for PostgreSQL database")
# creating a new function to insert data into the db
def get_data(name, age, address):
    # We need database details to connect to it
    conn = psycopg2.connect(dbname="postgres", user="yashshah", password="yashshah", host="localhost", port="5432")
    # To write queries to the db, we first need to create a cursor like below
    cur = conn.cursor()
    # Now we can write a quesry as below & it will be executed automatically
    query = '''INSERT INTO student(NAME, AGE, ADDRESS) VALUES(%s,%s,%s);'''
    cur.execute(query, (name, age, address))
    # printing a message if the code execution is successful
    print("Data Inserted")
    # once the connection is established, we need to commit the changes and then close the connection
    conn.commit()
    # closing the connection
    conn.close()
    # adding display_all function here for immediate update of entry on screen
    display_all()
# craeting a function to search for data by id
def searchbyid(id_search):
    conn = psycopg2.connect(dbname="postgres", user="yashshah", password="yashshah4", host="localhost", port="5432")
    cur = conn.cursor()
    query = '''SELECT * FROM student WHERE id=%s;'''
    cur.execute(query,(id_search))
    # fetching the results from the query(use fetchall for more than 1 result entry)
    data = cur.fetchall()
    if data:
        disp(data)
    else:
        disp("No data available for these search parameters")
    conn.commit()
    conn.close()

# Creating a function to search for data by age
def searchbyage(search_age):
    conn = psycopg2.connect(dbname="postgres", user="yashshah", password="yashshah4", host="localhost", port="5432")
    cur = conn.cursor()
    query = '''SELECT * FROM student WHERE age={0}::text;'''
    cur.execute(query.format(search_age))
    data = cur.fetchall()
    if data:
        disp(data)
    else:
        disp("No data available for these search parameters")
    conn.commit()
    conn.close()
# Creating a new function to display the query result in the root window
def disp(data):
    listbox = Listbox(frame, width=35, height=1)
    listbox.grid(row=16,column=1)
    listbox.insert(END, data)

# Creating a new function to display all entries
def display_all():
    conn = psycopg2.connect(dbname="postgres", user="yashshah", password="yashshah4", host="localhost", port="5432")
    cur = conn.cursor()
    query = '''SELECT * FROM student;'''
    cur.execute(query)
    data = cur.fetchall()

    listbox = Listbox(frame, width=35, height=8)
    listbox.grid(row=20,column=1)
    # looping through all entries of the query result to print it all
    for x in data:
        listbox.insert(END, x)

# creating a canvas in the root window
Canvas(root, height = 480, width=900).pack()

# laying out a frame on the canvas
frame = Frame()
frame.place(relx=0.3,rely=0.1,relwidth=0.8,relheight=0.8)

# adding a label object and placing it on top middle of the root window
Label(frame, text="Add data").grid(row=0,column=1)

# creating new label & entry fields to accept name, age and address
Label(frame, text="Name").grid(row=1,column=0)
name_entry = Entry(frame)
name_entry.grid(row=1,column=1)

Label(frame, text="Age").grid(row=2,column=0)
age_entry = Entry(frame)
age_entry.grid(row=2,column=1)

Label(frame, text="Address").grid(row=3,column=0)
address_entry = Entry(frame)
address_entry.grid(row=3,column=1)

# adding a button to the frame to add the data
Button(frame, text="Add data", command=lambda: get_data(name_entry.get(),age_entry.get(),address_entry.get())).grid(row=5,column=1)
# creating a label for search functionality
Label(frame, text="Search for data").grid(row=10,column=1)
# Creating the label and entry field for id
Label(frame, text="Search by ID").grid(row=11, column=0)
id_search = Entry(frame)
id_search.grid(row=11,column=1)

# creating a search button
Button(frame, text="search", command=lambda: searchbyid(id_search.get())).grid(row=11,column=2)

# Creating the label and entry field for id
Label(frame, text="Search by Age").grid(row=12, column=0)
search_age = Entry(frame)
search_age.grid(row=12,column=1)

# creating a search button
Button(frame, text="search", command=lambda: searchbyage(search_age.get())).grid(row=12,column=2)

display_all()

# using main loop to show the window
root.mainloop()