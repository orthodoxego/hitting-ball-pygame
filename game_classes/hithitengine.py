import pygame
from setup.setup import Setup
from game_classes.player import Player
from game_classes.textures import Textures

class HitHitEngine:

    def __init__(self):
        textures = Textures()
        self.player = Player(textures.player, textures.player_rect)

    def draw(self, pygame: pygame, scene: pygame.display):
        self.player.draw(pygame, scene)

    def __check_mouse(self, delta):
        """Изменяет координаты площадки игрока в зависимости
        от положения курсора мыши."""
        x = pygame.mouse.get_pos()[0]
        y = pygame.mouse.get_pos()[1]

        if x < self.player.x:
            self.player.x -= (Setup.speed_player + (self.player.x - x) * 2) * delta
        if x > self.player.x + self.player.width:
            self.player.x += (Setup.speed_player + (x - self.player.x) * 2) * delta

    def act(self, delta: float):
        delta /= 1000

        if pygame.mouse.get_focused():
            self.__check_mouse(delta)



