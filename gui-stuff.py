from tkinter import *

# This database dictionary will store user:password pairs (encrypted in some way)
database = {}
main_gui = Tk()


def encrypt(some_phrase):
    # some encryption method... we will figure it out.

    return some_phrase


def process_data(username, password):

    """
    This function takes the desired username and password input into the two text boxes in the GUI and does some
    operations.
    It checks it against the existing database, which must be limited to 20 users, to see if it exists, and if not, will
    input it into the database.



    """

    if len(database.items()) < 20 and database.get(username) is None:
        # Encrypt both the password and the username and update the database.
        print(username.get())
        print(password.get())
        database.update({encrypt(username.get()): encrypt(password.get())})
        print("hello?")
        print(database)


    else:
        print("The database is full.")
        return




label_1 = Label(main_gui, text="Please enter your username:")
entry_user = Entry(main_gui)

label_2 = Label(main_gui, text="Please enter your password:")
entry_pass = Entry(main_gui)

button_submit = Button(main_gui, text="Submit", command=process_data(entry_user, entry_pass))

label_1.grid(row=0,column=0)
entry_user.grid(row=0, column=1)
label_2.grid(row=1,column=0)
entry_pass.grid(row=1, column=1)
button_submit.grid(row=2, column=0)

# Runs the gui window
main_gui.mainloop()
