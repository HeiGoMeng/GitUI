import tkinter as tk
from tkinter import ttk
import subprocess

root = tk.Tk()

#Fun fact: Tkinter button object's command method expects a string, not a function
def WinCreate(title:str, height:int, width:int, options:tuple, rootWin:tk.Tk | tk.Toplevel, 
              func:str, OpVar:tk.StringVar, runButtonText:str = "Run your chosen function"):
    #Setup of new window
    Temp = tk.Toplevel(rootWin, height=height, width=width)
    Temp.title(title)
    Temp.withdraw()
    #The combobox for options
    Choices = ttk.Combobox(Temp, textvariable=OpVar)
    Choices['values'] = options
    Choices.grid(column=1, row=1, sticky="nswe")
    Choices.config(width=max([len(x) for x in options]))
    #Some would consider this redundant since Tk automatically resizes. Deletion is optional.
    #Resizement
    rootWin.update_idletasks()
    Temp.config(width=Choices.winfo_width())
    #A button to run stuff
    RunButton = tk.Button(rootWin, command=func, text=runButtonText)
    RunButton.grid(row=2, column=1)

    return Temp
PushVar = tk.StringVar()
GitRepo = None  #Placeholder


#FYI: Git pull -r origin basically gets the current branch on the remote 
# and puts it ahead of the current main branch
def Pull():
    if PushVar == "Standard":
        subprocess.run(
            [
            "git",
            "push"
            ]
        )
    elif PushVar == "Delete branch against remote":
        subprocess.run(
            [
                "git",
                "push",
                "origin",
                "--delete",
                "feature-branch"

            ]
        )
    elif PushVar == "Show what would be pushed":
        subprocess.run(
            [
                "git",
                "push",
                "--dry-run"
            ]
        )
         
        

WinCreate("Push", 250, 250, ("Delete branch against remote", "Standard", "Show what would be pushed"), root, func = "Push", runButtonText="PushOptions", OpVar = PushVar)