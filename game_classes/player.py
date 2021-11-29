import pygame
from dataclasses import dataclass
from setup.setup import Setup

@dataclass
class PlayerData:
    # Координаты (ваш Кэп)
    x: int
    y: int

    # Скин и прямоугольник для расчётов столкновения
    skin: pygame.image
    rect: pygame.rect

    # Энергия для удара
    energy_y: float = 0

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

    def inc_energy(self, delta):
        self.pd.energy_y += (Setup.max_energy_player + self.pd.energy_y) * delta
        if self.pd.energy_y > Setup.max_energy_player:
            self.pd.energy_y = 0

    def dec_energy(self, delta):
        self.pd.energy_y -= Setup.max_energy_player * 50 * delta
        if self.pd.energy_y < 0:
            self.pd.energy_y = 0


    def draw(self, pygame: pygame, scene: pygame.display):
        pd = self.pd
        scene.blit(pd.skin, (pd.x, pd.y + int(pd.energy_y)))

