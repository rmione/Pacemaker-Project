import tkinter as tk
from tkinter import ttk
import json
import os
from tkinter import messagebox
from MiscFunctions import *

UserID = "UserID"

''' ------------------------------------------------------ '''
def create_user(username, password, frame_class):
    """
    This function takes the desired username and password input into the two text boxes in the GUI and does some
    operations.
    It checks it against the existing database, which must be limited to 20 users, to see if it exists, and if not, will
    input it into the database.
    Also takes a frame_class
    """

    global UserID
    # Encrypt both the password and the username and update the database.
    en_user = IO.encrypt(str(username.get()))
    UserID = str(username.get())
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
        messagebox.showinfo("Username already exists.", "Please login with this user or attempt to create a new one.")
        return
    elif len(en_user) == 0:
        print("Please enter username")

        messagebox.showinfo("Please enter username", "Enter a valid username.")
    elif len(en_pass) == 0:
        print("Please enter password")
    else:
        print("Database is full")
        messagebox.showinfo("Database is full", "The database cannot accept any more users.")


def login_test(username, password, frame_class):
    """Function takes text-variable version of username and password, as well as frame class"""

    global UserID
    # Like in the create user function we will be using the encoded version
    en_user = IO.encrypt(str(username.get()))
    UserID = str(username.get())
    en_pass = IO.encrypt(str(password.get()))

    if (len(en_user) == 0) or (len(en_pass) == 0):
        print("Invalid credentials")
        messagebox.showinfo("Invalid credentials", "Either your username or password are invalid, try again.")
    elif database.get(en_user) == en_pass:
        frame_class.switch_frame(Menu)
    else:
        print("User does not exist")
        messagebox.showinfo("User does not exist", "This user does not exist in the database, try again.")


