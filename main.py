#importing libraries:
from numpy import split
import google_searcher2 as gr2
import response_management as rm





#Starting the chat
def main():

    print('Welcome to the chatbot! Say Hello to start a conversation!')

    exit_list = ['exit','see you later','bye']

    while (True):

        user_input = input('You: ')

        if user_input.lower() in exit_list:
            print('Bot: See you next time! :)')
            break

        elif user_input.lower().startswith('google search'):
            print(gr2.google_search())

        else:
            if rm.check_all_messages(user_input) != None:
                print('Bot: ' + rm.get_response(user_input))

            else:
               print('Bot: ' + rm.get_response(user_input))

main()
