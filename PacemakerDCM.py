# Multi-frame tkinter application v2.3
import tkinter as tk
from tkinter import ttk
import json
import os


'''                          DECLARATIONS
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
'''                               

'''database and pacemaker values store the username and password info, and pacemaker parameters, respectively'''
database = {}
pacemaker_values = {}
user_info = []

# Shift value is hardcoded here as a constant for use later in the encrypt/decrypt functions
SHIFT = 2

# Database dump location and upload location is going to be made a constant so it doesnt constantly need to be remade.
DUMP_LOCATION = os.getcwd() + '\database.json'
UPLOAD_LOCATION = os.getcwd() + '\SerialComm.json'

''' DATABASE '''
# Checks if the json file exists
if os.path.exists(DUMP_LOCATION):
    # if it exists, load in that database as the current database. Now it has memory
    with open(DUMP_LOCATION) as f:
        database = json.load(f)
else:
    # Otherwise initialize a new database. 
    database = {}

''' PACEMAKER VALUES '''
# Checks if the json file exists
if os.path.exists(UPLOAD_LOCATION):
    # if it exists, load in that database as the current database. Now it has memory
    with open(UPLOAD_LOCATION) as f:
        pacemaker_values = json.load(f)
else:
    # Otherwise initialize a new database. 
    pacemaker_values = {}

'''                           Functions
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
'''

class IO:
    """
    Simple class to do with file i/o and encryptiom/decryption. Consists of three class methods.
    """
    @classmethod
    def encrypt(cls, some_phrase):
        # Given string (user or pass), encrypts using the shift value
        # Used when STORING new user into database

        length = len(some_phrase)
        conv = ""
        for i in range(length):
            conv = conv + chr(ord(some_phrase[i]) + SHIFT)
        return conv

    @classmethod
    def decrypt(cls, some_phrase):
        # Given string (user or pass), decrypts using the shift value
        # Used when READING existing user from database

        length = len(some_phrase)
        conv = ""
        for i in range(length):
            conv = conv + chr(ord(some_phrase[i]) - SHIFT)
        return conv

    @classmethod
    def dump(cls, path, data_dict):
        """
        This function writes the current state of the user database to a json file. Having a local copy is very
        important, since this copy can be written to memory and accessed whether or not the DCM python script is running
        or not, and when the script reboots it remembers who has been registered.

        """
        # 'w+' mode is used to overwrite the previous database with the newest version.
        with open(path, 'w+') as dump_file:
            json.dump(data_dict, dump_file, indent=4, sort_keys=True)


def create_user(username, password, frame_class):
    """
    This function takes the desired username and password input into the two text boxes in the GUI and does some
    operations.
    It checks it against the existing database, which must be limited to 20 users, to see if it exists, and if not, will
    input it into the database.
    Also takes a frame_class
    """

    # Encrypt both the password and the username and update the database.
    en_user = IO.encrypt(str(username.get()))
    en_pass = IO.encrypt(str(password.get()))

    """
    Conditional will check our three conditions for adding to database: 
    less than 10 entries 
    and the user doesnt exist,
    and we have a valid password.
    """
    if len(database.items()) < 10 and database.get(en_user) is None and len(
            en_pass) > 0 and len(en_user) > 0:  # added no password case
        database.update({en_user: en_pass})
        IO.dump(DUMP_LOCATION, database)
        # We passed an object through (master in this case)
        frame_class.switch_frame(Menu)
    elif database.get(en_user):
        print("Username already exists.")
        return
    elif len(en_user) == 0:
        print("Please enter username")
    elif len(en_pass) == 0:
        print("Please enter password")
    else:
        print("Database is full")


def login_test(username, password, frame_class):
    """Function takes text-variable version of username and password, as well as frame class"""

    # Like in the create user function we will be using the encoded version
    en_user = IO.encrypt(str(username.get()))
    en_pass = IO.encrypt(str(password.get()))

    if (len(en_user) == 0) or (len(en_pass) == 0):
        print("Invalid credentials")
    elif database.get(en_user) == en_pass:
        frame_class.switch_frame(Menu)
    else:
        print("User does not exist")
    
