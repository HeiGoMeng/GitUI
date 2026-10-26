import tkinter as tk
from tkinter import ttk


def WinCreate(name:str, title:str, height:int, width:int, options:tuple, root:tk.Tk | tk.Toplevel, 
              func:function, runButtonText:str = "Run your chosen function"):
    #Setup of new window
    name = tk.Toplevel(root, heigh=height, width=width, title=title)
    name.withdraw()
    #The combobox for options
    ChoiceVar = tk.StringVar()
    Choices = ttk.Combobox(name, textvariable=ChoiceVar)
    Choices['values'] = options
    Choices.grid(column=1, row=1, sticky="nswe")
    Choices.config(width=max([len(x) for x in options]))
    #Some would consider this redundant since Tk automatically resizes. Deletion is optional.
    #Resizement
    root.update_idle_tasks()
    name.config(width=Choices.winfo_width())
    #A button to run stuff
    RunButton = tk.Button(root, command=func, text=runButtonText)
    RunButton.grid(row=2, column=1)


