import tkinter as tk
import pyperclip

#Global vars
toggle = 1                                      #toggle state 0 or 1
toggleOptions = ["ENCRYPT", "DECRYPT"]          #list of toggle options

filePath = ""                                   #holds the path of file to be modified
password = ""                                   #holds the key to encrypt or decrypt with

#Functions
def toggleFunc():                               # changes the state of toggle and updates widgets
    global toggle

    if toggle == 0:
        toggle = 1
    else:
        toggle = 0

    label_a["text"] = "Enter Filepath to " + toggleOptions[toggle]
    label_b["text"] = "Enter Password to " + toggleOptions[toggle]

def submitF():                                  #updates the filePath and password variables.  Todo: call encryption/decryption function
    global filePath
    global password

    filePath = filePathEntry.get()
    password = passwordEntry.get()

def setAsClip():                                #updates entry field(currently just filepath) with clipboard
    while len(filePathEntry.get()) > 0:         #removes entry field contents
        filePathEntry.delete(0)

    clip = ""
    clip = pyperclip.paste()
    filePathEntry.insert(0,clip)


# Window and Widgets
window = tk.Tk()
window.geometry("1080x460")

label_a = tk.Label(text="Enter Filepath to " + toggleOptions[toggle] +":")
label_a.place(x=40,y=40)

filePathEntry = tk.Entry(width=90)
filePathEntry.place(x= 200,y=40)

clipPasteButton = tk.Button(text="paste", command=setAsClip)
clipPasteButton.place(x=140,y=120)

label_b = tk.Label(text="Enter Password to " + toggleOptions[toggle] +":")
label_b.place(x=40,y=80)

passwordEntry = tk.Entry(width=90)
passwordEntry.place(x= 200,y=80)

submit = tk.Button(text="Submit", command=submitF, )
submit.place(x=750,y=55)

toggleButton = tk.Button(text="Toggle Function", command=toggleFunc)
toggleButton.place(x=40,y=120)

window.mainloop()


