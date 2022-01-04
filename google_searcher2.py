from textblob import TextBlob
import requests
from bs4 import BeautifulSoup

def search(message):
    term = ''.join(message[2:])
    print(term)
    url = 'https://www.google.com/search?=q{0}&source=lnms&tbm=nws'.format(term)
    response = requests.get(url)
    #print(response.text)
    soup = BeautifulSoup(response.text, 'html.parser')
    headline_results = soup.find_all('div', class_='st')

    for h in headline_results:
        print('h')

