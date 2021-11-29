import pygame
class Setup:

    # ФПС
    FPS = 60

    # Ширина и высота окна для оконного режима
    screen_width = 1024
    screen_height = 768

    # Скорость движения площадки за мышью, по горизонтали
    speed_player = FPS * 2

    # Максимальная энергия для отскока
    max_energy_player = 64

    # Цвета
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)