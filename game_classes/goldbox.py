import pygame

class GoldBox:
    def __init__(self, x, y, texture, speed_x, speed_y):
        self.__speed_x = speed_x
        self.__speed_y = speed_y
        self.__texture = texture
        self.__rect = pygame.Rect((x, y, texture.get_width(), texture.get_height()))

    @property
    def texture(self):
        return self.__texture

    @property
    def width(self):
        return self.__rect.width

    @property
    def height(self):
        return self.__rect.height

    @property
    def x(self):
        return self.__rect.x

    @x.setter
    def x(self, value):
        self.__rect.x = value

    @property
    def y(self):
        return self.__rect.y

    @y.setter
    def y(self, value):
        self.__rect.y = value

    def act(self, delta):
        self.x += self.__speed_x * delta
        self.y += self.__speed_y * delta