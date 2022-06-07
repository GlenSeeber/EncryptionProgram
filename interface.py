import tkinter as tk
from tkinter import font
import pyperclip
import subprocess
import main

# Global vars
toggle = 1  # toggle state 0 or 1
toggleOptions = ["ENCRYPT", "DECRYPT"]  # list of toggle options
# toggleFunctions = [Encrypt, Decrypt]   #list of functions

filePath = ""  # holds the path of file to be modified
password = ""  # holds the key to encrypt or decrypt with

fil = False    # bool for filepathentry focus
pas = False    # bool for passwordentry focus

Font_tuple = ("Comic Sans MS", 9)
# Functions


def toggleFunc():                               # changes the state of toggle and updates widgets
    global toggle

    if toggle == 0:
        toggle = 1
    else:
        toggle = 0

    label_a["text"] = "Enter Filepath to " + toggleOptions[toggle]
    label_b["text"] = "Enter Password to " + toggleOptions[toggle]

def sepFilePath(pth):
    global index

    index = 0
    for i in range(0, len(pth)):
        if pth[i] == "\\":
            index = i
    file = pth[index+1: -1]
    path = pth[0: index + 1]
    return (path, file)


def replaceSlash(pth):
    pth = pth.replace("\\", "/")
    return pth


# updates the filePath and password variables. Submits password and file to crypto functions
def submitF(Fpath=sepFilePath):
    global filePath
    global password

    filePath = filePathEntry.get()
    password = passwordEntry.get()

    path, file = Fpath(filePath)
    print(path + " " + file)

    if toggle == 0:
        main.encrypt(replaceSlash(path), file, password)
    else:
        main.decrypt(path, file, password)

    subprocess.Popen("explorer " + path)


def setAsClip():  # updates entry field(currently just filepath) with clipboard
    clip = ""
    print("hi")
    if(fil):
        while len(filePathEntry.get()) > 0:  # removes entry field contents
            filePathEntry.delete(0)
        clip = pyperclip.paste()
        filePathEntry.insert(0, clip)
    if(pas):
        while len(filePathEntry.get()) > 0:  # removes entry field contents
            passwordEntry.delete(0)
        clip = pyperclip.paste()
        passwordEntry.insert(0, clip)


def changeFill(e):
    global fil
    fil = not(fil)
    print(fil)


def changePass(e):
    global pas
    pas = not(pas)
    print(pas)


# Window and Widgets
window = tk.Tk()

window.geometry("880x460")

label_a = tk.Label(text="Enter Filepath to " + toggleOptions[toggle] + ":")
label_a.place(x=40, y=40)

filePathEntry = tk.Entry(width=90)
filePathEntry.place(x=220, y=40)

filePathEntry.bind("<FocusIn>", changeFill)
filePathEntry.bind("<FocusOut>", changeFill)

clipPasteButton = tk.Button(text="paste", command=setAsClip)
clipPasteButton.place(x=140, y=120)

label_b = tk.Label(text="Enter Password to " + toggleOptions[toggle] + ":")
label_b.place(x=40, y=80)

passwordEntry = tk.Entry(width=40)
passwordEntry.place(x=220, y=80)

passwordEntry.bind("<FocusIn>", changePass)
passwordEntry.bind("<FocusOut>", changePass)

submit = tk.Button(text="Submit", command=submitF, )
submit.place(x=510, y=75)

toggleButton = tk.Button(text="Toggle Function", command=toggleFunc)
toggleButton.place(x=40, y=120)

label_a.configure( font = Font_tuple)
label_b.configure( font = Font_tuple)
submit.configure( font = Font_tuple)
toggleButton.configure( font = Font_tuple)
passwordEntry.configure( font = Font_tuple)
filePathEntry.configure( font = Font_tuple)

window.mainloop()
