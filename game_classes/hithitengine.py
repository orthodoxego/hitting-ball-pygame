import pygame

from background.Stars import Stars
from setup.setup import Setup
from font.text import Text
from view.view import View
from controller.controller import Controller
from game_classes.player import Player
from game_classes.textures import Textures
from game_classes.ball import Ball
from game_classes.Score import Score
from game_classes.nloengine import NLOEngine

class HitHitEngine:

    def __init__(self, game):
        """Инициализация:
        -- текстуры;
        -- класс игрока;
        -- класс шара;
        -- класс вывода изображений;
        -- класс-обработчик очков;
        -- класс работы с текстом;
        -- звёзды;
        -- контроллер."""
        textures = Textures()
        self.__player = Player(textures.player)
        self.__ball = Ball(textures.ball)
        self.__view = View()
        self.__score = Score()
        self.__text = Text()
        self.__stars = Stars(Setup.stars, Setup.screen_width, Setup.screen_height)
        self.__controller = Controller(self.__player)
        self.__nlo = []
        self.__nlo_engine = NLOEngine(textures.nlo)
        self.__nlo_engine.create_nlo()

        self.game = game
        self.current_frame = 0
        self.__max_frame = Setup.FPS * 50

    def draw(self, scene: pygame.display):
        """Взаимодействие с View."""

        # Сначала вывод звёзд, т.к. они должны быть по фону, "ниже" всего остального
        self.__view.stars_draw(scene, self.__stars.stars)

        # Вывод инопланетных кораблей
        for nlo in self.__nlo_engine.nlo:
            self.__view.nlo_draw(scene, nlo)

        # Площадка и шар
        self.__view.player_draw(scene, self.__player)
        self.__view.ball_draw(scene, self.__ball)

        # Текстовые сообщения
        txt = self.__text.getStringIntText("Очки: ", self.__score, (255, 100, 100))
        self.__view.text_draw(scene, txt, 20, 20)
        txt = self.__text.getStringIntText("Рекорд: ", self.__score.max_score, (255, 100, 100))
        self.__view.text_draw(scene, txt, Setup.screen_width - txt.get_width() * 1.2, 20)

        if self.current_frame < Setup.FPS * 10:
            self.__view.text_draw(scene, self.__text.help_surface_text, self.__text.help_surface_text.get_height(), Setup.screen_height - self.__text.help_surface_text.get_height() * 1.5)

        self.current_frame += 1
        if self.current_frame > self.__max_frame:
            self.current_frame = Setup.FPS * 10


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
            # ball.speed_x = ball.speed_x + ((center_b - center_p) * Setup.angle_correction) * delta

            # Горизонтальная скорость без зависимости от смещения от центра
            ball.speed_x = (center_b - center_p) * Setup.angle_correction * delta


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
        self.__nlo_engine.act(delta)

        # Проверка столкновения шара и ящиков
        self.__nlo_engine.check_collision_ball_and_nlo(self.__ball, self.__score)

        # Проверяет соударение шара и площадки
        self.check_collision_player_and_ball(self.__player.player.rect, self.__ball.ball.rect, delta)

        # Движение звёзд
        self.__stars.act(delta)

        return result



