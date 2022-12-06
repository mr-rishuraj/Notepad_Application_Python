#Import required libraries.
from tkinter import *
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog
from tkinter import ttk   
from tkinter import messagebox
import webbrowser 
#Setup the window.
window = tk.Tk()
window.geometry('600x400')
window.minsize(200,100)
window.title('Notepad')
#Create and Place the Scrolledtext widget.
text = ScrolledText(window,height=1000,undo=True)
text.pack(fill=tk.BOTH)
#User defined functions.
#Function 1 for 'New' option.
def new():
  text.delete('1.0','end')
#Function 2 for 'Open' option.
def Open():
  file_open = filedialog.askopenfilename(title="Select file",filetypes=(("jpeg files","*.jpg"),("all files","*.*")))
  file = open(file_open)
  text.insert('end',file.read())
#Function 3 for 'Save as' option.
def save_as():
  window.filename = filedialog.asksaveasfile(mode="w",defaultextension='.txt')
  if window.filename is None:
    return
  file_save =  str(text.get(1.0,END))
  window.filename.write(file_save)
  window.filename.close()
#Function 4 for 'Save' option.
def save():
  save_As()
#Function 5 for 'Exit' option.
def exit():
  message = messagebox.askquestion('Notepad', 'Do You Want to Save Changes')
  if message == 'yes':
    save_as()
  else:
    window.destroy()
#Function 6 for 'Cut' option.
def cut():
  text.event_generate('<<Cut>>')
#Function 7 for 'Copy' option.
def copy():
  text.event_generate('<<Copy>>')
#Function 8 for 'Paste' option.
def paste():
  text.event_generate('<<Paste>>')
#Function 9 for 'Delete' option.
def delete():
  message = messagebox.askquestion('Notepad', 'Do you want to Delete All')
  if message == 'yes':
    text.delete('1.0', 'end')
  else: 
    return 'break'
#Function 10 for 'Select all' option.
def select_all():
  text.tag_add('sel', '1.0', 'end')
  return 'break'

#Function 11 for 'View help' option.
def view_help():
  webbrowser.open('https://support.microsoft.com/en-us/windows/help-in-notepad-4d68c388-2ff2-0e7f-b706-35fb2ab88a8c')
#Create menubar widget.
menubar = Menu(window)
#File Menu.
file = Menu(menubar)
#Add options in File Menu
file.add_command(label="New",command=new)
file.add_command(label="Open",command=Open)
file.add_command(label="Save", command = save)
file.add_command(label="Save as",command=save_as)
file.add_separator()
file.add_command(label="Exit", command = exit)
menubar.add_cascade(label="File",menu=file,font=('verdana',10,'bold'))
#Edit Menu.
edit = Menu(menubar)
#Add options in Edit Menu.
edit.add_command(label="Undo",accelerator="Ctrl+Z",command=text.edit_undo)
edit.add_command(label="Redo",accelerator="Ctrl+Y",command=text.edit_redo)
edit.add_separator()
edit.add_command(label="Cut",accelerator="Ctrl+X", command = cut)
edit.add_command(label="Copy",accelerator="Ctrl+C", command = copy)
edit.add_command(label="Paste",accelerator="Ctrl+V", command = paste)
edit.add_command(label="Delete",accelerator="Del", command = delete)
edit.add_command(label="Select All",accelerator="Ctrl+A", command = select_all)
menubar.add_cascade(label="Edit",menu=edit)
#Help Menu.
Help = Menu(menubar)
#Add options in Help Menu.
Help.add_command(label="View Help", command = view_help)
menubar.add_cascade(label="Help",menu=Help)
#Insert Options  
Insert = Menu(menubar)
#Add options in Insert Menu.
Insert.add_command(label="Insert Image", command = view_help)
menubar.add_cascade(label="Insert", menu=Help)
#Add Menubar to the window. 
m = Menu(window)
#Add menu items to Menu
window.config(menu=menubar)
#Call the mainloop() method.
window.mainloop()