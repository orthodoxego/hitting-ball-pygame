class Explosion:

    def __init__(self, x, y, textures):
        self.__x = x
        self.__y = y
        self.__textures = textures
        self.__frame = 0
        self.enabled = True

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def frame(self):
        return self.__frame

    @property
    def texture(self):
        if int(self.__frame) < len(self.__textures):
            return self.__textures[int(self.__frame)]
        return self.__textures[0]

    def incFrame(self, delta):
        self.__frame += delta
        if int(self.__frame) == len(self.__textures):
            self.enabled = False