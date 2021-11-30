import pygame

class Textures:

    def __init__(self):
        # Текстура игрока
        self.player = pygame.image.load('png/player.png')

        # Текстура шара
        self.ball = pygame.image.load('png/ball.png')

        # Текустура сундука
        self.goldbox = pygame.image.load('png/goldbox.png')