def update_info(mode, low, up, AAmp, VAmp, APW, VPW, ASense, VSense, ARP, VRP):
    """
    Neatly updates dictionary with pacemaker parameters as per requirements in documentation.
    """

    # todo: typecast all values and change all inputs in all modes to just StringVars
    # todo: typecast and check in this fxn that the typecasted input is valid (i.e: not "5a5")
    # todo: use a try-except block to check that all parameters are good
    # todo: maybe put into the documentation that we may want to use a slider with accepted values for next implementation
    try:
        """
        This conditional checks that all the strings passed in as parameters convert properly. It is inside a try-except 
        to catch a faulty conversion
        """
        if int(mode) and float(low) and float(up) and float(AAmp) and float(VAmp) and float(APW) and float(VPW) and float(ASense) and float(VSense) and float(ARP) and float(VRP):
            pass

        pacemaker_values.update({"Mode": mode})
        if float(up) > 150:
            up = 150
        elif float(up) < 75:
            up = 75
        pacemaker_values.update({"Up_Limit": float(up)})
        if float(low) > up:
            low = 50
        elif float(low) < 50:
            low = 50
        pacemaker_values.update({"Low_Limit": float(low)})
        if float(AAmp) > 5:
            AAmp = 5
        elif float(AAmp) < 0.5:
            AAmp = 0.5
        pacemaker_values.update({"A_Amp": float(AAmp)})
        if float(VAmp) > 5:
            VAmp = 5
        elif float(VAmp) < 0.5:
            VAmp = 0.5
        pacemaker_values.update({"V_Amp": float(VAmp)})
        if float(APW) > 10:
            APW = 10
        elif float(APW) < 1:
            APW = 1
        pacemaker_values.update({"A_PW": float(APW)})
        if float(VPW) > 10:
            VPW = 10
        elif float(VPW) < 1:
            VPW = 1
        pacemaker_values.update({"V_PW": float(VPW)})
        if float(ASense) > 10:
            ASense = 10
        elif float(ASense) < 0.25:
            ASense = 0.25
        pacemaker_values.update({"A_Sense": float(ASense)})
        if float(VSense) > 10:
            VSense = 10
        elif float(VSense) < 0.25:
            VSense = 0.25
        pacemaker_values.update({"V_Sense": float(VSense)})
        if float(ARP) > 500:
            ARP = 500
        elif float(ARP) < 150:
            ARP = 150
        pacemaker_values.update({"ARP": float(ARP)})
        if float(VRP) > 500:
            VRP = 500
        elif float(VRP) < 150:
            VRP = 150
        pacemaker_values.update({"VRP": float(VRP)})
        IO.dump(UPLOAD_LOCATION, pacemaker_values)
        print("Pacemaker Values Updated Successfully")

    except ValueError as e:

        """
        In this situation, we have some invalid input, and it didn't convert properly. 
        
        """
        print("Invalid info! Re enter")
        print("Error printout here: " + str(e))

'''                  Tkinter Windows & Interface
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
'''


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
                  command=lambda: master.switch_frame(Login)).pack(padx=10, pady=10)
        tk.Button(self, text="Create User",
                  command=lambda: master.switch_frame(CreateUser)).pack(padx=10, pady=10)


class Login(tk.Frame):
    def __init__(self, master):
        v1 = tk.StringVar()
        v2 = tk.StringVar()
        login = 0
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Enter your credentials").pack(side="top", fill="x", pady=10)
        tk.Label(self, text="Enter Username").pack()
        tk.Entry(self, textvariable=v1).pack()
        tk.Label(self, text="Enter Password").pack()
        tk.Entry(self, textvariable=v2).pack(padx=5)
        tk.Button(self, text="Submit", command=lambda: login_test(v1, v2, master)).pack()
        tk.Button(self, text="Return to start page",
                  command=lambda: master.switch_frame(StartUp)).pack()
        if login == 1:
            master.switch_frame(Menu)


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
                  command=lambda: create_user(v1, v2, master)).pack()
        tk.Button(self, text="Return to start page",
                  command=lambda: master.switch_frame(StartUp)).pack()
        

