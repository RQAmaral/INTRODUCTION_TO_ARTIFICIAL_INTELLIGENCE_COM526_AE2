from googlesearch import search
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from newspaper import Article

def google_search():

    user_input = input("Google Search mode: ")

    article_list = [] 

    #Getting Articles
    for i in search(user_input, tld='com', lang='en', num=10, stop=10, pause=2.0):
        article = Article(i)
        article_list.append(article)
    
    for article in article_list:
        article.download()
        article.parse()
        article.nlp()

        corpus = article.text

        #Downloading punkt package:
        nltk.download('punkt', quiet=True)

        #Tokenization
        text = corpus
        sentence_list = nltk.sent_tokenize(text) #creating a list of sentences
        
        sentence_list.append(user_input)
        bot_response = ''
        cm = CountVectorizer().fit_transform(sentence_list)
        similarity_scores = cosine_similarity(cm[-1],cm)
        similarity_scores_list = similarity_scores.flatten()
        index = index_sort(similarity_scores_list)
        index = index[1:]
        response_flag = 0

        j = 0
        for i in range(len(index)):
            if similarity_scores_list[index[i]] >0.0:
                bot_response = bot_response+' '+sentence_list[index[i]]
                response_flag = 1
                j = j+1
            if j > 2:
                break

        if response_flag == 0:
            bot_response = bot_response+"Sorry i didn't understand :("
        sentence_list.remove(user_input)

        return bot_response

        #url = 'https://www.google.com/search?q={0}&source=lnms&tbm=nws'.format(term)
    
def index_sort(list_var):
    length = len(list_var)
    list_index = list(range(0,length))

    x = list_var
    for i in range(length):
        for j in range(length):
            if x[list_index[i]] > x[list_index[j]]:
                #Swap
                temp = list_index[i]
                list_index[i] = list_index[j]
                list_index[j] = temp

    return list_index