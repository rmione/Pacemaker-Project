
import tkinter as tk
from tkinter import ttk
import json
import os

# main_gui = Tk()

# Shift value is hardcoded here as a constant for use later in the encrypt/decrypt functions
SHIFT = 2
# Database dump location is going to be made a constant so it doesnt constantly need to be remade.
DUMP_LOCATION = os.getcwd() + '\database.json'

if os.path.exists(DUMP_LOCATION):
    # if it exists, load in that database as the current database. Now it has memory
    with open(DUMP_LOCATION) as f:
        database = json.load(f)
else:
    # Otherwise initialize a new database.
    database = {}

def encrypt(some_phrase):
    # Given string (user or pass), encrypts using the shift value
    # Used when STORING new user into database

    length = len(some_phrase)
    Conv = ""
    for i in range(length):
        Conv = Conv + chr(ord(some_phrase[i]) + SHIFT)
    return Conv

def decrypt(ome_phrase):
    # Given string (user or pass), decrypts using the shift value
    # Used when READING existing user from database

    length = len(some_phrase)
    Conv = ""
    for i in range(length):
        Conv = Conv + chr(ord(some_phrase[i]) - SHIFT)
    return Conv

def process_data(username, password, object):

    """
    This function takes the desired username and password input into the two text boxes in the GUI and does some
    operations.
    It checks it against the existing database, which must be limited to 20 users, to see if it exists, and if not, will
    input it into the database.



    """
    # Conditional will check our two conditions for adding to database: less than 20 entries and the user doesnt exist.

    # Encrypt both the password and the username and update the database.
    en_user = encrypt(str(username.get()))
    en_pass = encrypt(str(password.get()))
    if len(database.items()) < 10 and database.get(en_user) is None and len(
            en_pass) > 0:  # added no password case
        database.update({en_user: en_pass})
        print(database)
        dump()
        # We passed an object through (master in this case)
        object.switch_frame(Menu)
    elif database.get(en_user):
        print("Username already exists.")
        return
    elif len(en_pass) == 0:
        print("Please enter password")
    else:
        print("Database is full")


def dump():
    """
    This function writes the current state of the user database to a json file. Having a local copy is very important
    since this copy can be written to memory and accessed whether or not the DCM python script is running or not.

    """
    # 'w+' mode is used to overwrite the previous database with the newest version.
    with open(DUMP_LOCATION, 'w+') as dump_file:
        json.dump(database, dump_file, indent=4, sort_keys=True)




class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartUp)

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


