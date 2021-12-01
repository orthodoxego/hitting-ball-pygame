class TextEffect:

    def __init__(self, text):
        self.__text = text
        self.__number = 0

    @property
    def text(self):
        return self.__text[0:self.__number]

    def tick(self):
        if self.__number < len(self.__text):
            self.__number += 1

    def resetNumber(self):
        self.__number = 0