from QuoteHandle import Quotes
from WallpaperCreator import Creator
from QuoteConnection import Connection
import time
import random

class Main:
    def __init__(self):
        self.__connected = False
#        self.__connections = Connection()
        self.__author = ["Albert Einstein",
                         "Douglas Adams"]


    def __call__(self):
        self.__connected = Connection.TryConnection

        q = Quotes()
        q.Author = self.ChooseAuthor(self.__author)
        c = Creator(q.Quote)
        c.SaveWallpaper()
        

    def ChooseAuthor(self, author):
        if isinstance(author, list) or isinstance(author, tuple):
            return random.choice(author)

        return author
            


if __name__ == "__main__":    
    m = Main()
    m()
