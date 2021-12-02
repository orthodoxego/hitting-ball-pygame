import pygame
from random import randint

from game_classes.explosion import Explosion
from game_classes.score import Score
from setup.setup import Setup
from game_classes.nlo import NLO

class NLOEngine:

    def __init__(self, texture_nlo, textureExplosion):
        self.nlo = []
        self.__count_nlo = Setup.start_count_nlo
        self.texture_nlo = texture_nlo
        self.__textureExplosion = textureExplosion
        self.__explosions = []

    @property
    def explosions(self):
        return self.__explosions

    @property
    def count_nlo(self):
        return self.__count_nlo

    @count_nlo.setter
    def count_nlo(self, value):
        self.__count_nlo = value

    def append_nlo(self):
        self.nlo.append(NLO(Setup.screen_width + randint(0, int(Setup.screen_width)),
                            randint(0, int(Setup.screen_height * 0.65)),
                            self.texture_nlo, randint(int(Setup.screen_width * 0.1),
                                                            int(Setup.screen_width * 0.25)) * -1,
                            0))

    def create_nlo(self):
        self.nlo.clear()

        for i in range(self.__count_nlo):
            self.append_nlo()

    def act(self, delta):
        for nlo in self.nlo:
            nlo.act(delta)



        for expl in self.__explosions:
            expl.incFrame(delta * 15)
            if not expl.enabled:
                self.__explosions.remove(expl)

        for i in range(len(self.nlo) - 1, -1, -1):
            if self.nlo[i].x + self.nlo[i].width < 0:
                self.nlo.remove(self.nlo[i])

        if len(self.nlo) < self.__count_nlo:
            self.append_nlo()

    def check_collision_ball_and_nlo(self, ball):
        """Проверка столкновений шара и НЛО."""
        count_collision = {"COUNT": 0, "RIGHT": False, "LEFT": False, "UP": False, "DOWN": False}
        for nlo in self.nlo:
            if ball.ball.rect.colliderect(nlo.rect):
                self.__explosions.append(Explosion(nlo.x, nlo.y, self.__textureExplosion))
                count_collision["COUNT"] += 1
                count_collision.update(self.run_collision(nlo, ball.ball))
        return count_collision


    def run_collision(self, a, b):
        # Проверка столкновения: верх, низ, лево, право
        ret = {"RIGHT": False, "LEFT": False, "UP": False, "DOWN": False}

        lX_ball = b.x                   # Левая граница шара
        rX_ball = b.x + b.rect.width    # Правая граница шара
        uY_ball = b.y                   # Верхняя граница шара
        dY_ball = b.y + b.rect.height   # Нижняя граница шара

        lX_NLO = a.x                    # Левая граница НЛО
        rX_NLO = a.x + a.width          # Правая граница НЛО
        uY_NLO = a.y                    # Верхняя граница НЛО
        dY_NLO = a.y + a.height         # Нижняя граница НЛО

        if uY_ball >= uY_NLO:
            # Нижняя граница
            ret["DOWN"] = True
        elif dY_ball <= dY_NLO:
            # Верхняя граница
            ret["UP"] = True

        if rX_ball <= rX_NLO:
            # Слева
            ret["LEFT"] = True
        elif lX_ball >= lX_NLO:
            # Справа
            ret["RIGHT"] = True


        # Убрать НЛО за левую границу экрана, чтобы удалилась
        a.x = -a.width * 2

        return ret