from tkinter import *


my_window=Tk()

label_1=Label(my_window,text="Please enter your username:")
entry_1 = Entry(my_window)
label_2=Label(my_window,text="Please enter your password:")
entry_2 = Entry(my_window)
button_1 = Button(my_window,text="Click me to enter name",command=my_window.destroy)

label_1.grid(row=0,column=0)
entry_1.grid(row=0,column=1)
label_2.grid(row=1,column=0)
entry_2.grid(row=1,column=1)
button_1.grid(row=2,column=0)

my_window.mainloop()


phrase = str(input("Please enter a phrase: "))
print()
shift = int(input("Enter the shift value: "))
length = len(phrase)
#print(length)
Conv = ""
for i in range(length):
    Conv = Conv + chr(ord(phrase[i])+shift)
print(Conv)
