import tkinter as tk
# from tkinter import LabelFrame
from tkinter import Button, Text, Label

window = tk.Tk()
window.title("Timelines")
window.geometry("600x400")

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

b1 = Button(window, text="One")
b1.pack()
b1.place(x=400, y=1)
tk.mainloop()
