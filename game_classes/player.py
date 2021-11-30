import pygame
from dataclasses import dataclass
from setup.setup import Setup


@dataclass
class PlayerData:
    # Координаты (ваш Кэп)
    x: int
    y: int

    # Скин и прямоугольник для расчётов столкновения
    skin: pygame.image
    rect: pygame.rect

    # Энергия для удара
    energy_y: float = 0


class Player:
    """Математическая модель игрока. Инкапсулированы действия над моделью."""

    def __init__(self, skin: pygame.image):
        """Определение координат по центру."""
        rect = skin.get_rect(bottomright=(skin.get_width(), skin.get_height()))
        x = (Setup.screen_width - rect.width) // 2
        y = Setup.screen_height - rect.height * 10
        rect.x, rect.y = x, y
        self.player = PlayerData(x=x, y=y, skin=skin, rect=rect)

    @property
    def width(self):
        """Вернёт ширину текстуры площадки."""
        return self.player.rect.width

    @property
    def x(self):
        """Вернёт координату X игрока."""
        self.player.rect.x = self.player.x
        return self.player.x

    @x.setter
    def x(self, x):
        """Контролируемая установка координаты X игрока."""
        if x < 0:
            x = 0
        if x > Setup.screen_width - self.player.rect.width:
            x = Setup.screen_width - self.player.rect.width
        self.player.x = x
        self.player.rect.x = self.player.x


    @property
    def y(self):
        """Вернёт координату Y игрока."""
        self.player.rect.y = self.player.y
        return self.player.x

    @y.setter
    def y(self, y):
        self.player.y = y
        self.player.rect.y = self.player.y

    def mouse_button1_pressed(self, delta):
        """ЛКМ удерживается."""
        self.inc_energy(delta)

    def mouse_button1_unpressed(self, delta):
        """ЛКМ отпущена."""
        self.dec_energy(delta)

    def inc_energy(self, delta):
        """Увеличение энергии удара. Площадка смещается вниз."""
        self.player.energy_y += (Setup.max_energy_player + self.player.energy_y * 5) * delta
        if self.player.energy_y > Setup.max_energy_player:
            self.player.energy_y = Setup.max_energy_player


    def dec_energy(self, delta):
        """Уменьшение энергии удара. Площадка смещается вверх."""
        self.player.energy_y -= Setup.max_energy_player * 50 * delta
        if self.player.energy_y < 0:
            self.player.energy_y = 0

    def move_left(self, delta, x):
        """Смещение влево по координате мыши"""
        self.x -= (Setup.speed_player + (self.x - x) * 2) * delta

    def move_right(self, delta, x):
        """Смещение вправо по координате мыши"""
        self.x += (Setup.speed_player + (x - self.x - self.width) * 2) * delta
