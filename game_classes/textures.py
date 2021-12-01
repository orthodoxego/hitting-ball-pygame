import pygame

class Textures:

    def __init__(self):
        # Текстура игрока
        self.player = pygame.image.load('png/player.png')

        # Текстура шара
        self.ball = pygame.image.load('png/ball.png')

        # Текстура призрачного шара
        self.ghost_ball = pygame.image.load('png/ghost_ball.png')

        # Текустура НЛО
        self.nlo = pygame.image.load('png/nlo.png')

