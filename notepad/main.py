from tkinter import*
import pyttsx3
from tkinter import colorchooser
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os
engine=pyttsx3.init()
engine.setProperty('rate', 140)
engine.setProperty('volume',3)

def speek(text):
    engine.say(text)
    engine.runAndWait()

def speek_text():
    get=textbox.get(0.1,END)
    speek(get)
def cut():
    textbox.event_generate(("<<Cut>>"))


def copy():
    textbox.event_generate(("<<Copy>>"))


def paste():
    textbox.event_generate(("<<Paste>>"))


def delete():
    textbox.get(0.1, END)
    textbox.delete(0.1, END)


def changebackgroung():
    color = colorchooser.askcolor(title="Choose color")
    textbox.config(bg=color[1])


def changetext_color():
    text_color = colorchooser.askcolor(title="Choose color")
    textbox.config(fg=text_color[1])


def newfile():
    window.title("Untitled-Notepad")
    textbox.delete(1.0, END)


def openfile():
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*")])
    if file == "":
        file = None
    else:
        window.title(os.path.basename(file)+" Notepad"
                     )
        f = open(file, "r")
        textbox.delete(0.1, END)
        textbox.insert(1.0, f.read())
        f.close()


def savefile():
    global savefile
    savefile = asksaveasfilename(defaultextension=".txt", initialfile='Untitled.txt',
                                 filetypes=[("All Files", "*.*")])
    if savefile == "":
        savefile = None
    else:
        f = open(savefile, 'w')
        f.write(textbox.get(0.1, END))
        f.close()
        window.title(os.path.basename(savefile))


window = Tk()
window.geometry("600x400")
window.title("Notepad")

# adding app icon
icon = PhotoImage(file="note.png")
window.iconphoto(True, icon)

# adding scrollbar
scrollbar = Scrollbar(window)
scrollbar.pack(side=RIGHT, fill=Y)


textbox = Text(window, height=40, width=50, yscrollcommand=scrollbar.set, undo=True,
               font="korinna 15", selectbackground="yellow", selectforeground="black")
textbox.pack(fill=BOTH)
scrollbar.config(command=textbox.yview)
# Menubar
menubar = Menu(window)
menu = Menu(menubar, tearoff=0)
menu.add_command(label="New", command=newfile)
menu.add_command(label="Open", command=openfile)
menu.add_separator()
menu.add_command(label="Save as", command=savefile)
menu.add_command(label="Quit", command=window.quit)
menubar.add_cascade(label="File", menu=menu)

Edit = Menu(menubar, tearoff=0)
Edit.add_command(label="Cut               Ctrl+X", command=cut)
Edit.add_command(label="Copy            Ctrl+C  ", command=copy)
Edit.add_command(label="Paste            Ctrl+P", command=paste)
Edit.add_command(label="Clean", command=delete)

menubar.add_cascade(label="Edit", menu=Edit)

color = Menu(menubar, tearoff=0)
color.add_command(label="Backgroung Colour", command=changebackgroung)
color.add_command(label="Text Colour", command=changetext_color)
menubar.add_cascade(label='Colour', menu=color)

# menu for right click events
menu2 = Menu(window, tearoff=0)
menu2.add_command(label="New", command=newfile)
menu2.add_command(label="Open", command=openfile)
menu2.add_command(label="Save as", command=savefile)
menu2.add_separator()
menu2.add_command(label="Copy         Ctrl+C  ", command=copy)
menu2.add_command(label="Paste         Ctrl+P", command=paste)
menu2.add_command(label="Clean", command=delete)
menu2.add_command(label="Undo", command=textbox.edit_undo)
menu2.add_command(label="Redo", command=textbox.edit_redo)
menu2.add_command(label="speek", command=speek_text)
menu2.add_separator()
menu2.add_command(label="Text Color", command=changetext_color)
menu2.add_separator()
menu2.add_command(label="Quit Programme", command=window.quit)


def popup(event):
    # tk_popup it help you to pop up menu window on screen it take a parameter x.root and y.root
    # (x.root,y.root)==> give the current position of mouse pointer .
    try:
        menu2.tk_popup(event.x_root, event.y_root)
    finally:
        menu2.grab_release()


# handling right click events
textbox.bind("<Button-3>", popup)

window.config(menu=menubar)
window.mainloop()
