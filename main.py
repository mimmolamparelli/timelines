import tkinter as tk
# from tkinter import LabelFrame
from tkinter import Button, Text, Label

def addTimeLine():
    print ("adding a timeline")
    year = txtYear.get("1.0","end-1c")
    event = txtEvent.get("1.0","end-1c")
    print (f"year:{year} event:{event}")

window = tk.Tk()
window.title("Timelines")
window.geometry("600x400")

timeline = {}
lblYear = Label(window, text="Year", font=("Verdana", 8))
lblYear.pack()
lblYear.place(x=1, y=1)

txtYear = Text(window, font=("Verdana", 8), height=1, width=10)
txtYear.pack()
txtYear.place(x=1, y=18)

lblEvent = Label(window, text="Event", font=("Verdana", 8))
lblEvent.pack()
lblEvent.place(x=80, y=1)

txtEvent = Text(window, font=("Verdana", 8), height=1, width=30)
txtEvent.pack()
txtEvent.place(x=80, y=18)

btnAdd = Button(window, text="Add", height=1, width=5,command=addTimeLine)
btnAdd.pack()
btnAdd.place(x=400, y=1)



tk.mainloop()
