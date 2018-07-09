import requests
from bs4 import BeautifulSoup
import random
import string

class Quotes:
    def __init__(self):
        self.__source = "https://www.brainyquote.com/authors/"
        self.__author = "Douglas Adams"
        self.__quotes = []
        self.__quote = ""
        self.__Update()
        

    @property
    def Author(self):
        return self.__author


    @Author.setter
    def Author(self, value):
        for p in string.punctuation:
            if p in value:
                value.replace(p, "")

        self.__author = value

        #Reload
        self.__Update()


    @property
    def Quotes(self):
        return self.__quotes


    @property
    def Quote(self):
        return self.__quote


    def __Update(self):
        self.LoadQuotes()
        self.RandomQuote()


    def LoadQuotes(self):
        url = self.__source + self.__author.replace(" ", "_").lower()

        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        quotes = soup.find_all("a", title="view quote")
        buffer = []

        for quote in quotes:
            quote = quote.text

            if quote != "":
                buffer.append(quote)

        self.__quotes = list(set(buffer))
        return self.__quotes


    def RandomQuote(self):     
        if self.__quotes:
            self.__quote = random.choice(self.__quotes) + "--" + self.__author
            return self.__quote
        
        return []
    
        

        


