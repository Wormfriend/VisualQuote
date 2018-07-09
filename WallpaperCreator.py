from PIL import Image, ImageFont, ImageDraw
from screeninfo import get_monitors
import os

class Creator:
    def __init__(self,
                 Text = "Test",
                 FontSize=100,
                 AuthorFontSize = 80,
                 FontType="Jellyka_Estrya_Handwriting.ttf",
                 FontColor=(255,255,255),
                 BackgroundColor = "black",
                 Path = "/home/" + os.environ["USER"] + "/Pictures/VisualQuoteWallpaper.png"):

        self.__Text = ""
        self.__Author = ""
        self.Text = Text
        self.__FontSize = FontSize
        self.__AuthorFontSize = AuthorFontSize
        self.__FontType = FontType
        self.__FontColor = FontColor
        self.__BackgroundColor = BackgroundColor
        self.__WallpaperSize = self.AutoSize()
        self.__img = None
        self.__path = Path
        self.CreateWallpaper()


    @property
    def FontSize(self):
        return self.__FontSize


    @FontSize.setter
    def FontSize(self, value):
        self.__FontSize = value


    @property
    def AuthorFontSize(self):
        return self.__AuthorFontSize


    @AuthorFontSize.setter
    def AuthorFontSize(self, value):
        self.__AuthorFontSize = value


    @property
    def FontType(self):
        return self.__FontType


    @FontType.setter
    def FontType(self, value):
        self.__FontType = value


    @property
    def WallpaperSize(self):
        return self.__WallpaperSize


    @WallpaperSize.setter
    def WallpaperSize(self, value):
        if isinstance(value, tuple):
            if len(value) == 2:
                self.__WallpaperSize = value
                return self.__WallpaperSize

        raise ValueError("WallpaperSize must be tuple with length 2.")


    @property
    def Text(self):
        return self.__Text


    @Text.setter
    def Text(self, value):
        self.__Text, self.__Author = self.__FormatText(value)        


    def AutoSize(self):
        resolution = get_monitors()[0]

        self.__WallpaperSize = (resolution.width, resolution.height)
        return resolution.width, resolution.height


    def __FormatText(self, text):
        text, author = text.split("--")
        text = text.split(" ")
        formated_text = ""
        
        for i, token in enumerate(text, start=1):
            formated_text += token

            if i % 15:
                formated_text += " "
                continue

            formated_text += "\n"
        
        return formated_text, author


    def __TextSize(self, draw, text, fnt):
        return draw.textsize(text, font=fnt)
            

    def __Center(self, size):
        w, h = size
        width, height = self.__WallpaperSize

        x = width/2 - w/2
        y = height/2 - h/2

        return int(x), int(y)


    def __PositionAuthor(self, text_size, author_size, offset=0.1):
        text_x, text_y = self.__Center(text_size)
        text_width, text_height = text_size

        author_width, author_height = author_size
        author_x = (text_x + text_width) - int((text_x + text_width)*offset) - author_width
        author_y = (text_y + text_height) + 10

        return int(author_x), int(author_y)
        
                    
    def CreateWallpaper(self):
        resolution = get_monitors()[0]
        width, height = self.__WallpaperSize
        
        img = Image.new("RGB", self.__WallpaperSize, color=self.__BackgroundColor)
        d = ImageDraw.Draw(img)
        
        text_fnt = ImageFont.truetype(self.__FontType, self.__FontSize)
        text_size = self.__TextSize(d, self.__Text, text_fnt)
        d.text(self.__Center(text_size), self.__Text, font=text_fnt, fill=self.__FontColor)

        author_fnt = ImageFont.truetype(self.__FontType, self.__AuthorFontSize)
        author_size = self.__TextSize(d, self.__Author, author_fnt)
        d.text(self.__PositionAuthor(text_size, author_size), self.__Author, font=author_fnt, fill=self.__FontColor)

        self.__img = img


    def SaveWallpaper(self):
        self.__img.save(self.__path)


    def ShowWallpaper(self):
        self.__img.show()
    
