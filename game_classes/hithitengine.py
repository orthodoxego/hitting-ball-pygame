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

        self.check_collision_player_and_ball(self.__player.player.rect, self.__ball.ball.rect, delta)

        return result

    def check_collision_player_and_ball(self, a, b, delta):
        """Проверяет столкновение мяча и площадки"""
        
        player = self.__player.player
        ball = self.__ball.ball

        last_y = player.rect.y
        player.rect.y += player.energy_y

        # В случае столкновения:
        # Если ЛКМ нажата, то просто меняет вертикальную скорость
        # Если нет, то увеличивает на величину enegry_y для игрока
        if a.colliderect(b):
            if self.__controller.lkm_pressed:
                """Если в этот момент левая кнопка нажата."""
                ball.speed_y = -ball.speed_y * Setup.correct_up
            else:
                """Если в этот момент левая кнопка отпущена.
                Добавляем ускорение от площадки"""
                ball.speed_y = -ball.speed_y * Setup.correct_up + (player.energy_y * Setup.multiple_energy) * -1
                ball.y = player.y - ball.rect.height
                if abs(ball.speed_y) > Setup.FPS * 0.5:
                    player.energy_y = Setup.max_energy_player // 2

            # Вычисляет смещение от центра площадки
            center_p = player.x + player.rect.width // 2
            center_b = ball.x + ball.rect.width // 2

            # Горизонтальная скорость в зависимости от смещения от центра
            ball.speed_x = (ball.speed_x + (center_b - center_p) * Setup.angle_correction * delta) / 2

            # Если шар провливается в площадку
            if ball.rect.y + ball.rect.height > player.rect.y:
                ball.rect.y = player.rect.y - ball.rect.height
                ball.y = ball.rect.y
                self.__ball.update_rect()
                
        player.rect.y = last_y




