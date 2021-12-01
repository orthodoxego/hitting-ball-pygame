import pygame
from dataclasses import dataclass
from setup.setup import Setup

@dataclass
class BallData:
    """x и y выделены для повышения точности расчётов,
    т.к. координаты в rect только целочисленные."""
    x: float
    y: float

    speed_x: float
    speed_y: float

    skin: pygame.image
    rect: pygame.rect

class Ball:

    def __init__(self, skin):
        """Определяет позицию шара на экране."""
        rect = skin.get_rect(bottomright=(skin.get_width(), skin.get_height()))
        x = (Setup.screen_width - rect.width) // 2
        y = (Setup.screen_height - rect.height) // 2
        rect.x, rect.y = x, y
        self.ball = BallData(x=x, y=y, skin=skin, rect=rect, speed_x=Setup.speed_ball_x, speed_y=Setup.speed_ball_y)

        # Сколько раз шар вывалился за нижнюю границу экрана
        self.__count_drop_ball = 0

    @property
    def count_drop_ball(self):
        return self.__count_drop_ball

    @count_drop_ball.setter
    def count_drop_ball(self, value):
        self.__count_drop_ball = value

    def incDropBall(self):
        self.__count_drop_ball += 1

    def __reset_ball(self):
        self.ball.x = (Setup.screen_width - self.width) // 2
        self.ball.y = self.height
        self.ball.speed_x = Setup.speed_ball_x
        self.ball.speed_y = Setup.speed_ball_y
        self.ball.rect.x = self.ball.x
        self.ball.rect.y = self.ball.y

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
        self.ball.rect.x = int(value)
        self.ball.x = value

    @property
    def y(self):
        return self.ball.rect.y

    @y.setter
    def y(self, value):
        self.ball.rect.y = int(value)
        self.ball.y = value

    def __change_speed(self, delta):
        """Изменение скорости по X и Y."""
        self.x += self.ball.speed_x * delta
        self.ball.speed_y += Setup.ball_acceleration
        self.y += self.ball.speed_y * delta

    def act(self, delta):
        # Прирастить скорость
        self.__change_speed(delta)
        # Проверить соударения со стенами
        self.__check_up_down_left_right(delta)

    def collision_up(self, delta):
        self.y = 0
        self.ball.speed_y = Setup.FPS * 1.2 * delta

    def __check_up_down_left_right(self, delta):
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

        # Если выходит за нижнюю границу сцены + 100%
        if self.y > Setup.screen_height * 2:
            # Увеличить количество "выпадений" за границу экрана
            self.incDropBall()
            self.__reset_ball()





