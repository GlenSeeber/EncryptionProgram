import tkinter as tk
import pyperclip

#Global vars
toggle = 1                                      #toggle state 0 or 1
toggleOptions = ["Encrypt", "Decrypt"]          #list of toggle options

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
    toggleButton["text"] = toggleOptions[toggle-1]

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
window.geometry("640x460")

label_a = tk.Label(text="Enter Filepath to " + toggleOptions[toggle], width=100)
label_a.pack()

filePathEntry = tk.Entry(width=90)
filePathEntry.pack()

clipPasteButton = tk.Button(text="paste", command=setAsClip)
clipPasteButton.pack()

label_b = tk.Label(text="Enter Password to " + toggleOptions[toggle], width=100)
label_b.pack()

passwordEntry = tk.Entry(width=90)
passwordEntry.pack()

submit = tk.Button(text="Submit", command=submitF, )
submit.pack()

toggleButton = tk.Button(text=toggleOptions[toggle-1], command=toggleFunc)
toggleButton.pack()

window.mainloop()


