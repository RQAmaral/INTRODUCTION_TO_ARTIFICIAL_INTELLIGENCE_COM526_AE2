from tkinter import *

window = Tk() #independent window
window.title("ChatBot")
window.geometry('500x300')


label = Label(window, text='hola ninhooooo',fg='blue',font=('Arial',14))
label.grid(row=0,column=0,padx=5,pady=10)

data=StringVar()

textbox1=Entry(window,textvariable=data,fg='green',font=('Arial',14))
textbox1.grid(row=0,column=1)

def myfunction():
    emptylabel.config(text='hello')

button1=Button(window,command=myfunction,text='submit',fg='green',font=('Arial',14))
button1.grid(row=1,column=1,sticky=W)

emptylabel = Label(window,fg='blue',font=('Arial',14))
emptylabel.grid(row=2,column=1,sticky=W)

window.mainloop()





















