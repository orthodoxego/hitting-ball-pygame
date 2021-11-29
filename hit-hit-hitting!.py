import pygame
from setup.setup import Setup
from game_classes.hithitengine import HitHitEngine

class Game:
    """Класс-шаблон для игр на базе pygame."""

    def __init__(self, width, height, caption, fps):
        """Конструктор, настройка основных параметров."""
        pygame.init()

        if width + height == 0:
            width = pygame.display.Info().current_w
            height = pygame.display.Info().current_h
            self.scene = pygame.display.set_mode(flags=pygame.FULLSCREEN)
        else:
            self.__size = [width, height]
            self.scene = pygame.display.set_mode(self.__size)
            pygame.display.set_caption(caption)

        Setup.screen_width = width
        Setup.screen_height = height

        self.__size = [Setup.screen_width, Setup.screen_height]
        self.clock = pygame.time.Clock()

        self.playGame = True
        self.__delta = 0

        self.__hit_engine = HitHitEngine()

    @property
    def WIDTH(self):
        return self.__WIDTH

    @property
    def HEIGHT(self):
        return self.__HEIGHT

    def run(self):
        """Главный цикл игры."""
        while (self.playGame):

            # Проверяем нажатые клавиши и события мыши
            self.playGame = self.__hit_engine.check_keys(pygame.event.get())

            self.scene.fill(Setup.BLACK)

            self.__hit_engine.draw(pygame, self.scene)
            self.__hit_engine.act(self.__delta)

            pygame.display.flip()

            self.__delta = self.clock.tick(Setup.FPS)

        pygame.quit()


if __name__ == "__main__":
    game = Game(Setup.screen_width, Setup.screen_height, "Бах-бах-набиваем мяч", 60)
    # game = Game(0, 0, "Бах-бах-набиваем мяч", 60)
    game.run()