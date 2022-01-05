from tkinter import *
from numpy import split
import google_searcher2 as gr2
import response_management as rm
import time

window = Tk() #independent window
window.title("CHATBOT")
txt = Text(window)
txt.grid(row=0, column=0, columnspan=2)
e = Entry(window, width=100)
e.grid(row = 1, column=0)

def send():
    user_input = e.get()
    send = 'You: ' + e.get()

    txt.insert(END, "\n" + send)
    e.delete(0, END)
    txt.see(END)

    return user_input

#--------------------------------Logic---------------------------------------

txt.insert(END,'Welcome to the chatbot! Say Hello to start a conversation!')

exit_list = ['exit','see you later','bye']

def logic():
        
        user_input = send()

        if user_input.lower() in exit_list:
            txt.insert(END, "\n" +'Bot: See you next time! :)')
            time.sleep(3)
            window.destroy()

        elif user_input.lower().startswith('google search'):
            txt.insert(END, "\n" +'Bot: Type what you would like to search on the console!')
            search = gr2.google_search()
            txt.insert(END, "\n" + 'Bot: ' +  search)

        else:
            if rm.check_all_messages(user_input) != None:
                txt.insert(END, "\n" +'Bot: ' + rm.get_response(user_input))

            else:
                txt.insert(END, "\n" +'Bot: ' + rm.get_response(user_input))

#----------------------------------------------------------------------------
send_button = Button(window, text='Send', command = logic).grid(row=1, column=1)
window.mainloop()