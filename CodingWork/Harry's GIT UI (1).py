#This is cyberkid21c@hotmail.com's GIT UI with an inbuilt ForgeJo/Teams tab.
#For any issues, or questions please message me at harry.szeto@donvale.vic.edu.au or the aforementioned email above
#Feel free to mess with any code. Code has no copyright and is free to be used for any whatsoever, within lawful, and ethical reason.

#setup Tkinter code
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
import subprocess
import os
root = tk.Tk()
root.option_add('*tearOff', 0)

#setup Tk window
root.title("GIT UI with ForgeJo/teams builtin")
root.geometry("500x500")
#background and other astethics
#bgF is background frame/root frame
bgF = tk.Frame(root, width = 500, height=500) #
bgImg = Image.open(r"C:\Users\harry.szeto\OneDrive - Donvale Christian College\Year 8\Electives\Coding\GIT UI\BG.png")
bg = ImageTk.PhotoImage(bgImg)
bgLabel = tk.Label(bgF, image = bg)
bgLabel.place(x=0, y=0, relwidth = 1, relheight = 1)
bgF.pack()

#Functions
#CD into a folder
def cdFolder():
    cfd = filedialog.askdirectory()
    print(cfd)
    os.chdir(cfd)
    folder_window = tk.Toplevel(root)
#Run a command in terminal
def RunCmd():
    subprocess.run(
        [
            "git",
            NameToCmd[Choice.get()]
        ]
    )
#Open existing window
def OpWin():
    windows[Choice.get()].deiconify()


#UI

#UI creation frame
uiF = tk.Frame(bgF, width = 250, height = 250)
uiF.place(relx=0.125, rely=0.125, relheight= 0.75, relwidth = 0.75)

#Widgets

#Combobox of options
Choice = tk.StringVar()

funcChoice = ttk.Combobox(uiF, textvariable = Choice)

funcChoice['values'] = ('Add',
                        'Pull',
                        'Push',
                        'Commit',
                        'Branch',
                        'Checkout',
                        'Check branches',
                        'Rebase',
                        'Merge'
                        )
funcChoice.grid(row = 2, column = 1, sticky="ew")

#ApplyAction button
Act = tk.Button(uiF,
          text = "Run",
          command = OpWin
          )
Act.grid(row = 1, column = 2)

#Selectfolder button
selectFolder = tk.Button(uiF,
                       text = "Choose folder",
                       command = cdFolder)
selectFolder.grid(row=3, column=1)
#The purpose of NameToCmd, is so that long GIT function can be abreviated and to provide a dictionary 
#of function for easy auto window creation; just enter a func here, and a window will be created for it.
#You still need to add code though.
NameToCmd = {
    'Add': "add",
    "Pull": "pull",
    "Push": "push",
    "Commit": "commit",
    "Branch":"branch",    
    "Checkout":'checkout',
    "Check branches": "branch",
    "Rebase": "rebase",
    "Merge": 'merge'
            }
#All the function sub-windows
#For all those wondering, NameToCmd[i] returns the key.
#This is a list of windows for evry single function

#Subwindows

#Subwindow creation
windows = {}
for i in NameToCmd:
    windows[i] = tk.Toplevel(root)
    windows[i].title(f"{NameToCmd[i]}")
    windows[i].withdraw()
    windows[i].geometry("250x250")

#Only the existing function will have code. If you want something to be added, add it yourself. I am never 
#coming back to this project.

#Shorthand variable; easier
AddW = windows["Add"]

#Git add can stage multiple files. Sees if the user wants to stage one file, 
#multiple files or really just everything

Files = ttk.Combobox(AddW, selectmode = "multiple")
Files.grid(column=1, row=1, sticky="nswe")

#I am not including git add -p. I do not have time. If you want it, add it yourself.

AddChoices = ["everything in directory",
              "everything in directory plus deletions",
              "all modified and deleted files, but not untracked files",
              "show what would be staged"]
for i in AddChoices:
    Files.insert(tk.END, i)
Files.config(width=max([len(x) for x in AddChoices]))
#ending Tkinter code
root.mainloop()

