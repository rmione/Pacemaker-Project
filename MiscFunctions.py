import tkinter as tk
from tkinter import ttk
import json
import os
from Interface import *

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
    # if it exists, load in that database as the current database.
    with open(DUMP_LOCATION) as f:
        database = json.load(f)
else:
    # Otherwise initialize a new database. 
    database = {}

''' PACEMAKER VALUES '''
# Checks if the json file exists
if os.path.exists(UPLOAD_LOCATION):
    # if it exists, load in that database as the current database.
    with open(UPLOAD_LOCATION) as f:
        pacemaker_values = json.load(f)
else:
    # Otherwise initialize a new database. 
    pacemaker_values = {}

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

    
def update_info(mode, low, up, AAmp, VAmp, APW, VPW, ASense, VSense, ARP, VRP, MaxSense, PVARP, FAVD, ReTime, RecTime, RespFact, AThresh, user):
    """
    Neatly updates dictionary with pacemaker parameters as per requirements in documentation.
    """

    

    UpdateMsg = ""            
                
    if float(low) > float(up):
        low = 50
        UpdateMsg = UpdateMsg + "Lower Rate Limit Fixed to 50ppm \n"
    elif float(low) < 50:
        low = 50
    pacemaker_values.update({user :{"Mode": mode, "Up_Limit": (up), "Low_Limit": (low), "A_Amp": (AAmp), "V_Amp": (VAmp), "A_PW": (APW), "V_PW": (VPW), "A_Sense": (ASense), "V_Sense": (VSense), "ARP": (ARP), "VRP": (VRP), "Max_Sense": (MaxSense), "PVARP": (PVARP), "FAVD": (FAVD), "ReTime": (ReTime), "RecTime": (RecTime), "RespFact": (RespFact), "AThresh": (AThresh)}})
    IO.dump(UPLOAD_LOCATION, pacemaker_values)
    UpdateMsg = UpdateMsg + "Pacemaker Values Updated Successfully"
    print(UpdateMsg)
    messagebox.showinfo("Pacemaker Message", UpdateMsg)

'''
    try:
        """
        This conditional checks that all the strings passed in as parameters convert properly. It is inside a try-except 
        to catch a faulty conversion
        """
        if int(mode) and int(low) and int(up) and int(AAmp) and int(VAmp) and int(APW) and int(VPW) and int(ASense) and int(VSense) and int(ARP) and int(VRP) and int(MaxSense) and int(PVARP) and int(FAVD):
            pass
        
    except ValueError as e:

        """
        In this situation, we have some invalid input, and it didn't convert properly. 
        
        """
        messagebox.showinfo("Error", "Invalid info! Re enter")
'''