class Menu(tk.Frame):
    def __init__(self, master):      
        tk.Frame.__init__(self, master)
        Low_Limit = tk.StringVar()
        Up_Limit = tk.StringVar()
        A_Amp = tk.StringVar()
        V_Amp = tk.StringVar()
        A_PW = tk.StringVar()
        V_PW = tk.StringVar()
        A_Sense = tk.StringVar()
        V_Sense = tk.StringVar()
        ARP = tk.StringVar()
        VRP = tk.StringVar()
        
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
        row5 = ttk.Frame(AOOTab)
        row5.pack()

        tk.Label(row1, text="Lower Rate Limit (ppm)").pack(side="left", padx=5, pady=5)
        tk.Entry(row1, textvariable=Low_Limit).pack(side="left", padx=5, pady=5)
        tk.Label(row2, text="Upper Rate Limit (ppm)").pack(side="left", padx=5, pady=5)
        tk.Entry(row2, textvariable=Up_Limit).pack(side="left", padx=5, pady=5)
        tk.Label(row3, text="Atrial Amplitude(V)").pack(side="left", padx=15, pady=5)
        tk.Entry(row3, textvariable=A_Amp).pack(side="left", padx=5, pady=5)
        tk.Label(row4, text="Atrial Pulse Width (ms)").pack(side="left", padx=6, pady=5)
        tk.Entry(row4, textvariable=A_PW).pack(side="left", padx=5, pady=5)
        tk.Button(row5, text="Submit", command=lambda:
                  update_info(1, Low_Limit.get(), Up_Limit.get(), A_Amp.get(), 0.5, A_PW.get(), 1, 0.25, 0.25, 150, 150)).pack(side="bottom", pady=5)

        # VOO
        row1 = ttk.Frame(VOOTab)
        row1.pack()
        row2 = ttk.Frame(VOOTab)
        row2.pack()
        row3 = ttk.Frame(VOOTab)
        row3.pack()
        row4 = ttk.Frame(VOOTab)
        row4.pack()
        row5 = ttk.Frame(VOOTab)
        row5.pack()
        tk.Label(row1, text="Lower Rate Limit (ppm)").pack(side="left", padx=22, pady=5)
        tk.Entry(row1, textvariable=Low_Limit).pack(side="left", padx=5, pady=5)
        tk.Label(row2, text="Upper Rate Limit (ppm)").pack(side="left", padx=22, pady=5)
        tk.Entry(row2, textvariable=Up_Limit).pack(side="left", padx=5, pady=5)
        tk.Label(row3, text="Ventricular Amplitude (V)").pack(side="left", padx=17, pady=5)
        tk.Entry(row3, textvariable=V_Amp).pack(side="left", padx=5, pady=5)
        tk.Label(row4, text="Ventricular Pulse Width (ms)").pack(side="left", padx=10, pady=5)
        tk.Entry(row4, textvariable=V_PW).pack(side="left", padx=5, pady=5)
        tk.Button(row5, text="Submit", command=lambda:
                  update_info(2, Low_Limit.get(), Up_Limit.get(), 0.5, V_Amp.get(), 1, V_PW.get(), 0.25, 0.25, 150, 150)).pack(side="bottom", pady=5)

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
        row7 = ttk.Frame(AAITab)
        row7.pack()
        tk.Label(row1, text="Lower Rate Limit (ppm)").pack(side="left", padx=5, pady=5)
        tk.Entry(row1, textvariable=Low_Limit).pack(side="left", padx=5, pady=5)
        tk.Label(row2, text="Upper Rate Limit (ppm)").pack(side="left", padx=5, pady=5)
        tk.Entry(row2, textvariable=Up_Limit).pack(side="left", padx=5, pady=5)
        tk.Label(row3, text="Atrial Amplitude (V)").pack(side="left", padx=15, pady=5)
        tk.Entry(row3, textvariable=A_Amp).pack(side="left", padx=5, pady=5)
        tk.Label(row4, text="Atrial Pulse Width (ms)").pack(side="left", padx=7, pady=5)
        tk.Entry(row4, textvariable=A_PW).pack(side="left", padx=5, pady=5)
        tk.Label(row5, text="Atrial Sensitivity (mV)").pack(side="left", padx=11, pady=5)
        tk.Entry(row5, textvariable=A_Sense).pack(side="left", padx=5, pady=5)
        tk.Label(row6, text="ARP (ms)").pack(side="left", padx=43, pady=5)
        tk.Entry(row6, textvariable=ARP).pack(side="left", padx=5, pady=5)
        tk.Button(row7, text="Submit", command=lambda:
                  update_info(3, Low_Limit.get(), Up_Limit.get(), A_Amp.get(), 0.5, A_PW.get(), 1, A_Sense.get(), 0.25, ARP.get(), 150)).pack(side="bottom", pady=5)
        
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
        row7 = ttk.Frame(VVITab)
        row7.pack()
        tk.Label(row1, text="Lower Rate Limit (ppm)").pack(side="left", padx=20, pady=5)
        tk.Entry(row1, textvariable=Low_Limit).pack(side="left", padx=5, pady=5)
        tk.Label(row2, text="Upper Rate Limit (ppm)").pack(side="left", padx=20, pady=5)
        tk.Entry(row2, textvariable=Up_Limit).pack(side="left", padx=5, pady=5)
        tk.Label(row3, text="Ventrical Amplitude (V)").pack(side="left", padx=21, pady=5)
        tk.Entry(row3, textvariable=V_Amp).pack(side="left", padx=5, pady=5)
        tk.Label(row4, text="Ventricular Pulse Width (ms)").pack(side="left", padx=7, pady=5)
        tk.Entry(row4, textvariable=V_PW).pack(side="left", padx=5, pady=5)
        tk.Label(row5, text="Ventricular Sensitivity (mV)").pack(side="left", padx=11, pady=5)
        tk.Entry(row5, textvariable=V_Sense).pack(side="left", padx=5, pady=5)
        tk.Label(row6, text="VRP (ms)").pack(side="left", padx=57, pady=5)
        tk.Entry(row6, textvariable=VRP).pack(side="left", padx=5, pady=5)
        tk.Button(row7, text="Submit", command=lambda:
                  update_info(4, Low_Limit.get(), Up_Limit.get(), 0.5, V_Amp.get(), 1, A_PW.get(), 0.25, V_Sense.get(), 150, VRP.get())).pack(side="bottom", pady=5)
        

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
    
