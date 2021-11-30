import pygame
from dataclasses import dataclass
from setup.setup import Setup

@dataclass
class BallData:
    speed_x: float
    speed_y: float

    skin: pygame.image
    rect: pygame.rect

class Ball:

    def __init__(self, skin):
        rect = skin.get_rect(bottomright=(skin.get_width(), skin.get_height()))
        x = (Setup.screen_width - rect.width) // 2
        y = (Setup.screen_height - rect.width) // 2
        rect.x, rect.y = x, y
        self.ball = BallData(skin=skin, rect=rect, speed_x=Setup.speed_ball_x, speed_y=Setup.speed_ball_y)

    @property
    def speed_y(self):
        return self.ball.speed_y

    @speed_y.setter
    def speed_y(self, value):
        self.ball.speed_y = value

    @property
    def speed_x(self):
        return self.ball.speed_x

    @speed_x.setter
    def speed_x(self, value):
        self.ball.speed_x = value

    @property
    def width(self):
        return self.ball.rect.width

    @property
    def height(self):
        return self.ball.rect.height

    @property
    def x(self):
        return self.ball.rect.x

    @x.setter
    def x(self, value):
        self.ball.rect.x = value
        return

    @property
    def y(self):
        return self.ball.rect.y

    @y.setter
    def y(self, value):
        self.ball.rect.y = value
        return

    def __change_speed(self, delta):
        """Изменение скорости по X и Y."""
        self.x += self.ball.speed_x
        self.ball.speed_y += Setup.ball_acceleration
        self.y += self.ball.speed_y * delta

    def act(self, delta):
        # Прирастить скорость
        self.__change_speed(delta)
        # Проверить соударения со стенами
        self.__check_up_left_right(delta)

    def collision_up(self, delta):
        self.y = 0
        self.ball.speed_y = Setup.FPS * 50 * delta

    def __check_up_left_right(self, delta):
        """Проверяет соударение с границами экрана
        и изменяет координаты и скорость."""

        # Столкновение с препятствием сверху
        if self.y < 0:
            self.collision_up(delta)

        # Правая граница
        if self.x + self.width > Setup.screen_width:
            self.ball.speed_x = -self.ball.speed_x * 0.98
            self.x = Setup.screen_width - self.width

        # Левая граница
        if self.x < 0:
            self.ball.speed_x = -self.ball.speed_x * 0.98
            self.x = 0





