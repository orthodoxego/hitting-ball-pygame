import pygame
from random import randint

from game_classes.Score import Score
from setup.setup import Setup
from game_classes.nlo import NLO

class NLOEngine:

    def __init__(self, texture_nlo):
        self.nlo = []
        self.count_nlo = Setup.start_count_nlo
        self.texture_nlo = texture_nlo

    def append_nlo(self):
        self.nlo.append(NLO(Setup.screen_width + randint(0, int(Setup.screen_width)),
                            randint(0, int(Setup.screen_height * 0.65)),
                            self.texture_nlo, randint(int(Setup.screen_width * 0.1),
                                                            int(Setup.screen_width * 0.25)) * -1,
                            0))

    def create_nlo(self):
        self.nlo.clear()

        for i in range(self.count_nlo):
            self.append_nlo()

    def act(self, delta):
        for nlo in self.nlo:
            nlo.act(delta)

        for i in range(len(self.nlo) - 1, -1, -1):
            if self.nlo[i].x + self.nlo[i].width < 0:
                self.nlo.remove(self.nlo[i])

        if len(self.nlo) == 0:
            self.create_nlo()

    def check_collision_ball_and_nlo(self, ball, score: Score):
        """Проверка столкновений шара и ящиков."""

        for nlo in self.nlo:
            if ball.ball.rect.colliderect(nlo.rect):
                score += 1
                nlo.x = -nlo.width

