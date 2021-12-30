#importing libraries:
import random
import string
import numpy as np
import warnings
import bot_response as br
warnings.filterwarnings("ignore")

#Starting the chat
def main():

    print('Welcome to the chatbot! Say Hello to start a conversation!')

    exit_list = ['exit','see you later','bye']

    while (True):
        user_input = input()
        if user_input.lower() in exit_list:
            print('Bot: See you next time! :)')
            break
        
        else:
            if greeting_response(user_input) != None:
                print('Bot:'+greeting_response(user_input))

            else:
                print('Bot:'+br.bot_response(user_input))


#Function which return a random response to users greeting
def greeting_response(text):
    text = text.lower()

    bot_greetings = ['hello', 'hey', 'hiya', 'sup','hi']

    user_greetings = ['hello', 'hey', 'hiya', 'sup','hi']

    for word in text.split():
        if word in user_greetings:
            return random.choice(bot_greetings)


if __name__ == "__main__":
    main()