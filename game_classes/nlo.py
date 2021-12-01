import pygame

class NLO:
    def __init__(self, x, y, texture, speed_x, speed_y):
        self.__speed_x = speed_x
        self.__speed_y = speed_y
        self.__texture = texture
        self.__x = x
        self.__y = y
        self.__width = texture.get_width()
        self.__height = texture.get_height()
        self.__rect = pygame.Rect((0, 0, 0, 0))

    def __getRect(self):
        self.__rect.x = int(self.x + self.width * 0.25)
        self.__rect.y = int(self.y + self.height * 0.25)
        self.__rect.width = int(self.__width * 0.5)
        self.__rect.height = int(self.__height * 0.5)
        return self.__rect

    @property
    def rect(self):
        return self.__getRect()

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
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

    @property
    def speed_x(self):
        return self.__speed_x

    @property
    def speed_y(self):
        return self.__speed_y

    def act(self, delta):
        self.x += self.__speed_x * delta
        self.y += self.__speed_y * delta
        self.__rect = self.__getRect()
