from tkinter import *

base_window = Tk() #independent window

def create_window():
    new_window = Toplevel()#Dependent window

def create_base_window():
    base_window.destroy()
    window = Tk()#Independent window
    Button(window,text="Create new Window",command = create_window).pack()
    Button(window,text="Create new Base Window",command = create_base_window).pack()


Button(base_window,text="Create new Window",command = create_window).pack()
Button(base_window,text="Create new Base Window",command = create_base_window).pack()


base_window.mainloop()