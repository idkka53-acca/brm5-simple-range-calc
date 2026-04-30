#modules

from tkinter import *
from tkinter import ttk
import tkinter as tk

#modules end

#essentials
root = tk.Tk()
root.title("simple brm5 calc")
frame1 = ttk.Frame(root, padding=10)
def buttononeclicked():
    root.destroy()
testvar = root.attributes("-alpha",0.92)
#esentials end

#interactable elements

button1 = ttk.Button(frame1, text="quit",command=buttononeclicked)
button1.grid(column=10, row=21)
frame1.grid(row=6, column=5, sticky=(N, W, E, S))
Entry1 = ttk.Entry(frame1, width=20)
Entry1.grid(column=0, row=3)
root.resizable(False, False)
root.geometry("420x420")
sides = StringVar()
sides1 = ttk.Combobox(frame1, width=17, textvariable=sides)
sides1['values'] = ("shoulder to shoulder", "torso width", "sides", "height")
sides1.grid(column=0, row=4)
sides1.state(['readonly'])
thingette = ttk.Label(frame1, text="input the mils")
thingette.grid(column=0, row=6)
miliradians = StringVar()
miliradians1 = ttk.Entry(frame1, width=20, textvariable=miliradians)
miliradians1.grid(column=0, row=7)
#interactable elements end

#calculating part

sizevals = ["520", "130.8", "87", "480"]
rootdict = {"shoulder to shoulder": 520, "torso width": 130.8, "sides": 87, "height": 480}
def youraisemeupdontyou():
    root.attributes("-topmost", button4.instate(['selected']))
    return
def calculate(width , mils):
    hopes = rootdict[width]
    global distance
    distance = (hopes) / mils
    label3.config(text=f"Calculated distance: {distance:} meters")
    return distance
def sides():
   global a
   a = sides1.get()
   print(a)
   calculate(a , b)
def mils():
    global b
    b = float(miliradians1.get())
    print(b)
    sides()

#calculating end

#labels

button2 = ttk.Button(frame1, text="calculate", command=mils)
button2.grid(column=9, row=8)
root.bind("<F7>",  lambda event: button4.invoke())
button4 = ttk.Checkbutton(frame1, text="toggle always on top", command=youraisemeupdontyou)
button4.grid(column=15, row=0)
#labeling
label2 = ttk.Label(frame1, text="")
label2.grid(column=7, row=7)
label3 = ttk.Label(frame1, text="")
label3.grid(column=0, row=9)
instlabel = ttk.Label(frame1, text="press F7 to toggle always on top")
instlabel2 = ttk.Label(frame1, text="input the SIDE your measuring and the mils")
instlabel2.grid(column=0, row=19)
instlabel.grid(column=0, row=20)
label = ttk.Label(frame1, text="Which side are you measuring?")
label.grid(column=0, row=0)

#labeling end



#no inputs without this
root.mainloop()

