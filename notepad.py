from tkinter import *
import tkinter.messagebox as tmsg
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os
def newfile():
    global file
    root.title("Untitled-Notepad")
    file = None
    Textarea.delete(1.0,END)


def openfile():
    global file
    file=askopenfilename(defaultextension=".txt",filetypes=[("All files","*.*"),("TextDocuments","*.txt")])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file)+"- Notepad")
        Textarea.delete(1.0,END)
        f=open(file,"r")
        Textarea.insert(1.0,f.read())
        f.close()

def savefile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile='Untitled.txt',defaultextension=".txt",filetypes=[("All files","*.*"),("TextDocuments","*.txt")])
        if file=="":
            file = None
        else:
            f = open(file,"w")
            f.write(Textarea.get(1.0,END))
            f.close()
            root.title(os.path.basename(file) + " - Notepad")
            print("file saved")

    else:
        f = open(file, "w")
        f.write(Textarea.get(1.0, END))
        f.close()


def quitapp():
    root.destroy()

def cut():
    Textarea.event_generate(("<<Cut>>"))
def copy():
    Textarea.event_generate(("<<Copy>>"))
def paste():
    Textarea.event_generate(("<<Paste>>"))


def about():
    tmsg.showinfo("Notepad ---> avani baheti ","Notepad by avani baheti.")


if __name__=='__main__':
    root = Tk()
    root.geometry("500x600")
    root.title("Notepad ---> Avani baheti")
    root.wm_iconbitmap("icon1.ico")
    Textarea=Text(root,font="lucida 11")
    file=None
    Textarea.pack(expand=True,fill=BOTH)

    menubar = Menu(root)

    filemenu = Menu(menubar,tearoff=0)
    filemenu.add_command(label="New",command=newfile)
    filemenu.add_command(label="Open",command=openfile)
    filemenu.add_command(label="Save", command=savefile)
    filemenu.add_separator()
    filemenu.add_command(label="Exit",command=quitapp)
    menubar.add_cascade(label="File",menu=filemenu)

    editmenu = Menu(menubar, tearoff=0)
    editmenu.add_command(label="Cut", command=cut)
    editmenu.add_command(label="Copy", command=copy)
    editmenu.add_command(label="Paste", command=paste)
    menubar.add_cascade(label="Edit", menu=editmenu)

    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="About Notepad", command=about)
    menubar.add_cascade(label="Help", menu=helpmenu)

    scrollbar = Scrollbar(Textarea)
    scrollbar.pack(side=RIGHT, fill=Y)
    scrollbar.config(command=Textarea.yview)
    Textarea.config(yscrollcommand=scrollbar.set)
    root.config(menu=menubar)


    root.mainloop()