from glob import glob
import tkinter as tk
from turtle import bgcolor

from matplotlib.pyplot import text

toggle = 1
toggleOptions = ["Encrypt", "Decrypt"]

def toggleFunc():
    global toggle
    if toggle == 0:
        toggle = 1
    else:
        toggle = 0

    label_a["text"] = "Enter Filepath to " + toggleOptions[toggle]
    toggleButton["text"] = toggleOptions[toggle-1]

def submitF():
    print(filePath.get())

window = tk.Tk()

frame_a = tk.Frame()
frame_b = tk.Frame()

label_a = tk.Label(master=frame_a, text="Enter Filepath to " + toggleOptions[toggle], width=70)
label_a.pack()

filePath = tk.Entry(master=frame_a, width=30)
filePath.pack()

submit = tk.Button(master=frame_a, text="Submit", command=submitF)
submit.pack()

toggleButton = tk.Button(master=frame_a, text=toggleOptions[toggle-1], command=toggleFunc)
toggleButton.pack()

frame_a.pack()

window.mainloop()


