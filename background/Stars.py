from random import randint, choice
from setup.setup import Setup


class Stars:

    def __init__(self, n, width, height):
        self.width = width
        self.height = height
        self.stars = []
        for i in range(n):
            color = randint(100, 200)
            self.stars.append([randint(0, self.width),   # 0 x
                               randint(0, self.height),   # 1 y
                               choice([-self.width // 4, -self.width // 8, -self.width // 16, -self.width // 32]), # 2 speed_x
                               0, # 3 speed_y
                               (color, color, color)]) # 4 color

    def act(self, delta):
        for star in self.stars:
            star[0] += star[2] * delta
            star[1] += star[3] * delta
            if star[0] < 0:
                star[0] = self.width
            if star[0] > self.width:
                star[0] = 0
            if star[1] < 0:
                star[1] = self.height
            if star[1] > self.height:
                star[1] = 1
