import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
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
CommitVar = tk.StringVar()
GitRepo = None  #Placeholder


#FYI: Git pull -r origin basically gets the current branch on the remote 
# and puts it ahead of the current main branch
def Commit():
    if CommitVar == "Standard":
        if CommitMessageTextbox.get("1.0", tk.END) != "":
            subprocess.run(
                [
                "git",
                "commit",
                "-m",
                f"{CommitMessageTextbox.get("1.0", tk.END)}"
                ]
            )
        else:
            pass #Once warning window creation is made
        
    elif CommitVar == "Stage and commit all changes to tracked files":
        if CommitMessageTextbox.get("1.0", tk.END) != "":
                    subprocess.run(
                        [
                        "git",
                        "commit",
                        "-am",
                        f"{CommitMessageTextbox.get("1.0", tk.END)}"
                        ]
                    )
        else:
            pass #Once warning window creation is made
    elif CommitVar == "Write over the previous commit in the chain, with a new commit including all staged changes plus a new commit message":
        if CommitMessageTextbox.get("1.0", tk.END) != "":
            subprocess.run(
                [
                    "git",
                    "commit",
                    "--amend",
                    "-m",
                    f"{CommitMessageTextbox.get("1.0", tk.END)}"
                ]
            )
        else:
            pass #Same thing here mate.
            
         
        

CommitWin = WinCreate("Push", 250, 250, ("Stage and commit all changes to tracked files", "Standard", "Write over the previous commit in the chain, with a new commit including all staged changes plus a new commit message"), root, func = "Push", runButtonText="PushOptions", OpVar = CommitVar)
CommitMessageTextboxLabel = tk.Label(CommitWin, text = 'Enter your commit message here')
CommitMessageTextboxLabel.grid(row=3, column=1)
CommitMessageTextbox = scrolledtext.ScrolledText(
    CommitWin,
    wrap = tk.WORD,
    height = 125,
    width=250,
)
CommitMessageTextbox.grid(row=4, column = 1)