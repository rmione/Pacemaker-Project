from tkinter import *

# This database dictionary will store user:password pairs (encrypted in some way)
database = {}
main_gui = Tk()
user_info = []

# The program structure might not be the neatest rn
v1 = StringVar()
label_1 = Label(main_gui, text="Please enter your username:")
entry_user = Entry(main_gui, textvariable=v1)


v2 = StringVar()
label_2 = Label(main_gui, text="Please enter your password:")
entry_pass = Entry(main_gui, textvariable=v2)

# Text file has a space between username and password
# Text file needs \n after last line, so when writing to file, make sure to put \n after each password
#   or else you will get errors/not get last character of last password
def read_users(textfile,user_info):
    for line in textfile:
        for i in range(0, len(line)-1):
            if (line[i] == " "):
                user = line[0:i]
                password = line[i+1:len(line)-1]
        user_info.append(user)
        user_info.append(password)
    return 1

def encrypt(some_phrase):
    # some encryption method... we will figure it out
    phrase = str(input("Please enter a phrase: "))  #####
    shift = 2   #####
    length = len(some_phrase)
    Conv = ""
    for i in range(length):
        Conv = Conv + chr(ord(phrase[i])+shift)
    return Conv

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
textfile = open("user_data.txt", "r")
mainloop()
read_users(textfile,user_info)
print(user_info)
