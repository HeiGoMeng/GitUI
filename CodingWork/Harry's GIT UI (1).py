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
#CD'd folder directory
cfd = None
def cdFolder():
    global cfd
    cfd = filedialog.askdirectory()
    os.chdir(cfd)
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
    #windows[Choice.get()].deiconify()
    pass
    #add this back later in the code due to the fact that this ain't a compiler

#Fun fact: Tkinter button object's command method expects a string, not a function
def WinCreate(title:str, height:int, width:int, options:tuple, rootWin:tk.Tk | tk.Toplevel, 
              func:str, OpVar:tk.StringVar, textBox:bool = False, textBoxMessage:str = "Enter your text here", runButtonText:str = "Run your chosen function"):
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
    RunButton = tk.Button(win, command=lambda : func, text=runButtonText)
    RunButton.grid(row=2, column=1)
    #Quite a few Git functions need text. e.g Commit needs a commit message. So i have this textbox
    if textBox == True:
        WinTextboxLabel = tk.Label(win, text = textBoxMessage)
        WinTextboxLabel.grid(row=3, column=1)
        WinTextbox = scrolledtext.ScrolledText(
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
                        'Create new branch',
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
    "Branch": "branch",
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

#Windows are created bit by bit for more individual control over them


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

AddWin = WinCreate(title="Add", width=250, height=250, options=tuple(AddPos), 
                                     rootWin=root, func = "Push", runButtonText="PushOptions", OpVar = AddVar)

#Commit

CommitVar = tk.StringVar()

CommitPos = ["Stage and commit all changes to tracked files", 
             "Standard", 
             "Write over the previous commit in the chain, with a new commit including all staged changes plus a new commit message"]

#FYI: Git pull -r origin basically gets the current branch on the remote 
# and puts it ahead of the current main branch

def Commit():
    #comTex is short for commit text
    #winfo_children gets the window's children. the number 3 is hard-coded because I have other priorities
    #and you could honestly add that yourself. And if you wondering, what does it acess, it acesses the optional
    #textbox is the function
    comTex = CommitWin.winfo_children()[3].get("1.0", tk.END) # type: ignore
    if CommitVar == CommitPos[1]:
        if comTex != "":
            RunCmd("-m", f"{comTex}")
        else:
            pass #Once warning window creation is made
        
    elif CommitVar == CommitPos[0]:
        if comTex != "":
                    RunCmd("-am", f"{comTex}")
        else:
            pass #Once warning window creation is made
    elif CommitVar == CommitPos[2]:
        if comTex != "":
            RunCmd("--amend", "-m", f"{comTex}")
        else:
            pass #Same thing here mate.'

CommitWin = WinCreate(title="Commit", width=250, height=250, options=tuple(CommitPos), 
                                     rootWin = root, func = "Commit", runButtonText="CommitOptions", OpVar = CommitVar, 
                                     textBox=True, textBoxMessage= "Please enter your commit message here."
                                     )       
#Win creation
CommitWin = WinCreate("Push", 250, 250, ("Stage and commit all changes to tracked files", "Standard", "Write over the previous commit in the chain, with a new commit including all staged changes plus a new commit message"), root, func = "Push", runButtonText="PushOptions", OpVar = CommitVar)


#Pull

PullVar = tk.StringVar()

PullPos = ["rebase",
           "Standard"
           ]

#FYI: Git pull -r origin basically gets the current branch on the remote 
# and puts it ahead of the current main branch
def Pull():
    if PullVar == PullPos[0]:
        RunCmd("-r", "origin", f"{cfd}")
    elif PullVar == PullPos[1]:
        RunCmd()
        
PullWin = WinCreate(title="Pull", width=250, height=250, options=("rebase", "Standard"), rootWin=root, func = "Pull", runButtonText="PullOptions", OpVar = PullVar)

#Push
PushVar = tk.StringVar()

PushPos = [
    "Standard",
    "Delete branch against remote",
    "Show what would be pushed"
]

#FYI: Git pull -r origin basically gets the current branch on the remote 
# and puts it ahead of the current main branch
def Push():
    if PushVar == PushPos[0]:
        RunCmd()
    elif PushVar == PushPos[1]:
        RunCmd("origin", "--delete", "feature-branch")
    elif PushVar == "Show what would be pushed":
        RunCmd("--dry-run")

PushWin = WinCreate(title="Push", width=250, height=250, options=tuple(PushPos), rootWin=root, func = "Push", runButtonText="PushOptions", OpVar = PushVar)

#Create new branch

BranchCreateVar = tk.StringVar()

BranchCreatePos = [
    "Create new branch",
    "Switch to a new branch",
    "Check branches",
    "Rebase onto new branch"
]
#BranchCreateVar == BranchCreatePos

def Branch():
    BranchText =  BranchWin.winfo_children()[3].get("1.0", tk.END) #type: ignore
    if BranchCreateVar == BranchCreatePos[0]:
        RunCmd(f"{BranchText}")
    if BranchCreateVar == BranchCreatePos[1]:
        subprocess.run(
            [
                "git",
                "switch",
                f"{BranchText}"
            ]
        )
    if BranchCreateVar == BranchCreatePos[2]:
        #You can change this to runcmd(). I feel this will be easier though to use subprocess.run to
        #directly capture the output, since i only need to do it for this one function
        OutBranchTxt = subprocess.run(
            [
                "git",
                "branch"
            ],
            capture_output=True,
            text=True
        )
        #ResLabel for result label branch win
        ResLblBnchWin = tk.Label(BranchWin, text=f"{OutBranchTxt}")
        ResLblBnchWin.grid(row=5, column=1)
    if BranchCreateVar == BranchCreatePos[3]:
        subprocess.run(
            [
                "git",
                "rebase",
                f"{BranchText}"
            ]
        )

BranchWin = WinCreate(title="Branch", width=250, height=250, options= tuple(BranchCreatePos),
                      rootWin=root, func = "Branch", runButtonText="BranchOptions", OpVar = BranchCreateVar,
                      textBox=True, textBoxMessage="Please enter your new branch name, name of branch you are" \
                      "switching to, or branch you are rebasing on top of")

#Only the existing functions will have code. If you want something to be added, add it yourself. I am never 
#coming back to this project.



#ending Tkinter code
root.mainloop()

#NameToCmd = {
    #"Rebase": "rebase",
    #"Merge": 'merge'
     #       
