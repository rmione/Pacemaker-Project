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

    
def update_info(mode, low, up, AAmp, VAmp, APW, VPW, ASense, VSense, ARP, VRP):
    """
    Neatly updates dictionary with pacemaker parameters as per requirements in documentation.
    """

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
        if float(low) > float(up):
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


