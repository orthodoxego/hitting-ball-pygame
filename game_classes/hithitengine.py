import pygame

from game_classes.ball import Ball
from setup.setup import Setup
from game_classes.player import Player
from game_classes.textures import Textures
from view.view import View
from controller.controller import Controller

class HitHitEngine:

    def __init__(self):
        textures = Textures()
        self.__player = Player(textures.player)
        self.__ball = Ball(textures.ball)
        self.__view = View()
        self.__controller = Controller(self.__player)

    def draw(self, scene: pygame.display):
        self.__view.player_draw(scene, self.__player)
        self.__view.ball_draw(scene, self.__ball)

    def act(self, pygame, delta: float):
        result = True
        result *= self.__controller.act(pygame, delta)

        # Движение шарика
        self.__ball.act(delta)

        self.check_collision_player_and_ball(self.__player.player.rect, self.__ball.ball.rect)

        return result

    def check_collision_player_and_ball(self, a, b):
        """Проверяет столкновение мяча и площадки"""
        last_y = self.__player.player.rect.y
        self.__player.player.rect.y += self.__player.player.energy_y

        if a.colliderect(b):
            if self.__controller.lkm_pressed:
                self.__ball.ball.speed_y = -self.__ball.ball.speed_y * 0.75
            else:
                self.__ball.ball.speed_y = -self.__ball.ball.speed_y * 0.75 + (self.__player.player.energy_y * Setup.multiple_energy) * -1
                self.__ball.ball.y = self.__player.player.y - self.__ball.ball.rect.height
                self.__player.player.energy_y = Setup.max_energy_player // 2

        # Останавливает шар
        if abs(self.__ball.ball.speed_y) < 1:
            self.__ball.ball.speed_y = 0

        self.__player.player.rect.y = last_y