''' ============================================================= '''

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
        master.resizable(False, False)
        tk.Label(self, text="Welcome").pack()
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
        DOOTab = ttk.Frame(tabControl)
        AOORTab = ttk.Frame(tabControl)
        VOORTab = ttk.Frame(tabControl)
        AAIRTab = ttk.Frame(tabControl)
        VVIRTab = ttk.Frame(tabControl)
        DOORTab = ttk.Frame(tabControl)
        tabControl.add(AOOTab, text='AOO')
        tabControl.add(VOOTab, text='VOO')
        tabControl.add(AAITab, text='AAI')
        tabControl.add(VVITab, text='VVI')
        tabControl.add(DOOTab, text='DOO')
        tabControl.add(AOORTab, text='AOOR')
        tabControl.add(VOORTab, text='VOOR')
        tabControl.add(AAIRTab, text='AAIR')
        tabControl.add(VVIRTab, text='VVIR')
        tabControl.add(DOORTab, text='DOOR')
        
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
        row6 = ttk.Frame(AOOTab)
        row6.pack()
        tk.Label(row1, text="Lower Rate Limit (ppm)").pack(side="left", padx=5, pady=5)
        AOOLRL = tk.Scale(row1, from_=30, to=175, length=600, tickinterval=15, orient=tk.HORIZONTAL)
        AOOLRL.pack(side="left", padx=5, pady=5)
        tk.Label(row2, text="Upper Rate Limit (ppm)").pack(side="left", padx=5, pady=5)
        AOOURL = tk.Scale(row2, from_=50, to=175, length=600, tickinterval=15, orient=tk.HORIZONTAL)
        AOOURL.pack(side="left", padx=5, pady=5)
        tk.Label(row3, text="Atrial Amplitude(V)").pack(side="left", padx=15, pady=5)
        AOOAA = tk.Scale(row3, from_=0.5, to=5, length=600, tickinterval=0.5, orient=tk.HORIZONTAL)
        AOOAA.pack(side="left", padx=5, pady=5)
        tk.Label(row4, text="Atrial Pulse Width (ms)").pack(side="left", padx=6, pady=5)
        AOOPW = tk.Scale(row4, from_=1, to=10, length=600, tickinterval=1, orient=tk.HORIZONTAL)
        AOOPW.pack(side="left", padx=5, pady=5)
        tk.Button(row5, text="Submit", command=lambda:
                  update_info(1, AOOLRL.get(), AOOURL.get(), AOOAA.get(), 0, AOOPW.get(), 0, 0, 0, 0, 0, 0, 0, 0, UserID)).pack(side="bottom", pady=5)
        tk.Label(row6, text=UserID).pack(side="left", padx=0, pady=5)
        tk.Label(row6, text=' ').pack(side="left", padx=325, pady=5)

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
        row6 = ttk.Frame(VOOTab)
        row6.pack()
        tk.Label(row1, text="Lower Rate Limit (ppm)").pack(side="left", padx=22, pady=5)
        VOOLRL = tk.Scale(row1, from_=30, to=175, length=600, tickinterval=15, orient=tk.HORIZONTAL)
        VOOLRL.pack(side="left", padx=5, pady=5)
        tk.Label(row2, text="Upper Rate Limit (ppm)").pack(side="left", padx=22, pady=5)
        VOOURL = tk.Scale(row2, from_=50, to=175, length=600, tickinterval=15, orient=tk.HORIZONTAL)
        VOOURL.pack(side="left", padx=5, pady=5)
        tk.Label(row3, text="Ventricular Amplitude (V)").pack(side="left", padx=17, pady=5)
        VOOVA = tk.Scale(row3, from_=0.5, to=5, length=600, tickinterval=0.5, orient=tk.HORIZONTAL)
        VOOVA.pack(side="left", padx=5, pady=5)
        tk.Label(row4, text="Ventricular Pulse Width (ms)").pack(side="left", padx=10, pady=5)
        VOOPW = tk.Scale(row4, from_=1, to=10, length=600, tickinterval=1, orient=tk.HORIZONTAL)
        VOOPW.pack(side="left", padx=5, pady=5)
        tk.Button(row5, text="Submit", command=lambda:
                  update_info(2, VOOLRL.get(), VOOURL.get(), 0, VOOVA.get(), 1, VOOPW.get(), 0, 0, 0, 0, 0, 0, 0, UserID)).pack(side="bottom", pady=5)
        tk.Label(row6, text=UserID).pack(side="left", padx=0, pady=5)
        tk.Label(row6, text=' ').pack(side="left", padx=325, pady=5)

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
        row8 = ttk.Frame(AAITab)
        row8.pack()
        tk.Label(row1, text="Lower Rate Limit (ppm)").pack(side="left", padx=5, pady=5)
        AAILRL = tk.Scale(row1, from_=30, to=175, length=600, tickinterval=15, orient=tk.HORIZONTAL)
        AAILRL.pack(side="left", padx=5, pady=5)
        tk.Label(row2, text="Upper Rate Limit (ppm)").pack(side="left", padx=5, pady=5)
        AAIURL = tk.Scale(row2, from_=50, to=175, length=600, tickinterval=15, orient=tk.HORIZONTAL)
        AAIURL.pack(side="left", padx=5, pady=5)
        tk.Label(row3, text="Atrial Amplitude (V)").pack(side="left", padx=15, pady=5)
        AAIAA = tk.Scale(row3, from_=0.5, to=5, length=600, tickinterval=0.5, orient=tk.HORIZONTAL)
        AAIAA.pack(side="left", padx=5, pady=5)
        tk.Label(row4, text="Atrial Pulse Width (ms)").pack(side="left", padx=7, pady=5)
        AAIPW = tk.Scale(row4, from_=1, to=10, length=600, tickinterval=1, orient=tk.HORIZONTAL)
        AAIPW.pack(side="left", padx=5, pady=5)
        tk.Label(row5, text="Atrial Sensitivity (mV)").pack(side="left", padx=11, pady=5)
        AAIAS = tk.Scale(row5, from_=1, to=10, length=600, tickinterval=1, orient=tk.HORIZONTAL)
        AAIAS.pack(side="left", padx=5, pady=5)
        tk.Label(row6, text="ARP (ms)").pack(side="left", padx=43, pady=5)
        AAIARP = tk.Scale(row6, from_=150, to=500, length=600, tickinterval=20, orient=tk.HORIZONTAL)
        AAIARP.pack(side="left", padx=5, pady=5)
        tk.Button(row7, text="Submit", command=lambda:
                  update_info(3, AAILRL.get(), AAIURL.get(), AAIAA.get(), 0, AAIPW.get(), 0, AAIAS.get(), 0, AAIARP.get(), 0, 0, 0, 0, UserID)).pack(side="bottom", pady=5)
        tk.Label(row8, text=UserID).pack(side="left", padx=0, pady=5)
        tk.Label(row8, text=' ').pack(side="left", padx=325, pady=5)
        
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
        row8 = ttk.Frame(VVITab)
        row8.pack()
        tk.Label(row1, text="Lower Rate Limit (ppm)").pack(side="left", padx=20, pady=5)
        VVILRL = tk.Scale(row1, from_=30, to=175, length=600, tickinterval=15, orient=tk.HORIZONTAL)
        VVILRL.pack(side="left", padx=5, pady=5)
        tk.Label(row2, text="Upper Rate Limit (ppm)").pack(side="left", padx=20, pady=5)
        VVIURL = tk.Scale(row2, from_=50, to=175, length=600, tickinterval=15, orient=tk.HORIZONTAL)
        VVIURL.pack(side="left", padx=5, pady=5)
        tk.Label(row3, text="Ventrical Amplitude (V)").pack(side="left", padx=21, pady=5)
        VVIVA = tk.Scale(row3, from_=0.5, to=5, length=600, tickinterval=0.5, orient=tk.HORIZONTAL)
        VVIVA.pack(side="left", padx=5, pady=5)
        tk.Label(row4, text="Ventricular Pulse Width (ms)").pack(side="left", padx=7, pady=5)
        VVIPW = tk.Scale(row4, from_=1, to=10, length=600, tickinterval=1, orient=tk.HORIZONTAL)
        VVIPW.pack(side="left", padx=5, pady=5)
        tk.Label(row5, text="Ventricular Sensitivity (mV)").pack(side="left", padx=11, pady=5)
        VVIVS = tk.Scale(row5, from_=1, to=10, length=600, tickinterval=1, orient=tk.HORIZONTAL)
        VVIVS.pack(side="left", padx=5, pady=5)
        tk.Label(row6, text="VRP (ms)").pack(side="left", padx=57, pady=5)
        VVIVRP = tk.Scale(row6, from_=150, to=500, length=600, tickinterval=20, orient=tk.HORIZONTAL)
        VVIVRP.pack(side="left", padx=5, pady=5)
        tk.Button(row7, text="Submit", command=lambda:
                  update_info(4, VVILRL.get(), VVIURL.get(), 0, VVIVA.get(), 0, VVIPW.get(), 0, VVIVS.get(), 0, VVIVRP.get(), 0, 0, 0, UserID)).pack(side="bottom", pady=5)
        tk.Label(row8, text=UserID).pack(side="left", padx=0, pady=5)
        tk.Label(row8, text=' ').pack(side="left", padx=325, pady=5)


        # DOO
        row1 = ttk.Frame(DOOTab)
        row1.pack()
        row2 = ttk.Frame(DOOTab)
        row2.pack()
        row3 = ttk.Frame(DOOTab)
        row3.pack()
        row4 = ttk.Frame(DOOTab)
        row4.pack()
        row5 = ttk.Frame(DOOTab)
        row5.pack()
        row6 = ttk.Frame(DOOTab)
        row6.pack()
        row7 = ttk.Frame(DOOTab)
        row7.pack()
        row8 = ttk.Frame(DOOTab)
        row8.pack()
        tk.Label(row1, text="Lower Rate Limit (ppm)").pack(side="left", padx=20, pady=5)
        DOOLRL = tk.Scale(row1, from_=30, to=175, length=600, tickinterval=15, orient=tk.HORIZONTAL)
        DOOLRL.pack(side="right", padx=5, pady=5)
        tk.Label(row2, text="Upper Rate Limit (ppm)").pack(side="left", padx=20, pady=5)
        DOOURL = tk.Scale(row2, from_=50, to=175, length=600, tickinterval=15, orient=tk.HORIZONTAL)
        DOOURL.pack(side="right", padx=5, pady=5)
        tk.Label(row3, text="Atrial Amplitude (V)").pack(side="left", padx=30, pady=5)
        DOOAA = tk.Scale(row3, from_=0.5, to=5, length=600, tickinterval=0.5, orient=tk.HORIZONTAL)
        DOOAA.pack(side="right", padx=5, pady=5)
        tk.Label(row4, text="Ventricular Amplitude (V)").pack(side="left", padx=15, pady=5)
        DOOVA = tk.Scale(row4, from_=0.5, to=5, length=600, tickinterval=0.5, orient=tk.HORIZONTAL)
        DOOVA.pack(side="right", padx=5, pady=5)
        tk.Label(row5, text="Atrial Pulse Width (ms)").pack(side="left", padx=21, pady=5)
        DOOAPW = tk.Scale(row5, from_=1, to=10, length=600, tickinterval=1, orient=tk.HORIZONTAL)
        DOOAPW.pack(side="right", padx=5, pady=5)
        tk.Label(row6, text="Ventricular Pulse Width (ms)").pack(side="left", padx=7, pady=5)
        DOOVPW = tk.Scale(row6, from_=1, to=10, length=600, tickinterval=1, orient=tk.HORIZONTAL)
        DOOVPW.pack(side="right", padx=5, pady=5)
        tk.Button(row7, text="Submit", command=lambda:
                  update_info(5, DOOLRL.get(), DOOURL.get(), DOOAA.get(), DOOVA.get(), DOOAPW.get(), DOOVPW.get(), 0, 0, 0, 0, 0, 0, 0, UserID)).pack(side="bottom", pady=5)
        tk.Label(row8, text=UserID).pack(side="left", padx=0, pady=5)
        tk.Label(row8, text=' ').pack(side="left", padx=325, pady=5)


        # AOOR
        row1 = ttk.Frame(AOORTab)
        row1.pack()
        row2 = ttk.Frame(AOORTab)
        row2.pack()
        row3 = ttk.Frame(AOORTab)
        row3.pack()
        row4 = ttk.Frame(AOORTab)
        row4.pack()
        row5 = ttk.Frame(AOORTab)
        row5.pack()
        row6 = ttk.Frame(AOORTab)
        row6.pack()
        row7 = ttk.Frame(AOORTab)
        row7.pack()
        tk.Label(row1, text="Lower Rate Limit (ppm)").pack(side="left", padx=20, pady=5)
        AOORLRL = tk.Scale(row1, from_=30, to=175, length=600, tickinterval=15, orient=tk.HORIZONTAL)
        AOORLRL.pack(side="right", padx=5, pady=5)
        tk.Label(row2, text="Upper Rate Limit (ppm)").pack(side="left", padx=20, pady=5)
        AOORURL = tk.Scale(row2, from_=50, to=175, length=600, tickinterval=15, orient=tk.HORIZONTAL)
        AOORURL.pack(side="right", padx=5, pady=5)
        tk.Label(row3, text="Max Sensor Rate (ppm)").pack(side="left", padx=20, pady=5)
        AOORMSR = tk.Scale(row3, from_=50, to=175, length=600, tickinterval=10, orient=tk.HORIZONTAL)
        AOORMSR.pack(side="right", padx=5, pady=5)
        tk.Label(row4, text="Atrial Amplitude (V)").pack(side="left", padx=30, pady=5)
        AOORAA = tk.Scale(row4, from_=0.5, to=5, length=600, tickinterval=0.5, orient=tk.HORIZONTAL)
        AOORAA.pack(side="right", padx=5, pady=5)
        tk.Label(row5, text="Atrial Pulse Width (ms)").pack(side="left", padx=23, pady=5)
        AOORAPW = tk.Scale(row5, from_=1, to=10, length=600, tickinterval=1, orient=tk.HORIZONTAL)
        AOORAPW.pack(side="right", padx=5, pady=5)
        tk.Button(row6, text="Submit", command=lambda:
                  update_info(6, AOORLRL.get(), AOORURL.get(), AOORAA.get(), 0, AOORAPW.get(), 0, 0, 0, 0, 0, AOORMSR.get(), 0, 0, UserID)).pack(side="bottom", pady=5)
        tk.Label(row7, text=UserID).pack(side="left", padx=0, pady=5)
        tk.Label(row7, text=' ').pack(side="left", padx=325, pady=5)


        # VOOR
        row1 = ttk.Frame(VOORTab)
        row1.pack()
        row2 = ttk.Frame(VOORTab)
        row2.pack()
        row3 = ttk.Frame(VOORTab)
        row3.pack()
        row4 = ttk.Frame(VOORTab)
        row4.pack()
        row5 = ttk.Frame(VOORTab)
        row5.pack()
        row6 = ttk.Frame(VOORTab)
        row6.pack()
        row7 = ttk.Frame(VOORTab)
        row7.pack()
        tk.Label(row1, text="Lower Rate Limit (ppm)").pack(side="left", padx=20, pady=5)
        VOORLRL = tk.Scale(row1, from_=30, to=175, length=600, tickinterval=15, orient=tk.HORIZONTAL)
        VOORLRL.pack(side="right", padx=5, pady=5)
        tk.Label(row2, text="Upper Rate Limit (ppm)").pack(side="left", padx=20, pady=5)
        VOORURL = tk.Scale(row2, from_=50, to=175, length=600, tickinterval=15, orient=tk.HORIZONTAL)
        VOORURL.pack(side="right", padx=5, pady=5)
        tk.Label(row3, text="Max Sensor Rate (ppm)").pack(side="left", padx=20, pady=5)
        VOORMSR = tk.Scale(row3, from_=50, to=175, length=600, tickinterval=10, orient=tk.HORIZONTAL)
        VOORMSR.pack(side="right", padx=5, pady=5)
        tk.Label(row4, text="Ventricular Amplitude (V)").pack(side="left", padx=15, pady=5)
        VOORVA = tk.Scale(row4, from_=0.5, to=5, length=600, tickinterval=0.5, orient=tk.HORIZONTAL)
        VOORVA.pack(side="right", padx=5, pady=5)
        tk.Label(row5, text="Ventricular Pulse Width (ms)").pack(side="left", padx=8, pady=5)
        VOORVPW = tk.Scale(row5, from_=1, to=10, length=600, tickinterval=1, orient=tk.HORIZONTAL)
        VOORVPW.pack(side="right", padx=5, pady=5)
        tk.Button(row6, text="Submit", command=lambda:
                  update_info(7, VOORLRL.get(), VOORURL.get(), 0, VOORVA.get(), 0, VOORVPW.get(), 0, 0, 0, 0, VOORMSR.get(), 0, 0, UserID)).pack(side="bottom", pady=5)
        tk.Label(row7, text=UserID).pack(side="left", padx=0, pady=5)
        tk.Label(row7, text=' ').pack(side="left", padx=325, pady=5)


        # AAIR
        row1 = ttk.Frame(AAIRTab)
        row1.pack()
        row2 = ttk.Frame(AAIRTab)
        row2.pack()
        row3 = ttk.Frame(AAIRTab)
        row3.pack()
        row4 = ttk.Frame(AAIRTab)
        row4.pack()
        row5 = ttk.Frame(AAIRTab)
        row5.pack()
        row6 = ttk.Frame(AAIRTab)
        row6.pack()
        row7 = ttk.Frame(AAIRTab)
        row7.pack()
        row8 = ttk.Frame(AAIRTab)
        row8.pack()
        row9 = ttk.Frame(AAIRTab)
        row9.pack()
        row10 = ttk.Frame(AAIRTab)
        row10.pack()
        tk.Label(row1, text="Lower Rate Limit (ppm)").pack(side="left", padx=20, pady=5)
        AAIRLRL = tk.Scale(row1, from_=30, to=175, length=600, tickinterval=15, orient=tk.HORIZONTAL)
        AAIRLRL.pack(side="right", padx=5, pady=5)
        tk.Label(row2, text="Upper Rate Limit (ppm)").pack(side="left", padx=20, pady=5)
        AAIRURL = tk.Scale(row2, from_=50, to=175, length=600, tickinterval=15, orient=tk.HORIZONTAL)
        AAIRURL.pack(side="right", padx=5, pady=5)
        tk.Label(row3, text="Max Sensor Rate (ppm)").pack(side="left", padx=20, pady=5)
        AAIRMSR = tk.Scale(row3, from_=50, to=175, length=600, tickinterval=10, orient=tk.HORIZONTAL)
        AAIRMSR.pack(side="right", padx=5, pady=5)
        tk.Label(row4, text="Atrial Amplitude (V)").pack(side="left", padx=30, pady=5)
        AAIRAA = tk.Scale(row4, from_=0.5, to=5, length=600, tickinterval=0.5, orient=tk.HORIZONTAL)
        AAIRAA.pack(side="right", padx=5, pady=5)
        tk.Label(row5, text="Atrial Pulse Width (ms)").pack(side="left", padx=23, pady=5)
        AAIRAPW = tk.Scale(row5, from_=1, to=10, length=600, tickinterval=1, orient=tk.HORIZONTAL)
        AAIRAPW.pack(side="right", padx=5, pady=5)
        tk.Label(row6, text="Atrial Sensitivity (mV)").pack(side="left", padx=28, pady=5)
        AAIRAS = tk.Scale(row6, from_=1, to=10, length=600, tickinterval=1, orient=tk.HORIZONTAL)
        AAIRAS.pack(side="right", padx=5, pady=5)
        tk.Label(row7, text="ARP (ms)").pack(side="left", padx=60, pady=5)
        AAIRPVARP = tk.Scale(row7, from_=150, to=500, length=600, tickinterval=20, orient=tk.HORIZONTAL)
        AAIRPVARP.pack(side="right", padx=5, pady=5)
        tk.Label(row8, text="PVARP (ms)").pack(side="left", padx=53, pady=5)
        AAIRPVARP = tk.Scale(row8, from_=150, to=500, length=600, tickinterval=20, orient=tk.HORIZONTAL)
        AAIRPVARP.pack(side="right", padx=5, pady=5)
        tk.Button(row9, text="Submit", command=lambda:
                  update_info(8, AAIRLRL.get(), AAIRURL.get(), AAIRAA.get(), 0, AAIRAPW.get(), 0, AAIRAS.get(), 0, 0, 0, AAIRMSR.get(), AAIRPVARP.get(), 0, UserID)).pack(side="bottom", pady=5)
        tk.Label(row10, text=UserID).pack(side="left", padx=0, pady=5)
        tk.Label(row10, text=' ').pack(side="left", padx=325, pady=5)


        # VVIR
        row1 = ttk.Frame(VVIRTab)
        row1.pack()
        row2 = ttk.Frame(VVIRTab)
        row2.pack()
        row3 = ttk.Frame(VVIRTab)
        row3.pack()
        row4 = ttk.Frame(VVIRTab)
        row4.pack()
        row5 = ttk.Frame(VVIRTab)
        row5.pack()
        row6 = ttk.Frame(VVIRTab)
        row6.pack()
        row7 = ttk.Frame(VVIRTab)
        row7.pack()
        row8 = ttk.Frame(VVIRTab)
        row8.pack()
        row9 = ttk.Frame(VVIRTab)
        row9.pack()
        tk.Label(row1, text="Lower Rate Limit (ppm)").pack(side="left", padx=20, pady=5)
        VVIRLRL = tk.Scale(row1, from_=30, to=175, length=600, tickinterval=15, orient=tk.HORIZONTAL)
        VVIRLRL.pack(side="right", padx=5, pady=5)
        tk.Label(row2, text="Upper Rate Limit (ppm)").pack(side="left", padx=20, pady=5)
        VVIRURL = tk.Scale(row2, from_=50, to=175, length=600, tickinterval=15, orient=tk.HORIZONTAL)
        VVIRURL.pack(side="right", padx=5, pady=5)
        tk.Label(row3, text="Max Sensor Rate (ppm)").pack(side="left", padx=20, pady=5)
        VVIRMSR = tk.Scale(row3, from_=50, to=175, length=600, tickinterval=10, orient=tk.HORIZONTAL)
        VVIRMSR.pack(side="right", padx=5, pady=5)
        tk.Label(row4, text="Ventricular Amplitude (V)").pack(side="left", padx=15, pady=5)
        VVIRVA = tk.Scale(row4, from_=0.5, to=5, length=600, tickinterval=0.5, orient=tk.HORIZONTAL)
        VVIRVA.pack(side="right", padx=5, pady=5)
        tk.Label(row5, text="Ventricular Pulse Width (ms)").pack(side="left", padx=8, pady=5)
        VVIRVPW = tk.Scale(row5, from_=1, to=10, length=600, tickinterval=1, orient=tk.HORIZONTAL)
        VVIRVPW.pack(side="right", padx=5, pady=5)
        tk.Label(row6, text="Ventricular Sensitivity (mV)").pack(side="left", padx=13, pady=5)
        VVIRVS = tk.Scale(row6, from_=1, to=10, length=600, tickinterval=1, orient=tk.HORIZONTAL)
        VVIRVS.pack(side="right", padx=5, pady=5)
        tk.Label(row7, text="VRP (ms)").pack(side="left", padx=60, pady=5)
        VVIRVRP = tk.Scale(row7, from_=150, to=500, length=600, tickinterval=20, orient=tk.HORIZONTAL)
        VVIRVRP.pack(side="right", padx=5, pady=5)
        tk.Button(row8, text="Submit", command=lambda:
                  update_info(9, VVIRLRL.get(), VVIRURL.get(), 0, VVIRVA.get(), 0, VVIRVPW.get(), 0, VVIRVS.get(), 0, VVIRVRP.get(), VVIRMSR.get(), 0, 0, UserID)).pack(side="bottom", pady=5)
        tk.Label(row9, text=UserID).pack(side="left", padx=0, pady=5)
        tk.Label(row9, text=' ').pack(side="left", padx=325, pady=5)


        # DOOR
        row1 = ttk.Frame(DOORTab)
        row1.pack()
        row2 = ttk.Frame(DOORTab)
        row2.pack()
        row3 = ttk.Frame(DOORTab)
        row3.pack()
        row4 = ttk.Frame(DOORTab)
        row4.pack()
        row5 = ttk.Frame(DOORTab)
        row5.pack()
        row6 = ttk.Frame(DOORTab)
        row6.pack()
        row7 = ttk.Frame(DOORTab)
        row7.pack()
        row8 = ttk.Frame(DOORTab)
        row8.pack()
        row9 = ttk.Frame(DOORTab)
        row9.pack()
        row10 = ttk.Frame(DOORTab)
        row10.pack()
        tk.Label(row1, text="Lower Rate Limit (ppm)").pack(side="left", padx=20, pady=5)
        DOORLRL = tk.Scale(row1, from_=30, to=175, length=600, tickinterval=15, orient=tk.HORIZONTAL)
        DOORLRL.pack(side="right", padx=5, pady=5)
        tk.Label(row2, text="Upper Rate Limit (ppm)").pack(side="left", padx=20, pady=5)
        DOORURL = tk.Scale(row2, from_=50, to=175, length=600, tickinterval=15, orient=tk.HORIZONTAL)
        DOORURL.pack(side="right", padx=5, pady=5)
        tk.Label(row3, text="Max Sensor Rate (ppm)").pack(side="left", padx=20, pady=5)
        DOORMSR = tk.Scale(row3, from_=50, to=175, length=600, tickinterval=10, orient=tk.HORIZONTAL)
        DOORMSR.pack(side="right", padx=5, pady=5)
        tk.Label(row4, text="Fixed AV Delay (ms)").pack(side="left", padx=28, pady=5)
        DOORFAVD = tk.Scale(row4, from_=70, to=300, length=600, tickinterval=10, orient=tk.HORIZONTAL)
        DOORFAVD.pack(side="right", padx=5, pady=5)
        tk.Label(row5, text="Atrial Amplitude (V)").pack(side="left", padx=30, pady=5)
        DOORAA = tk.Scale(row5, from_=0.5, to=5, length=600, tickinterval=0.5, orient=tk.HORIZONTAL)
        DOORAA.pack(side="right", padx=5, pady=5)
        tk.Label(row6, text="Ventricular Amplitude (V)").pack(side="left", padx=15, pady=5)
        DOORVA = tk.Scale(row6, from_=0.5, to=5, length=600, tickinterval=0.5, orient=tk.HORIZONTAL)
        DOORVA.pack(side="right", padx=5, pady=5)
        tk.Label(row7, text="Atrial Pulse Width (ms)").pack(side="left", padx=23, pady=5)
        DOORAPW = tk.Scale(row7, from_=1, to=10, length=600, tickinterval=1, orient=tk.HORIZONTAL)
        DOORAPW.pack(side="right", padx=5, pady=5)
        tk.Label(row8, text="Ventricular Pulse Width (ms)").pack(side="left", padx=8, pady=5)
        DOORVPW = tk.Scale(row8, from_=1, to=10, length=600, tickinterval=1, orient=tk.HORIZONTAL)
        DOORVPW.pack(side="right", padx=5, pady=5)
        tk.Button(row9, text="Submit", command=lambda:
                  update_info(10, DOORLRL.get(), DOORURL.get(), DOORAA.get(), DOORVA.get(), DOORAPW.get(), DOORVPW.get(), 0, 0, 0, 0, DOORMSR.get(), 0, DOORFAVD.get(), UserID)).pack(side="bottom", pady=5)
        tk.Label(row10, text=UserID).pack(side="left", padx=0, pady=5)
        tk.Label(row10, text=' ').pack(side="left", padx=325, pady=5)

        
