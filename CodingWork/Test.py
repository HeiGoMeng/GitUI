import tkinter as tk
from tkinter import scrolledtext

root = tk.Tk()
top = tk.Toplevel(root)
lab = scrolledtext.ScrolledText(top)
lab.insert(tk.INSERT, "test text smple")


wig = top.winfo_children()[0]
wigT = wig.winfo_children()[1]
print(wigT.get("1.0", tk.END)) #type:ignore

print(top.winfo_children()[0].winfo_children()[1].get("1.0", tk.END)) 