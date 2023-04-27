import tkinter as tk
import tkinter.filedialog as fd
import json
# from tkinter import LabelFrame
from tkinter import Button, Text, Label, Listbox, Canvas
# from tkinter import Scrollbar

def SortTimeLine():
    global timeline
    tlKeys= list(timeline.keys())
    tlKeys.sort()
    timeline = {i: timeline[i] for i in tlKeys}
    
def addTimeLine():
    year = txtYear.get("1.0","end-1c").strip()
    event = txtEvent.get("1.0","end-1c").strip()
    # print (f"year:{year} event:{event}")
    timeline[year]=event
    SortTimeLine()
    updateEventsList()

def updateEventsList():
    lstEvents.delete(0,tk.END)
    counter = 0
    for elem in timeline:
        lstEvents.insert(counter,f"{elem}|{timeline[elem]}")
        counter +=1

def removeItem():
    selectionList=[]
    global timeline
    sel = lstEvents.curselection()
    for s in sel:
        elem = lstEvents.get(s).split("|")[0]
        del timeline[elem]
    updateEventsList()
    
def loadTimeLine():
    global timeline
    f=fd.askopenfile().name
    print (f"file name:{f}")
    with open(f) as json_file:
        timeline = json.load(json_file)
    updateEventsList()

def saveTimeLine():
    global timeline
    f=fd.asksaveasfile().name
    print (f)
    with open(f,"w") as outfile:
        json_object = json.dump(timeline,outfile)

def drawTimeLine():
    lenght = 570
    start = 10
    y = 30
    w = 2
    cnvGraph.create_line(start,y,lenght,y,fill="green",width=w)
    


#region Main 
window = tk.Tk()
window.title("Timelines")
window.geometry("600x400")

# timeline={"1492":"Scoperta dell'America","1990":"GUNNS","1982":"Campioni del Mondo"}
timeline = {}

# scrollbar = Scrollbar(window)
# scrollbar.pack(side=tk.RIGHT, fill="y")

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

btnAdd = Button(window, text="Add", height=1, width=1,command=addTimeLine)
btnAdd.pack()
btnAdd.place(x=440, y=1)

# lstEvents = Listbox(window,font=("Verdana,8"),selectmode=tk.MULTIPLE,yscrollcommand = scrollbar.set)
lstEvents = Listbox(window,font=("Verdana,8"),selectmode=tk.MULTIPLE)
lstEvents.pack()
lstEvents.place(x=1,y=36,width=600,height=200)
# scrollbar.config(command=lstEvents.yview)

btnQuit = Button(window, text="Quit", height=1, width=1, command=quit)
btnQuit.pack()
btnQuit.place(x=540,y=1)

btnDelete = Button(window, text="Delete", height=1, width=2, command=removeItem)
btnDelete.pack()
btnDelete.place(x=480,y=1)

btnLoad = Button(window,text="Load",height=1,width=1,command=loadTimeLine)
btnLoad.pack()
btnLoad.place(x=400,y=1)

btnSave = Button(window,text="save",height=1,width=1,command=saveTimeLine)
btnSave.pack()
btnSave.place(x=350,y=1)

cnvGraph=Canvas(window,bg="light yellow",width=600)
cnvGraph.pack()
cnvGraph.place(x=1,y=250)

btnTimeLine=Button(window,text="Timeline",width=3,height=1,command=drawTimeLine)
btnTimeLine.pack()
btnTimeLine.place(x=290,y=1)

updateEventsList()
tk.mainloop()
#endregion