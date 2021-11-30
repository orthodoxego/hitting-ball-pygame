import pygame
from setup.setup import Setup
from game_classes.player import Player
from game_classes.textures import Textures
from view.view import View
from controller.controller import Controller

class HitHitEngine:

    def __init__(self):
        textures = Textures()
        self.__player = Player(textures.player, textures.player_rect)
        self.__view = View()
        self.__controller = Controller(self.__player)

    def draw(self, pygame: pygame, scene: pygame.display):
        self.__view.player_draw(pygame, scene, self.__player)

    def act(self, pygame, delta: float):
        result = True
        result *= self.__controller.act(pygame, delta)

        return result



