#This is cyberkid21c@hotmail.com's GIT UI with an inbuilt ForgeJo/Teams tab.
#For any issues, or questions please message me at harry.szeto@donvale.vic.edu.au or the aforementioned email above
#Feel free to mess with any code. Code has no copyright and is free to be used for any whatsoever, within lawful, and ethical reason.

#BTW, if I haven't yet added redundancy. Could someone please do that. Thanks!

#setup Tkinter code
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import scrolledtext
from tkinter import font
from PIL import Image, ImageTk
import subprocess
import os
from enum import Enum
root = tk.Tk()
root.option_add('*tearOff', 0)

#setup Tk window
root.title("GIT UI with ForgeJo/teams builtin")
root.geometry("500x500")
fontUsed = font.nametofont("TkDefaultFont")
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
            GitOps[Choice.get()],
            *Suf
        ]
    )
#Open existing window
def OpWin():
    windows[
        GitOps[Choice.get()].value #This is a part of the 5 way repeat handshake I talk about later
        ].deiconify()

    #add this back later in the code due to the fact that this ain't a compiler

class GitOps(Enum):
    ADD = "add"
    PULL = 'pull'
    PUSH = 'push'
    COMMIT = 'commit'
    BRANCH_FUNCTION_INC_REBASE = 'branch'
    MERGE = 'merge'
#Fun fact: Tkinter button object's command method expects a string, not a function


def WinCreate(title:str, options:tuple, rootWin:tk.Tk | tk.Toplevel, 
              func:str, OpVar:tk.StringVar, textBox:bool = False, textBoxMessage:str = "Enter your text here", runButtonText:str = "Run your chosen function",
              height:int = 250, width:int = 250, ):
    #Setup of new window
    win = tk.Toplevel(rootWin)
    win.title(title)
    win.geometry(f"{height}x{width}")
    #When the user tries to delete the window, it's withdrawn instead for later use
    win.protocol("WM_DELETE_WINDOW", win.withdraw)
    win.withdraw()
    #The combobox for options
    OpVar = tk.StringVar()
    Choices = ttk.Combobox(win, textvariable=OpVar)
    Choices['values'] = options
    Choices.grid(column=1, row=1, sticky="nswe")
    Choices.config(width=len(max(options, key=len)))
    #Some would consider this redundant since Tk automatically resizes. Deletion is optional.
    #Resizement
    win.update_idletasks()
    #A button to run stuff
    RunButton = tk.Button(win, command=lambda : func, text=runButtonText)
    RunButton.grid(row=2, column=1)
    #Quite a few Git functions need text. e.g commit needs a commit message. So i have this textbox
    if textBox == True:
        WinTextboxLabel = tk.Label(win, text = textBoxMessage)
        WinTextboxLabel.grid(row=3, column=1)
        WinTextbox = scrolledtext.ScrolledText(
        win,
        wrap = tk.WORD,
        height = 5 #In characters, not pixels
        )
        WinTextbox.grid(row=4, column = 1, sticky="ew")
        #Choice.winfo_width and everything else is measured in no# of characters, then max returns the largest one. measure takes how many
        #pixels long it is

        #max(options, key=len) is the width of the combobox, set earlier in code
        #This negates the problem of TypeError: object of type 'method' has no len()
    #Window resizement
    Leeway = 150
    #Let's say you underestimate the width of the windows you thought you needed.
    #This fixes that problem for you!
    #Unfortunately, if you have two widgets in the same row, like in the merge window, it doesn't work
    #That one's on you
    if fontUsed.measure(max(max(options, key=len), runButtonText, textBoxMessage if True else "", key=len)) > width:
        win.geometry(f'{fontUsed.measure(max(max(options, key=len), runButtonText, textBoxMessage if True else "", key=len))+Leeway}x{height}')
    return win
#UI

#UI creation frame
uiF = tk.Frame(bgF, width = 250, height = 250)
uiF.place(relx=0.125, rely=0.125, relheight= 0.75, relwidth = 0.75)

#Widgets

#Combobox of options
Choice = tk.StringVar()

funcChoice = ttk.Combobox(uiF, textvariable = Choice)

funcChoice['values'] = tuple([x.name for x in GitOps])

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


#All the function sub-windows


#Subwindows 

#Subwindow pararmeter definition

#You must define everything in the subwindow BEFORE you create them because you need to 
# pass it to the function

#Windows are created bit by bit for more individual control over them


#Make sure to add not choosing right redundancy


#add

addVar = tk.StringVar()

