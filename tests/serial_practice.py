import serial
import struct
import serial.tools.list_ports
import json
import os
import tkinter as tk
from tkinter import ttk
from Interface import *
# todo: Here we have the baud rate, defined in the lecture slides/serial guide.
#   No idea what serial port we're going to be using, so for now it will be set to COM2.
#   We definitely need to have parity bits... I don't know how even to use a parity bit... is the error detection done
#   automatically, or...?

UPLOAD_LOCATION = os.getcwd() + '\SerialComm.json'
"""
I imagine that this will be best done by a function, or we could hard code it each time with a unique version, depending 
on which pacing mode we use, etc., since we will be using more or less parametes depending on a few things.

Or we can have our function, either taking them all and defaulting the optional parameters to None, OR
we could have kwargs which sort of accomplish the same goal anyways.
"""
def list_ports():
    ports_list = serial.tools.list_ports.comports()
    connected_ports = []
    # read off how many connected ports we have
    print(len(connected_ports))
    for port in ports_list:
        connected_ports.append(port)
        # return the list of connected ports when all is said and done
        # it returns memory addresses?
    return connected_ports


def to_bytes(mode, low, up, AAmp, VAmp, APW, VPW, ASense, VSense, ARP, VRP, MaxSense, FAVD, ReTime, RecTime, RespFact, AThresh):
    """
    Going to need some sort of order here.
    Judging by the params we have laid out, something like this: 
        mode:lowerratelim:upperratelim:... and so on, and so forth
    """


    # todo:
    #  for now we are going to assume longs. No idea as to what behaviour this entails but could be a catch all!!!!
    #  keep in mind these are signed longs, so i think it will work as a catch-all

    # Something like this seems to be the proper thing to do. We'll have to see

    """
    Mostafa was sayng that uint8s can be denoted for Python purposes to shorts or char? 
    doubles are d
    

    """
    # todo: we can write just the struct.pack????? Do we need to return a bytesarray?!?!?!?!
    return bytearray(struct.pack('HIIddIIddIIIIIHHI', mode, low, up, AAmp, VAmp, APW, VPW, ASense, VSense, ARP, VRP, MaxSense, FAVD, ReTime, RecTime, RespFact, AThresh))  # todo: honestly don't know if this is fine or not. We'll have to see.


baud_rate = 115200
# You can define Serial objects with unique parameters, so we can have different parities, bytesize etc. will be handy!!
# board = serial.Serial(
#                         port='COM1',
#                         baudrate=baud_rate,
#                         parity=serial.PARITY_NONE,
#                         bytesize=8
#
#                     )
print(to_bytes(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17)) # Writing to serial seems to be fairly simple

class Serial_functions:
    @classmethod
    def serial_read(cls, serial_obj):

        print("top level..")
        for line in serial_obj.readlines(8): # read 8 bytes
            print("yo!")
            print(line)
        # b = board.inWaiting()
        # print(board.read(b))
        serial_obj.close()


# Serial_functions.serial_read(board)

def communicate_parameters(username):
    with open(UPLOAD_LOCATION) as f:
        pacemaker_params = json.load(f)[username]
        # todo: in this case we'll need to make sure the user exists when we do this
        try:
            """
            Something like this is basically what we're going to have to do afaik so I'll leave it at that
            """
            data = to_bytes(
                # todo: maybe switch to dict.get method instead???!!!!
                pacemaker_params["Mode"],
                pacemaker_params["Low_Limit"],
                pacemaker_params["Up_Limit"],
                pacemaker_params["A_Amp"],
                pacemaker_params["V_Amp"],
                pacemaker_params["A_PW"],
                pacemaker_params["V_PW"],
                pacemaker_params["A_Sense"],
                pacemaker_params["V_Sense"],
                pacemaker_params["ARP"],
                pacemaker_params["VRP"],
                pacemaker_params["Max_Sense"],
                pacemaker_params["PVARP"],
                pacemaker_params["FAVD"],
                username
                    )
            board.write(data)
        except KeyError as e:
            messagebox.showinfo("Error", "Something went critically wrong: " + str(e))


