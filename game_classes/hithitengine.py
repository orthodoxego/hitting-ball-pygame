import pygame
from setup.setup import Setup
from game_classes.player import Player
from game_classes.textures import Textures

class HitHitEngine:

    def __init__(self):
        textures = Textures()
        self.player = Player(textures.player, textures.player_rect)
        self.mouse_button_1_down = False

    def draw(self, pygame: pygame, scene: pygame.display):
        self.player.draw(pygame, scene)

    def __inc_energy_from_mouse_1_button(self, delta):
        """Увеличивает энергию для отскока."""
        self.player.inc_energy(delta)

    def __dec_energy_from_mouse_1_button(self, delta):
        """Увеличивает энергию для отскока."""
        self.player.dec_energy(delta)

    def __check_mouse(self, delta):
        """Изменяет координаты площадки игрока в зависимости
        от положения курсора мыши."""
        x = pygame.mouse.get_pos()[0]
        y = pygame.mouse.get_pos()[1]

        # Смещение в зависимости от курсора: слева или справа
        if x < self.player.x:
            self.player.x -= (Setup.speed_player + (self.player.x - x) * 2) * delta
            pass
        if x > self.player.x + self.player.width:
            self.player.x += (Setup.speed_player + (x - self.player.x - self.player.width) * 2) * delta

    def act(self, delta: float):
        delta /= 1000

        if self.mouse_button_1_down:
            self.__inc_energy_from_mouse_1_button(delta)
        else:
            self.__dec_energy_from_mouse_1_button(delta)


        if pygame.mouse.get_focused():
            self.__check_mouse(delta)


    def check_keys(self, events):

        for event in events:

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.mouse_button_1_down = True
                return True

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.mouse_button_1_down = False
                return True

            elif event.type == pygame.QUIT:
                return False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
                elif event.key == pygame.K_LEFT:
                    print("ВЛЕВО")
                elif event.key == pygame.K_RIGHT:
                    print("ВПРАВО")
                elif event.key == pygame.K_UP:
                    print("ВВЕРХ")
                elif event.key == pygame.K_DOWN:
                    print("ВНИЗ")

        return True