addPos = ["all changes in current directory including subdirectories",
                        "all changes in entire repository",
              "all modified and deleted files, but not untracked files",
              "one file",
              "one folder"]

def add():
    if addVar.get() != "":
        #Using addpos[1] because of better modularity and 
        #because I'm not typing that entire message in
        if addVar.get() == addPos[0]:
            #RunCmd makes it so we only have to get the suffix
            RunCmd(".")
        elif addVar.get() == addPos[1]:
            RunCmd("-A")
        elif addVar.get() == addPos[2]:
            RunCmd("-u")
        elif addVar.get() == addPos[3]:
            StageFile = filedialog.askopenfilename(initialdir="/",
                                                   title="select a file")
            RunCmd(f"{StageFile}")
        elif Choice.get() == addPos[4]:
            StageFolder = filedialog.askdirectory(initialdir="/",
                                                title="select a folder")
            RunCmd(f"{StageFolder}")
    else:
        pass
        #Again, can someone make sort of "opps, you made a mistake" popup? Thanks!


#Make sure to go name of func when you go NameToCmd[i] + win, so we can put all windows in one list
addWin = WinCreate(title="add", width=250, height=250, options=tuple(addPos), 
                                     rootWin=root, func = "push", runButtonText="pushOptions", OpVar = addVar)

#commit

commitVar = tk.StringVar()

commitPos = ["Stage and commit all changes to tracked files", 
             "Standard", 
             "Write over the previous commit in the chain, with a new commit including all staged changes plus a new commit message"]

#FYI: Git pull -r origin basically gets the current branch on the remote 
# and puts it ahead of the current main branch

def commit():
    #comTex is short for commit text
    #winfo_children gets the window's children. the number 3 is hard-coded because I have other priorities
    #and you could honestly add that yourself. And if you wondering, what does it acess, it acesses the optional
    #textbox is the function
    comTex = commitWin.winfo_children()[3].get("1.0", tk.END) # type: ignore
    if commitVar == commitPos[1]:
        if comTex != "":
            RunCmd("-m", f"{comTex}")
        else:
            pass #Once warning window creation is made
        
    elif commitVar == commitPos[0]:
        if comTex != "":
                    RunCmd("-am", f"{comTex}")
        else:
            pass #Once warning window creation is made
    elif commitVar == commitPos[2]:
        if comTex != "":
            RunCmd("--amend", "-m", f"{comTex}")
        else:
            pass #Same thing here mate.'

commitWin = WinCreate(title="commit", width=250, height=250, options=tuple(commitPos), 
                                     rootWin = root, func = "commit", runButtonText="commitOptions", OpVar = commitVar, 
                                     textBox=True, textBoxMessage= "Please enter your commit message here."
                                     )       


#pull

pullVar = tk.StringVar()

pullPos = ["rebase",
           "Standard"
           ]

#FYI: Git pull -r origin basically gets the current branch on the remote 
# and puts it ahead of the current main branch
def pull():
    if pullVar == pullPos[0]:
        RunCmd("-r", "origin", f"{cfd}")
    elif pullVar == pullPos[1]:
        RunCmd()
        
pullWin = WinCreate(title="pull", width=250, height=250, options=("rebase", "Standard"), rootWin=root, func = "pull", runButtonText="pullOptions", OpVar = pullVar)

#push
pushVar = tk.StringVar()

pushPos = [
    "Standard",
    "Delete branch against remote",
    "Show what would be pushed"
]

#FYI: Git pull -r origin basically gets the current branch on the remote 
# and puts it ahead of the current main branch
def push():
    if pushVar == pushPos[0]:
        RunCmd()
    elif pushVar == pushPos[1]:
        RunCmd("origin", "--delete", "feature-branch")
    elif pushVar == "Show what would be pushed":
        RunCmd("--dry-run")

pushWin = WinCreate(title="push", width=250, height=250, options=tuple(pushPos), rootWin=root, func = "push", runButtonText="pushOptions", OpVar = pushVar)

#Create new branch

branchCreateVar = tk.StringVar()

branchCreatePos = [
    "Create new branch",
    "Switch to a new branch",
    "Check branches",
    "Rebase onto new branch"
]


