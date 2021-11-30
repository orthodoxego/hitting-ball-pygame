import pygame

from game_classes.goldboxengine import GoldBoxEngine
from setup.setup import Setup
from game_classes.player import Player
from game_classes.textures import Textures
from game_classes.ball import Ball
from view.view import View
from controller.controller import Controller

class HitHitEngine:

    def __init__(self, game):
        """Инициализация:
        -- текстуры;
        -- класс игрока;
        -- класс шара;
        -- класс вывода изображений;
        -- контроллер."""
        textures = Textures()
        self.__player = Player(textures.player)
        self.__ball = Ball(textures.ball)
        self.__view = View()
        self.__controller = Controller(self.__player)
        self.__gold_boxes = []
        self.__gold_box_engine = GoldBoxEngine(textures.goldbox)
        self.__gold_box_engine.create_boxes()

        self.game = game

    def draw(self, scene: pygame.display):
        """Взаимодействие с View."""
        for goldbox in self.__gold_box_engine.boxes:
            self.__view.goldbox_draw(scene, goldbox)

        self.__view.player_draw(scene, self.__player)
        self.__view.ball_draw(scene, self.__ball)


    def __is_ball_down_screen(self):
        """Шарик вылетел за нижнюю границу экрана. СТОП."""
        if self.__ball.ball.rect.y > Setup.screen_height:
            return False
        return True

    def check_collision_player_and_ball(self, a, b, delta):
        """Проверяет столкновение мяча и площадки"""

        player = self.__player
        ball = self.__ball

        # Необходимо для восстановления позиции площадки после удара мяча
        last_y = player.y
        player.y += player.energy_y

        # В случае столкновения:
        # Если ЛКМ нажата, то просто меняет вертикальную скорость
        # Если нет, то увеличивает на величину enegry_y для игрока
        if a.colliderect(b):
            if self.__controller.lkm_pressed:
                # Если в этот момент левая кнопка нажата, то просто увеличить вертикальную скорость.
                ball.speed_y = -ball.speed_y * Setup.correct_up
            else:
                # Если в этот момент левая кнопка отпущена.
                # Добавляем ускорение от величины ускорения площадки.
                ball.speed_y = -ball.speed_y * Setup.correct_up + (player.energy_y * Setup.multiple_energy) * -1
                ball.y = player.y - ball.height
                if abs(ball.speed_y) > Setup.FPS * 0.5:
                    player.energy_y = Setup.max_energy_player // 2

            # Вычисляет смещение от центра площадки
            center_p = player.x + player.width // 2
            center_b = ball.x + ball.width // 2

            # Горизонтальная скорость в зависимости от смещения от центра
            ball.speed_x = (ball.speed_x + (center_b - center_p) * Setup.angle_correction * delta) / 2

            # Если шар проваливается в площадку
            if ball.y + ball.height > player.y:
                ball.y = player.y - ball.height

                
        player.y = last_y

    def act(self, pygame, delta: float):
        """Обработка данных в главном цикле."""
        result = True
        # Проверяет, вылетел ли шар вниз
        # result *= self.__is_ball_down_screen()

        # Обработка ввода
        result *= self.__controller.act(pygame, delta)

        # Движение шарика .act()
        self.__ball.act(delta)

        # Движение ящиков .act()
        self.__gold_box_engine.act(delta)

        # Проверяет соударение шара и площадки
        self.check_collision_player_and_ball(self.__player.player.rect, self.__ball.ball.rect, delta)

        return result



