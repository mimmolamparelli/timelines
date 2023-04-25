import tkinter as tk
from tkinter import LabelFrame
from tkinter import Button, Text

window = tk.Tk()
window.title("Timelines")
window.geometry("400x300")

# FRAMES
frame1 = LabelFrame(window,
                    text="Frame 1",
                    bg="yellow",
                    fg="green",
                    padx=100,
                    pady=100)
frame1.grid(row=0, column=0)
frame2 = LabelFrame(window,
                    text="Frame 2",
                    bg="gray",
                    fg="green",
                    padx=100,
                    pady=100)

frame2.grid(row=0, column=1)
frame3 = LabelFrame(window, text="Text", bg="white", fg="black")
frame3.grid(row=1, column=0)
# FRAME 1
b1 = Button(frame1, text="One")
# b2 = Button(frame1, text="Two")
# t2 = Text(frame1, height=2, width=10)
b1.pack(side=tk.BOTTOM)
# b2.pack(side=tk.BOTTOM)
# t2.pack(side=tk.BOTTOM)
# t2.insert(tk.END, "Three")

# FRAME 2
b3 = Button(frame2, text="Four")
b3.pack(side=tk.LEFT)
# FRAME 3
t1 = Text(frame3, height=2, width=10)
t1.insert(tk.END, "Five")
t1.pack(side=tk.LEFT)

# hello = tk.Label(text="Time Lines Creator")
# hello.pack()
# button = tk.Button(text="Click me!")
# button.pack()

tk.mainloop()
