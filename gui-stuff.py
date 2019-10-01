from tkinter import *

# This database dictionary will store user:password pairs (encrypted in some way)
database = {}
main_gui = Tk()

# The program structure might not be the neatest rn
v1 = StringVar()
label_1 = Label(main_gui, text="Please enter your username:")
entry_user = Entry(main_gui, textvariable=v1)


v2 = StringVar()
label_2 = Label(main_gui, text="Please enter your password:")
entry_pass = Entry(main_gui, textvariable=v2)

def encrypt(some_phrase):
    # some encryption method... we will figure it out
    return some_phrase

def work():
    print("yellow")

def process_data():

    """
    This function takes the desired username and password input into the two text boxes in the GUI and does some
    operations.
    It checks it against the existing database, which must be limited to 20 users, to see if it exists, and if not, will
    input it into the database.



    """
    # Conditional will check our two conditions for adding to database: less than 20 entries and the user doesnt exist.
    username = str(entry_user.get())
    password = str(entry_pass.get())
    if len(database.items()) < 20 and database.get(username) is None:
        # Encrypt both the password and the username and update the database.

        # database.update({encrypt(username): encrypt(password)})
        database.update({username: password})
        print("hello?")
        print(database)

    elif database.get(username):
        print("Username already exists.")
        return
    else:
        print("Database is full")


button_submit = Button(main_gui, text="Submit", command=process_data)


label_1.grid(row=0,column=0)
entry_user.grid(row=0, column=1)
label_2.grid(row=1,column=0)
entry_pass.grid(row=1, column=1)
button_submit.grid(row=2, column=0)

# Runs the gui window
mainloop()
