from tkinter import *
from tkinter.messagebox import showinfo
from PIL import Image,ImageTk
from random import randint

root=Tk()
root.title("cual es la probabilidad de que se chupen los webos")
root.geometry("360x360")

def puto():
    number = randint(60,100)
    showinfo("cuanto se aman los putos", f"la probabilidad de que se chupen los webos es de {number} %")

open_img=Image.open("love.png")
render_img = ImageTk.PhotoImage(open_img)

main_image = Label(root,image=render_img)
main_image.image=render_img
main_image.grid(row=0,columnspan=2)

label1=Label(root,text="Persona 1 : ",font=("arial",10,"bold"))
label1.grid(row=1,column=0,sticky="w")

entry1=Entry(root,font=("arial",10,"bold"))
entry1.grid(row=1,column=1)

label2=Label(root,text="Persona 2 : ",font=("arial",10,"bold"))
label2.grid(row=2,column=0)

entry2=Entry(root,font=("arial",10,"bold"))
entry2.grid(row=2,column=1)

button=Button(root,text="revisa si son geis xd !",bd=2,font=("arial",12,"bold"),command=puto,fg="red",bg="black")
button.grid(row=3,columnspan=2)

root.mainloop()