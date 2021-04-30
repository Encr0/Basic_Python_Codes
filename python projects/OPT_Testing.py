from tkinter import *
from tkinter import messagebox
import random

root=Tk()
root.title("OTP Testing")
root.geometry("300x200")
root.config(bg="black")

def getotp():
    messagebox.showinfo(title='OTP',message= f'YOUR OTP IS :{random.randint(1000,9999)}')


label=Label(root,text="--------Click to generate OTP--------",font=("arial",10,"bold"))
label.pack(fill=X,pady=5)

button=Button(root,text="GENERATE",font=("arial",10,"bold"),command=getotp)

button.pack()

root.mainloop()