def branch():
    branchText =  branchWin.winfo_children()[3].get("1.0", tk.END) #type: ignore
    if branchCreateVar == branchCreatePos[0]:
        RunCmd(f"{branchText}")
    if branchCreateVar == branchCreatePos[1]:
        subprocess.run(
            [
                "git",
                "switch",
                f"{branchText}"
            ]
        )
    if branchCreateVar == branchCreatePos[2]:
        #You can change this to runcmd(). I feel this will be easier though to use subprocess.run to
        #directly capture the output, since i only need to do it for this one function
        OutbranchTxt = subprocess.run(
            [
                "git",
                "branch"
            ],
            capture_output=True,
            text=True
        )
        #ResLabel for result label branch win
        ResLblBnchWin = tk.Label(branchWin, text=f"{OutbranchTxt}")
        ResLblBnchWin.grid(row=5, column=1)
    if branchCreateVar == branchCreatePos[3]:
        subprocess.run(
            [
                "git",
                "rebase",
                f"{branchText}"
            ]
        )

branchWin = WinCreate(title="branch", width=250, height=250, options= tuple(branchCreatePos),
                      rootWin=root, func = "branch", runButtonText="branchOptions", OpVar = branchCreateVar,
                      textBox=True, textBoxMessage="Please enter your new branch name, name of branch you are" \
                      "switching to, or branch you are rebasing on top of")

#merge

mergeVar = tk.StringVar()
mergeVarSuf = tk.StringVar()

mergePos = [
    "merge with another branch",
    "merge with multiple branches"
]

mergeSufPos = [
    "no fast forwards",
    "only fast forward",
    "if possible, fast forward"
]

def merge():
    #A list is used here, because the will grow too much due if further options are added, due to the fact
    #that you're combining the names and suffixes 
    mergeCmd = []
    if mergeVarSuf == mergeSufPos[0]:
        mergeCmd.append("--no-ff")
    elif mergeVar == mergeSufPos[1]:
        mergeCmd.append("--ff-only")
    elif mergeVarSuf == mergeSufPos[2]:
        mergeCmd.append("--ff")

    if mergeVar == mergePos[0]:
        mergeCmd.append(mergeWin.winfo_children()[3].get("1.0", tk.END)) #type:ignore
    elif mergeVar == mergePos[1]:
        mergeCmd.append(mergeWin.winfo_children()[3].get("1.0", tk.END).split(","))

    RunCmd(tuple(mergeCmd))

mergeWin = WinCreate(title="merge", width=250, height=250, options= tuple(mergePos),
                      rootWin=root, func = "merge", runButtonText="mergeOptions", OpVar = mergeVar,
                      textBox=True, textBoxMessage="Please the name/s of the branches you wish to merge with this syntax: branch_1," \
                      "branch_2,branch_3  and on and on, with no spaces" \
                      "switching to, or branch you are rebasing on top of")
SufComb = ttk.Combobox(mergeWin, textvariable=mergeVarSuf)
SufComb['values'] = mergeSufPos
SufComb.grid(row=1, column=2)

#Only the existing functions will have code. If you want something to be added, add it yourself. I am never 
#coming back to this project.

#List of all the windows for easy acces by opwin()

windows = {}
#For all those wondering, NameToCmd[i] returns the key.
#This is a list of windows for evry single function
#This is why we need NameToCmd[i] + win naming scheme for Toplevel window naming
#globals() returns a list of all global variables. If you would like to be able to have window variables not be global, you can go and
#manually add them to a global list, and change this around a bit, but this way is preferred for this simple usecase.

#globals()[f"{NameToCmd[i]}Win"] is the toplevels themselves

for i in range(len(GitOps)):
    windows[GitOps[list(GitOps.__members__.keys())[i]].value] = globals()[f"{GitOps[list(GitOps.__members__.keys())[i]].value}Win"]
    #The apporach of this line works like this:
    #[x.value for x in GitOps.__members__] returns a list of all values of GitOps. You then take the current index.
    #These values are the same as the variable names except that the first letter is lowercase and that it's missing "win"
    #globals() is a global dictionary allowing us to use the variable name to get the actual Toplevel
    #.upper, the curly brakets, and the indexes allow us to change the string and mold it into the toplevel name/global() key
    #this toplevel is then connected to the dic window as a value with the key [x.value for x in GitOps.__members__][i], which is it's name in the dropdown combobox
    #menu in the opening window
    # [i] takes the current relevant key. This coordinates with the options in the dropdown menu at the starting window

    #This connects to Opwin() via windows[Choice.get()], since Choice.get() is the same as [x.value for x in GitOps.__members__][i]],
    #since, GitOps is a conversion ENUM that converts the names in the dropdown menu to the actually command names
    #This is basically a five way handshake and for further explanation of this line, go up to the OpWin() function

#ending Tkinter code
root.mainloop()

