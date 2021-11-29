import pygame
from dataclasses import dataclass
from setup.setup import Setup

@dataclass
class PlayerData:
    x: int
    y: int
    skin: pygame.image
    rect: pygame.rect

class Player:

    def __init__(self, skin: pygame.image, rect: pygame.rect):
        x = (Setup.screen_width - rect.width) // 2
        y = Setup.screen_height - rect.height * 10
        self.pd = PlayerData(x=x, y=y, skin=skin, rect=rect)

    @property
    def width(self):
        return self.pd.rect.width

    @property
    def x(self):
        return self.pd.x

    @x.setter
    def x(self, x):
        if x < 0:
            x = 0
        if x > Setup.screen_width - self.pd.rect.width:
            x = Setup.screen_width - self.pd.rect.width
        self.pd.x = x

    def draw(self, pygame: pygame, scene: pygame.display):
        scene.blit(self.pd.skin, (self.pd.x, self.pd.y))