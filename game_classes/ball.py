import pygame
from dataclasses import dataclass
from setup.setup import Setup

@dataclass
class BallData:
    x: float
    y: float

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
        self.ball = BallData(x=x, y=y, skin=skin, rect=rect, speed_x=Setup.speed_ball_x, speed_y=Setup.speed_ball_y)

    @property
    def width(self):
        return self.ball.rect.width

    def __set_speed(self, delta):
        self.ball.x += self.ball.speed_x
        self.ball.speed_y += Setup.ball_acceleration
        self.ball.y += self.ball.speed_y * delta

    def act(self, delta):
        # Прирастить скорость
        self.__set_speed(delta)

        # Проверить соударения со стенами
        self.__check_up_left_right()

        # Установить прямоугольник для столкновений
        self.ball.rect.x, self.ball.rect.y = self.ball.x, self.ball.y


    def __check_up_left_right(self):
        """Проверяет соударение и изменяет координаты и скорости."""
        if self.ball.y < 0:
            self.ball.y = 0
            self.ball.speed_y = 100
