from tkinter import *
import json
import os
# This database dictionary will store user:password pairs (encrypted in some way)
database = {}
main_gui = Tk()
user_info = []
# Shift value is hardcoded here as a constant for use later in the encrypt/decrypt functions
SHIFT = 2
# Database dump location is going to be made a constant so it doesnt constantly need to be remade.
DUMP_LOCATION = os.getcwd() + '\database.json'
print(DUMP_LOCATION)

# Checks if the json file exists
if os.path.exists(DUMP_LOCATION):
    # if it exists, load in that database as the current database. Now it has memory
    with open(DUMP_LOCATION) as f:
        database = json.load(f)
else:
    # Otherwise initialize a new database. 
    database = {}
# The program structure might not be the neatest rn
v1 = StringVar()
label_1 = Label(main_gui, text="Please enter your username:")
entry_user = Entry(main_gui, textvariable=v1)


v2 = StringVar()
label_2 = Label(main_gui, text="Please enter your password:")
entry_pass = Entry(main_gui, textvariable=v2)

def encrypt(some_phrase):
    # Given string (user or pass), encrypts using the shift value
    # Used when STORING new user into database

    length = len(some_phrase)
    Conv = ""
    for i in range(length):
        Conv = Conv + chr(ord(some_phrase[i])+SHIFT)
    return Conv

def decrypt(some_phrase):
    # Given string (user or pass), decrypts using the shift value
    # Used when READING existing user from database

    length = len(some_phrase)
    Conv = ""
    for i in range(length):
        Conv = Conv + chr(ord(some_phrase[i])-SHIFT)
    return Conv

def dump():
    """
    This function writes the current state of the user database to a json file. Having a local copy is very important
    since this copy can be written to memory and accessed whether or not the DCM python script is running or not.

    """
    # 'w+' mode is used to overwrite the previous database with the newest version.
    with open(DUMP_LOCATION, 'w+') as dump_file:
        json.dump(database, dump_file, indent=4, sort_keys=True)


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
    # Encrypt both the password and the username and update the database.
    en_user = encrypt(username)             #####JOHN
    en_pass = encrypt(password)             #####JOHN
    if len(database.items()) < 10 and database.get(en_user) is None and len(password) > 0:     ###added no password case
        database.update({en_user: en_pass})
        print(database)
        dump()
    elif database.get(en_user):
        print("Username already exists.")
        return
    elif len(password) == 0:            ###JOHN
        print("Please enter password")  ###JOHN
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