class StartUp(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Button(self, text="Login",
                  command=lambda: master.switch_frame(Login)).pack()
        tk.Button(self, text="Create User",
                  command=lambda: master.switch_frame(CreateUser)).pack()


class Login(tk.Frame):
    def __init__(self, master):
        v1 = tk.StringVar()
        v2 = tk.StringVar()
        tk.Frame.__init__(self, master)
        # tk.Label(self, text="Enter your credentials").pack(side="top", fill="x", pady=10)
        tk.Label(self, text="Enter Username").pack()
        tk.Entry(self, textvariable=v1).pack()
        tk.Label(self, text="Enter Password").pack()
        tk.Entry(self, textvariable=v2).pack(padx=5)
        tk.Button(self, text="Submit").pack()
        tk.Button(self, text="Return to start page",
                  command=lambda: master.switch_frame(StartUp)).pack()


class CreateUser(tk.Frame):
    def __init__(self, master):
        v1 = tk.StringVar()
        v2 = tk.StringVar()
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Create a new user").pack(side="top", fill="x", padx=40, pady=10)
        tk.Label(self, text="Enter Username").pack()
        tk.Entry(self, textvariable=v1).pack()
        tk.Label(self, text="Enter Password").pack()
        tk.Entry(self, textvariable=v2).pack()
        tk.Button(self, text="Create",
                  command=lambda: process_data(v1, v2, master)).pack()
        tk.Button(self, text="Return to start page",
                  command=lambda: master.switch_frame(StartUp)).pack()


class Menu(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        mode = tk.IntVar()
        mode = 0
        Low_Limit = tk.IntVar()
        Up_Limit = tk.IntVar()
        A_Amp = tk.IntVar()
        V_Amp = tk.IntVar()
        A_PW = tk.IntVar()
        V_PW = tk.IntVar()
        A_Sense = tk.IntVar()
        V_Sense = tk.IntVar()
        ARP = tk.IntVar()
        VRP = tk.IntVar()

        tabControl = ttk.Notebook(self)
        AOOTab = ttk.Frame(tabControl)
        VOOTab = ttk.Frame(tabControl)
        AAITab = ttk.Frame(tabControl)
        VVITab = ttk.Frame(tabControl)
        tabControl.add(AOOTab, text='AOO')
        tabControl.add(VOOTab, text='VOO')
        tabControl.add(AAITab, text='AAI')
        tabControl.add(VVITab, text='VVI')
        tabControl.pack(expand=1, side="top")

        # AOO
        row1 = ttk.Frame(AOOTab)
        row1.pack()
        row2 = ttk.Frame(AOOTab)
        row2.pack()
        row3 = ttk.Frame(AOOTab)
        row3.pack()
        row4 = ttk.Frame(AOOTab)
        row4.pack()
        tk.Label(row1, text="Lower Rate Limit").pack(side="left", padx=5, pady=5)
        tk.Entry(row1, textvariable=Low_Limit).pack(side="left", padx=5, pady=5)
        tk.Label(row2, text="Upper Rate Limit").pack(side="left", padx=5, pady=5)
        tk.Entry(row2, textvariable=Up_Limit).pack(side="left", padx=5, pady=5)
        tk.Label(row3, text="Atrial Amplitude").pack(side="left", padx=5, pady=5)
        tk.Entry(row3, textvariable=A_Amp).pack(side="left", padx=5, pady=5)
        tk.Label(row4, text="Atrial Pulse Width").pack(side="left", padx=2, pady=5)
        tk.Entry(row4, textvariable=A_PW).pack(side="left", padx=5, pady=5)

        # VOO
        row1 = ttk.Frame(VOOTab)
        row1.pack()
        row2 = ttk.Frame(VOOTab)
        row2.pack()
        row3 = ttk.Frame(VOOTab)
        row3.pack()
        row4 = ttk.Frame(VOOTab)
        row4.pack()
        tk.Label(row1, text="Lower Rate Limit").pack(side="left", padx=22, pady=5)
        tk.Entry(row1, textvariable=Low_Limit).pack(side="left", padx=0, pady=5)
        tk.Label(row2, text="Upper Rate Limit").pack(side="left", padx=22, pady=5)
        tk.Entry(row2, textvariable=Up_Limit).pack(side="left", padx=0, pady=5)
        tk.Label(row3, text="Ventricular Amplitude").pack(side="left", padx=8, pady=5)
        tk.Entry(row3, textvariable=V_Amp).pack(side="left", padx=5, pady=5)
        tk.Label(row4, text="Ventricular Pulse Width").pack(side="left", padx=5, pady=5)
        tk.Entry(row4, textvariable=V_PW).pack(side="left", padx=5, pady=5)

        # AAI
        row1 = ttk.Frame(AAITab)
        row1.pack()
        row2 = ttk.Frame(AAITab)
        row2.pack()
        row3 = ttk.Frame(AAITab)
        row3.pack()
        row4 = ttk.Frame(AAITab)
        row4.pack()
        row5 = ttk.Frame(AAITab)
        row5.pack()
        row6 = ttk.Frame(AAITab)
        row6.pack()
        tk.Label(row1, text="Lower Rate Limit").pack(side="left", padx=5, pady=5)
        tk.Entry(row1, textvariable=Low_Limit).pack(side="left", padx=5, pady=5)
        tk.Label(row2, text="Upper Rate Limit").pack(side="left", padx=5, pady=5)
        tk.Entry(row2, textvariable=Up_Limit).pack(side="left", padx=5, pady=5)
        tk.Label(row3, text="Atrial Amplitude").pack(side="left", padx=5, pady=5)
        tk.Entry(row3, textvariable=A_Amp).pack(side="left", padx=5, pady=5)
        tk.Label(row4, text="Atrial Pulse Width").pack(side="left", padx=2, pady=5)
        tk.Entry(row4, textvariable=A_PW).pack(side="left", padx=5, pady=5)
        tk.Label(row5, text="Atrial Sensitivity").pack(side="left", padx=6, pady=5)
        tk.Entry(row5, textvariable=A_Sense).pack(side="left", padx=5, pady=5)
        tk.Label(row6, text="ARP").pack(side="left", padx=37, pady=5)
        tk.Entry(row6, textvariable=ARP).pack(side="left", padx=5, pady=5)

        # VVI
        row1 = ttk.Frame(VVITab)
        row1.pack()
        row2 = ttk.Frame(VVITab)
        row2.pack()
        row3 = ttk.Frame(VVITab)
        row3.pack()
        row4 = ttk.Frame(VVITab)
        row4.pack()
        row5 = ttk.Frame(VVITab)
        row5.pack()
        row6 = ttk.Frame(VVITab)
        row6.pack()
        tk.Label(row1, text="Lower Rate Limit").pack(side="left", padx=20, pady=5)
        tk.Entry(row1, textvariable=Low_Limit).pack(side="left", padx=5, pady=5)
        tk.Label(row2, text="Upper Rate Limit").pack(side="left", padx=20, pady=5)
        tk.Entry(row2, textvariable=Up_Limit).pack(side="left", padx=5, pady=5)
        tk.Label(row3, text="Ventrical Amplitude").pack(side="left", padx=11, pady=5)
        tk.Entry(row3, textvariable=A_Amp).pack(side="left", padx=5, pady=5)
        tk.Label(row4, text="Ventricular Pulse Width").pack(side="left", padx=2, pady=5)
        tk.Entry(row4, textvariable=A_PW).pack(side="left", padx=5, pady=5)
        tk.Label(row5, text="Ventricular Sensitivity").pack(side="left", padx=6, pady=5)
        tk.Entry(row5, textvariable=A_Sense).pack(side="left", padx=5, pady=5)
        tk.Label(row6, text="VRP").pack(side="left", padx=52, pady=5)
        tk.Entry(row6, textvariable=ARP).pack(side="left", padx=5, pady=5)


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
