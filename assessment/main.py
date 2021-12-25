#importing libraries:
from newspaper import Article
import random
import string
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import warnings
warnings.filterwarnings("ignore")

#Downloading punkt package:
nltk.download('punkt', quiet=True)

#Getting Articles
article = Article('https://www.sas.com/en_in/insights/analytics/machine-learning.html')
article.download()
article.parse()
article.nlp()
corpus = article.text



#Tokenization
text = corpus
setence_list = nltk.sent_tokenize(text) #creating a list of sentences



#Function which return a random response to users greeting
def greeting_response(text):
    text = text.lower()

    bot_greetings = ['hello', 'hey', 'hi ya', 'sup']

    user_greetings = ['hello', 'hey', 'hi ya', 'sup']

    for word in text.split():
        if word in user_greetings:
            return random.choice(bot_greetings)

def index_sort(list_var):
    length = len(list_var)
    list_index = list(range(0, length))

    x = list_var
    for i in range(length):
        for j in range(length):
            if x[list_index[i]] > x[list_index[j]]:
                #Swap
                temp = list_index[i]
                list_index[i] = list_index[j]
                list_index[j] = temp

    return list_index

#Creating bot responses
def bot_response(user_input):
    user_input  = user_input.lower()
    setence_list.append(user_input)
    bot_response = ''
    cm = CountVectorizer().fit_transform(setence_list)
    similarity_scores = cosine_similarity(cm[-1],cm)
    similarity_scores_list = similarity_scores.flatten()
    index = index_sort(similarity_scores_list)
    index = index[1:]
    response_flag = 0

    j = 0
    for i in range(len(index)):
        if similarity_scores_list[index[i]] >0.0:
            bot_response = bot_response+' '+setence_list[index[i]]
            response_flag = 1
            j = j+1
        if j > 2:
            break

    if response_flag == 0:
        bot_response = bot_response+' '+"Sorry i didn't understant ;("
    setence_list.remove(user_input)

    return bot_response

#Starting the chat
print('#something we gotta decide')

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
            print('Bot:'+bot_response(user_input))
