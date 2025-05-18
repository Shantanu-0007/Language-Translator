from tkinter import*
from tkinter import ttk
import tkinter as tk
from googletrans import Translator,LANGUAGES

def data():
    s=sorc.get()
    d=dest.get()
    masg=Size.get(1.0,END)
    textget=change(text=masg,src=s,dest=d)
    Size1.delete(1.0,END)
    Size1.insert(END,textget)

def change(text="type",src="English",dest="Hindi"):
    text1=text
    src1=src
    dest1=dest
    trans=Translator()
    trans1=trans.translate(text,src=src1,dest=dest1)
    return trans1.text

root=tk.Tk()
root.title("LANGUAGE TRANSLATOR")
root.geometry("500x700")
root.resizable(0,0)
root.config(bg='light blue')

Label(root,text="LANGUAGE TRANSLATOR",font="Algerian 20 bold",bg="light blue").pack()

frame=Frame(root).pack(side=BOTTOM)

label1=Label(root,text="Enter Text",font=("Algerian",18,"bold"),fg="Black",bg="light blue")
label1.place(x=100,y=100,height=20,width=300)

Size=Text(frame,font=("Time New Roman",20,"bold"),wrap=WORD)
Size.place(x=10,y=130,height=150,width=480)

list_text=list(LANGUAGES.values())

sorc=ttk.Combobox(frame,value=list_text)
sorc.place(x=10,y=300,height=40,width=150)
sorc.set("English")

button_change=Button(frame,text="CONVERT",relief=RAISED,command=data)
button_change.place(x=170,y=300,height=40,width=150)

dest=ttk.Combobox(frame,value=list_text)

dest.place(x=330,y=300,height=40,width=150)
dest.set("English")

label1=Label(root,text="Result",font=("Algerian",18,"bold"),fg="black",bg="light blue")
label1.place(x=100,y=360,height=20,width=300)

Size1=Text(frame,font=("Time New Roman",20,"bold"),wrap=WORD)
Size1.place(x=10,y=400,height=150,width=480)

root.mainloop()
