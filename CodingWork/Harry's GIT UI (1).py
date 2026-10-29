#This is cyberkid21c@hotmail.com's GIT UI with an inbuilt ForgeJo/Teams tab.
#For any issues, or questions please message me at harry.szeto@donvale.vic.edu.au or the aforementioned email above
#Feel free to mess with any code. Code has no copyright and is free to be used for any whatsoever, within lawful, and ethical reason.

#BTW, if I haven't yet added redundancy. Could someone please do that. Thanks!

#setup Tkinter code
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import scrolledtext
from PIL import Image, ImageTk
import subprocess
import os
from _collections_abc import Callable
root = tk.Tk()
root.option_add('*tearOff', 0)

#setup Tk window
root.title("GIT UI with ForgeJo/teams builtin")
root.geometry("500x500")
#background and other astethics
#bgF is background frame/root frame
bgF = tk.Frame(root, width = 500, height=500) #
bgImg = Image.open(r"C:\Users\CyberLiminal\GitUI\CodingWork\BG.png")
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
#Suf means suffix. Like -p, ., or any of the additions.
def RunCmd(*Suf):
    subprocess.run(
        [
            "git",
            NameToCmd[Choice.get()],
            *Suf
        ]
    )
#Open existing window
def OpWin():
    windows[Choice.get()].deiconify()

#Fun fact: Tkinter button object's command method expects a string, not a function
def WinCreate(title:str, height:int, width:int, options:tuple, rootWin:tk.Tk | tk.Toplevel, 
              func:str, OpVar:tk.StringVar, textBox:bool, textBoxMessage:str = "Enter your text here", runButtonText:str = "Run your chosen function"):
    #Setup of new window
    win = tk.Toplevel(rootWin, height=height, width=width)
    win.title(title)
    win.withdraw()
    #The combobox for options
    OpVar = tk.StringVar()
    Choices = ttk.Combobox(win, textvariable=OpVar)
    Choices['values'] = options
    Choices.grid(column=1, row=1, sticky="nswe")
    Choices.config(width=max([len(x) for x in options]))
    #Some would consider this redundant since Tk automatically resizes. Deletion is optional.
    #Resizement
    win.update_idletasks()
    win.config(width=Choices.winfo_width())
    #A button to run stuff
    RunButton = tk.Button(win, command=lambda : func(OpVar), text=runButtonText)
    RunButton.grid(row=2, column=1)
    #Quite a few Git functions need text. e.g Commit needs a commit message. So i have this textbox
    WinTextboxLabel = tk.Label(win, text = textBoxMessage)
    WinTextboxLabel.grid(row=3, column=1)
    WinTextbox = scrolledtext.ScrolledText(
    win,
    wrap = tk.WORD,
    height = 125,
    width=250,
)
    WinTextbox.grid(row=4, column = 1)
    return win
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

#Subwindow pararmeter definition

#You must define everything in the subwindow BEFORE you create them because you need to 
# pass it to the function


#Make sure to add not choosing right redundancy


#Add

AddVar = tk.StringVar()

AddPos = ["all changes in current directory including subdirectories",
                        "all changes in entire repository",
              "all modified and deleted files, but not untracked files",
              "one file",
              "one folder"]

def Add():
    if AddVar.get() != "":
        #Using Addpos[1] because of better modularity and 
        #because I'm not typing that entire message in
        if AddVar.get() == AddPos[0]:
            #RunCmd makes it so we only have to get the suffix
            RunCmd(".")
        elif AddVar.get() == AddPos[1]:
            RunCmd("-A")
        elif AddVar.get() == AddPos[2]:
            RunCmd("-u")
        elif AddVar.get() == AddPos[3]:
            StageFile = filedialog.askopenfilename(initialdir="/",
                                                   title="select a file")
            RunCmd(f"{StageFile}")
        elif Choice.get() == AddPos[4]:
            StageFolder = filedialog.askdirectory(initialdir="/",
                                                title="select a folder")
            RunCmd(f"{StageFolder}")
    else:
        pass
        #Again, can someone make sort of "opps, you made a mistake" popup? Thanks!

#Commit

CommitVar = tk.StringVar()

#FYI: Git pull -r origin basically gets the current branch on the remote 
# and puts it ahead of the current main branch
CommitWinName = None
def Commit():
    #comTex is short for commit text
    comTex = CommitWinName.WinTextBox.get("1.0", tk.END)
    if CommitVar == "Standard":
        if comTex != "":
            RunCmd("-m", f"{comTex}")
        else:
            pass #Once warning window creation is made
        
    elif CommitVar == "Stage and commit all changes to tracked files":
        if comTex != "":
                    RunCmd("-am", f"{comTex}")
        else:
            pass #Once warning window creation is made
    elif CommitVar == "Write over the previous commit in the chain, with a new commit including all staged changes plus a new commit message":
        if comTex != "":
            RunCmd("--amend", "-m", f"{comTex}")
        else:
            pass #Same thing here mate.

#Subwindow creation
windows = {}
for i in NameToCmd:
    windows[i] = WinCreate(title=NameToCmd[i], height=250, width=250, rootWin=root, 
                           options=AddPos, func=Add, runButtonText="Stage")

#Change to not doing it all at once, but bit by bit



            
         
        
#Win creation
CommitWin = WinCreate("Push", 250, 250, ("Stage and commit all changes to tracked files", "Standard", "Write over the previous commit in the chain, with a new commit including all staged changes plus a new commit message"), root, func = "Push", runButtonText="PushOptions", OpVar = CommitVar)
#For the actual commit message entry
CommitMessageTextboxLabel = tk.Label(CommitWin, text = 'Enter your commit message here')
CommitMessageTextboxLabel.grid(row=3, column=1)
CommitMessageTextbox = scrolledtext.ScrolledText(
    CommitWin,
    wrap = tk.WORD,
    height = 125,
    width=250,
)
CommitMessageTextbox.grid(row=4, column = 1)

#Pull

PullVar = tk.StringVar()
GitRepo = None  #Placeholder


#FYI: Git pull -r origin basically gets the current branch on the remote 
# and puts it ahead of the current main branch
def Pull():
    if PullVar == "rebase":
        subprocess.run(
            ["git",
            "pull",
            "-r",
            "origin",
            f"{GitRepo}"]
        )
    elif PullVar == "Standard":
        subprocess.run(
            [
                "git",
                "pull"
            ]
        )    
        

WinCreate("Pull", 250, 250, ("rebase", "Standard"), root, func = "Pull", runButtonText="PullOptions", OpVar = PullVar)

#Push

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

#Only the existing functions will have code. If you want something to be added, add it yourself. I am never 
#coming back to this project.


#ending Tkinter code
root.mainloop()

