import pygame

class Textures:

    def __init__(self):
        self.player = pygame.image.load('png/player.png')
        self.player_rect = self.player.get_rect(bottomright=(self.player.get_width(), self.player.get_height()))

